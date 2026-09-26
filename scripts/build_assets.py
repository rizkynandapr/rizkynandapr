"""Builds every SVG in ../assets from the data below.

Run:  python3 scripts/build_assets.py

Each graphic is written twice, *-dark.svg and *-light.svg, and the README
picks one with <picture> so it follows the viewer's GitHub theme. Fonts are
subset to the exact characters each file uses and embedded, so the SVGs look
the same everywhere without loading anything from the network.

Fonts (SIL Open Font License): Archivo, Geist, Geist Mono. Instanced copies
live in scripts/fonts/.
"""
from __future__ import annotations

import base64
import html
import io
import pathlib

from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
FONTS = pathlib.Path(__file__).resolve().parent / "fonts"

# ---------------------------------------------------------------- palette

THEMES = {
    "dark": dict(
        bg="#0D1117", card="#0E1218", card2="#141A22", line="#1F2732", line2="#344150",
        text="#E8EDF3", text2="#C9D1DC", dim="#8C97A7", faint="#5F6A7A",
        signal="#C4EE2F", ink="#1A2400", hl="#C4EE2F", accent="#8F88FF",
        accent_soft="#1E1B4B", ok="#5FD39F", dot="#E8EDF3", dot_op="0.07",
    ),
    "light": dict(
        bg="#FFFFFF", card="#FAFBFC", card2="#F1F3F6", line="#D8DEE6", line2="#AEB8C5",
        text="#0A0F1A", text2="#1C2433", dim="#556072", faint="#7C8796",
        signal="#C4EE2F", ink="#1A2400", hl="#3A2EF0", accent="#3A2EF0",
        accent_soft="#E5E3FF", ok="#0B7A50", dot="#0A0F1A", dot_op="0.08",
    ),
}

# ---------------------------------------------------------------- fonts

FONT_FILES = {
    "display": ("Archivo-ExpandedExtraBold.ttf", "RNDisplay"),
    "sans": ("Geist-Medium.ttf", "RNSans"),
    "mono": ("GeistMono-Medium.ttf", "RNMono"),
}
_font_cache: dict[str, TTFont] = {}


def font(kind: str) -> TTFont:
    if kind not in _font_cache:
        _font_cache[kind] = TTFont(FONTS / FONT_FILES[kind][0])
    return _font_cache[kind]


def text_width(s: str, kind: str, size: float, tracking: float = 0.0) -> float:
    f = font(kind)
    cmap = f.getBestCmap()
    hmtx = f["hmtx"]
    upm = f["head"].unitsPerEm
    w = 0
    for ch in s:
        g = cmap.get(ord(ch))
        w += hmtx[g][0] if g else upm * 0.5
    return w * size / upm + tracking * max(len(s) - 1, 0)


def embed_fonts(used: dict[str, set[str]]) -> str:
    rules = []
    for kind, chars in used.items():
        if not chars:
            continue
        fname, family = FONT_FILES[kind]
        opts = subset.Options()
        opts.flavor = "woff2"
        opts.layout_features = ["kern", "liga"]
        opts.name_IDs = []
        opts.notdef_outline = True
        sub = subset.Subsetter(opts)
        f = TTFont(FONTS / fname)
        sub.populate(text="".join(sorted(chars | {" "})))
        sub.subset(f)
        buf = io.BytesIO()
        f.flavor = "woff2"
        f.save(buf)
        data = base64.b64encode(buf.getvalue()).decode()
        rules.append(f"@font-face{{font-family:{family};src:url(data:font/woff2;base64,{data}) format('woff2')}}")
    return "".join(rules)


class Svg:
    """Tiny SVG builder that tracks which characters each font draws."""

    def __init__(self, w: int, h: int, title: str, desc: str, theme: str):
        self.w, self.h = w, h
        self.t = THEMES[theme]
        self.title, self.desc = title, desc
        self.body: list[str] = []
        self.css: list[str] = []
        self.used = {"display": set(), "sans": set(), "mono": set()}

    def add(self, s: str) -> None:
        self.body.append(s)

    def text(self, x, y, s, kind="sans", size=16, fill=None, weight=None, tracking=0.0,
             anchor="start", cls="", opacity=None) -> None:
        self.used[kind].update(s)
        fam = FONT_FILES[kind][1]
        attrs = [f'x="{x}"', f'y="{y}"', f'font-family="{fam}"', f'font-size="{size}"',
                 f'fill="{fill or self.t["text"]}"']
        if tracking:
            attrs.append(f'letter-spacing="{tracking}"')
        if anchor != "start":
            attrs.append(f'text-anchor="{anchor}"')
        if cls:
            attrs.append(f'class="{cls}"')
        if opacity is not None:
            attrs.append(f'opacity="{opacity}"')
        self.add(f"<text {' '.join(attrs)}>{html.escape(s)}</text>")

    def tspans(self, x, y, parts, kind="sans", size=16) -> None:
        """parts: [(text, fill), ...] on one line."""
        fam = FONT_FILES[kind][1]
        inner = ""
        for s, fill in parts:
            self.used[kind].update(s)
            inner += f'<tspan fill="{fill}">{html.escape(s)}</tspan>'
        self.add(f'<text x="{x}" y="{y}" font-family="{fam}" font-size="{size}">{inner}</text>')

    def render(self) -> str:
        style = embed_fonts(self.used) + "".join(self.css)
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
            f'width="{self.w}" height="{self.h}" role="img" aria-labelledby="t d">'
            f'<title id="t">{html.escape(self.title)}</title><desc id="d">{html.escape(self.desc)}</desc>'
            f"<style>{style}</style>" + "".join(self.body) + "</svg>"
        )


def dot_grid(svg: Svg, pid: str, w, h, rx=20, fill=None) -> None:
    t = svg.t
    svg.add(
        f'<defs><pattern id="{pid}" width="20" height="20" patternUnits="userSpaceOnUse">'
        f'<circle cx="1.5" cy="1.5" r="1.1" fill="{t["dot"]}" fill-opacity="{t["dot_op"]}"/></pattern>'
        f'<clipPath id="{pid}c"><rect width="{w}" height="{h}" rx="{rx}"/></clipPath></defs>'
    )
    svg.add(f'<rect width="{w}" height="{h}" rx="{rx}" fill="{fill or t["card"]}" stroke="{t["line"]}"/>')
    svg.add(f'<rect width="{w}" height="{h}" rx="{rx}" fill="url(#{pid})" clip-path="url(#{pid}c)"/>')


def pill(svg: Svg, x, y, label, bg, fg, kind="mono", size=12, pad=10, tracking=1.2, h=24) -> float:
    w = text_width(label, kind, size, tracking) + pad * 2
    svg.add(f'<rect x="{x}" y="{y}" width="{w:.1f}" height="{h}" rx="6" fill="{bg}"/>')
    svg.text(x + pad, y + h / 2 + size * 0.36, label, kind, size, fg, tracking=tracking)
    return w


# ---------------------------------------------------------------- data

HEADER = dict(
    name=["Rizky Nanda", "Praditia"],
    badge="AI AUTOMATION",
    where="ENGINEER · YOGYAKARTA, INDONESIA",
    tagline=("I ship AI agents that survive ", "real customers."),
    now="From 5 Oct: IT Delivery at Cekat.AI",
    trace=[
        ("wa.in", "Kak, ponco L masih ada?"),
        ("n8n", "history(6) loaded"),
        ("claude", '{ "is_order": true, "qty": 2 }'),
        ("sheets", "Orders.append -> row 214"),
        ("owner", "alert sent"),
    ],
)

METRICS = [
    ("81.8%", "HIT RATE@5", "LegalitasAI"),
    ("<30m", "ONBOARDING", "WhatsApp template"),
    ("98%", "ACCURACY", "Clickbait LSTM"),
    ("43", "TESTS IN CI", "eval-gated"),
    ("13", "BROWSER TOOLS", "Fileloka"),
    ("30", "TEST CALLS", "Dispatch Kit"),
]

CARDS = [
    dict(slug="legalitasai", kind="RAG · GUARDRAIL", name="LegalitasAI",
         tag="Legal RAG that won't answer without proof",
         metric="81.8%", label="HIT RATE@5, UP FROM 63.6%",
         stack="FastAPI · BM25 + RRF · Qdrant · Claude · Langfuse"),
    dict(slug="fileloka", kind="WEB · PRIVACY", name="Fileloka",
         tag="PDF and image tools that never upload your file",
         metric="13", label="TOOLS, ALL IN THE BROWSER",
         stack="vanilla JS · pdf-lib · pdf.js · Canvas · strict CSP"),
    dict(slug="whatsapp", kind="AGENT · N8N", name="WhatsApp AI Chatbot",
         tag="Turns a WhatsApp number into a sales agent",
         metric="<30m", label="TO ONBOARD A NEW BUSINESS",
         stack="n8n · WhatsApp Cloud API · Claude · Sheets"),
    dict(slug="applyiq", kind="PIPELINE", name="ApplyIQ",
         tag="Resume in, ranked jobs and cover letters out",
         metric="5", label="LLM PASSES PER UPLOAD",
         stack="React 19 · pdf.js · n8n · Supabase"),
    dict(slug="talentscout", kind="PIPELINE", name="TalentScout",
         tag="CV screening on fixed, explainable weights",
         metric="40/30/20/10", label="SKILLS · EXPERIENCE · EDUCATION · ACHIEVEMENTS",
         stack="LLM gap analysis · weighted scoring · HTML dashboard"),
    dict(slug="clickbait", kind="MODEL", name="Clickbait Detector",
         tag="LSTM headline classifier, live on HF Spaces",
         metric="98%", label="ACCURACY · 0.99 PRECISION",
         stack="TensorFlow · LSTM · Streamlit · Hugging Face"),
]

SECTIONS = [
    ("bench", "01", "On the bench", "WHAT I'M BUILDING NOW"),
    ("shipped", "02", "Shipped", "PUBLIC CODE, REAL NUMBERS"),
    ("stack", "03", "Stack", "WHAT I REACH FOR"),
    ("background", "04", "Background", "WHERE I LEARNED IT"),
]

STACK = [
    ("AI / LLM", ["Claude API", "RAG (BM25 + dense)", "Langfuse", "Cekat AI", "TensorFlow", "Hugging Face"]),
    ("AUTOMATION", ["n8n", "WhatsApp Cloud API", "Webhooks", "Google Sheets"]),
    ("CODE & DATA", ["Python", "SQL", "Pandas", "FastAPI", "Streamlit"]),
    ("WEB & INFRA", ["React", "Vite", "Supabase", "Qdrant", "Docker", "Vercel"]),
]


# ---------------------------------------------------------------- graphics

def header(theme: str) -> str:
    # Sized for GitHub's ~840px README column, so small text stays readable.
    W, H = 960, 340
    s = Svg(W, H, "Rizky Nanda Praditia, AI automation engineer",
            "I ship AI agents that survive real customers. A WhatsApp message runs through n8n and Claude, "
            "an order is captured and the owner is alerted.", theme)
    t = s.t
    dot_grid(s, "g", W, H, 22)
    s.add(f'<defs><radialGradient id="glow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="{t["accent"]}" '
          f'stop-opacity="0.22"/><stop offset="1" stop-color="{t["accent"]}" stop-opacity="0"/></radialGradient></defs>')
    s.add(f'<ellipse cx="740" cy="170" rx="250" ry="160" fill="url(#glow)"/>')

    x = 44
    w = pill(s, x, 46, HEADER["badge"], t["signal"], t["ink"], size=12, tracking=1.3, h=26)
    s.text(x + w + 12, 64, "ENGINEER · YOGYAKARTA", "mono", 12, t["dim"], tracking=1.2)

    s.text(x, 140, HEADER["name"][0], "display", 54, t["text"], tracking=-1.4)
    s.text(x, 200, HEADER["name"][1], "display", 54, t["text"], tracking=-1.4)

    a, b = HEADER["tagline"]
    s.tspans(x, 248, [(a, t["text2"]), (b, t["hl"])], "sans", 20)
    caret_x = x + text_width(a + b, "sans", 20) - 2
    s.add(f'<rect class="caret" x="{caret_x:.1f}" y="232" width="2.6" height="20" rx="1" fill="{t["hl"]}"/>')

    s.add(f'<circle class="pulse" cx="{x + 6}" cy="289" r="5" fill="{t["ok"]}"/>')
    s.text(x + 20, 294, HEADER["now"], "mono", 13.5, t["text2"], tracking=0.3)

    px, py, pw, ph = 548, 36, 380, 268
    s.add(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="16" fill="{t["card2"]}" stroke="{t["line"]}"/>')
    s.add(f'<line x1="{px}" y1="{py + 40}" x2="{px + pw}" y2="{py + 40}" stroke="{t["line"]}"/>')
    s.add(f'<circle cx="{px + 20}" cy="{py + 20}" r="4" fill="{t["ok"]}" class="pulse"/>')
    s.text(px + 32, py + 25, "trace // wa-agent", "mono", 12.5, t["dim"], tracking=0.4)
    s.text(px + pw - 18, py + 25, "LIVE", "mono", 11.5, t["ok"], tracking=1.6, anchor="end")

    top, gap = py + 72, 44
    nx = px + 28
    s.add(f'<line x1="{nx}" y1="{top}" x2="{nx}" y2="{top + gap * 4}" stroke="{t["line2"]}" stroke-width="1.5"/>')
    s.add(f'<line class="flow" x1="{nx}" y1="{top}" x2="{nx}" y2="{top + gap * 4}" stroke="{t["hl"]}" '
          f'stroke-width="1.5" stroke-dasharray="4 8"/>')
    for i, (tag, detail) in enumerate(HEADER["trace"]):
        cy = top + i * gap
        s.add(f'<circle cx="{nx}" cy="{cy}" r="7" fill="{t["card2"]}" stroke="{t["line2"]}" stroke-width="1.5"/>')
        s.add(f'<circle class="node n{i}" cx="{nx}" cy="{cy}" r="7" fill="{t["hl"]}"/>')
        s.text(nx + 20, cy + 4, tag.upper(), "mono", 11, t["faint"], tracking=1)
        color = t["accent"] if tag == "claude" else t["text"]
        s.text(nx + 84, cy + 5, detail, "mono", 13, color)
    s.add(f'<circle r="4.5" fill="{t["hl"]}"><animateMotion dur="5s" repeatCount="indefinite" '
          f'path="M{nx},{top} L{nx},{top + gap * 4}"/></circle>')

    s.css.append(
        ".caret{animation:blink 1.1s steps(1) infinite}"
        "@keyframes blink{50%{opacity:0}}"
        ".pulse{animation:pulse 2.2s ease-in-out infinite}"
        "@keyframes pulse{50%{opacity:.35}}"
        ".flow{animation:flow 1.2s linear infinite}"
        "@keyframes flow{to{stroke-dashoffset:-24}}"
        ".node{opacity:0;animation:light 5s linear infinite}"
        + "".join(f".n{i}{{animation-delay:{i}s}}" for i in range(5))
        + "@keyframes light{0%,4%{opacity:0}6%,20%{opacity:1}24%,100%{opacity:0}}"
        "@media (prefers-reduced-motion:reduce){*{animation:none!important}.node{opacity:0}}"
    )
    return s.render()


def metrics(theme: str) -> str:
    W, H = 880, 116
    s = Svg(W, H, "Numbers from the projects", ", ".join(f"{v} {l.lower()} ({c})" for v, l, c in METRICS), theme)
    t = s.t
    s.add(f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="16" fill="{t["card"]}" stroke="{t["line"]}"/>')
    cw = W / len(METRICS)
    for i, (v, label, ctx) in enumerate(METRICS):
        x0 = i * cw
        if i:
            s.add(f'<line x1="{x0:.1f}" y1="20" x2="{x0:.1f}" y2="{H - 20}" stroke="{t["line"]}"/>')
        s.text(x0 + 18, 34, label, "mono", 10.5, t["dim"], tracking=0.9)
        s.text(x0 + 16, 76, v, "display", 30, t["hl"] if i == 0 else t["text"], tracking=-0.8)
        s.text(x0 + 18, 98, ctx, "mono", 11, t["faint"])
    return s.render()


def section(key: str, idx: str, title: str, meta: str, theme: str) -> str:
    W, H = 880, 56
    s = Svg(W, H, f"{idx} {title}", meta.capitalize(), theme)
    t = s.t
    s.add(f'<rect x="0" y="14" width="38" height="28" rx="7" fill="{t["accent_soft"]}"/>')
    s.text(19, 33, idx, "mono", 13.5, t["accent"], tracking=1, anchor="middle")
    s.text(52, 37, title, "display", 23, t["text"], tracking=-0.5)
    tw = 52 + text_width(title, "display", 23, -0.5) + 18
    mw = text_width(meta, "mono", 11, 1.2)
    s.add(f'<line x1="{tw:.0f}" y1="28" x2="{W - mw - 18:.0f}" y2="28" stroke="{t["line"]}"/>')
    s.text(W, 32, meta, "mono", 11, t["faint"], tracking=1.2, anchor="end")
    return s.render()


def wrap(text: str, kind: str, size: float, max_w: float) -> list[str]:
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if text_width(trial, kind, size) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    return lines


def card(c: dict, theme: str) -> str:
    # Shown two per row at ~410px, so drawn at 420 to keep text near 1:1.
    W, H = 420, 250
    s = Svg(W, H, f"{c['name']}: {c['tag']}", f"{c['metric']} {c['label'].lower()}. Stack: {c['stack']}.", theme)
    t = s.t
    dot_grid(s, "d", W, H, 16)
    pill(s, 22, 22, c["kind"], t["accent_soft"], t["accent"], size=10.5, tracking=1.2, h=22)
    s.add(f'<rect x="{W - 46}" y="20" width="26" height="26" rx="7" fill="{t["card2"]}" stroke="{t["line"]}"/>')
    s.add(f'<path d="M{W - 39} 39 L{W - 28} 28 M{W - 36} 28 H{W - 28} V36" fill="none" '
          f'stroke="{t["text2"]}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>')

    size = 27
    while text_width(c["name"], "display", size, -0.6) > W - 44 and size > 18:
        size -= 1
    s.text(22, 80, c["name"], "display", size, t["text"], tracking=-0.6)
    for i, line in enumerate(wrap(c["tag"], "sans", 14.5, W - 44)[:2]):
        s.text(22, 106 + i * 20, line, "sans", 14.5, t["dim"])

    msize = 34
    while text_width(c["metric"], "display", msize, -1) > W - 44 and msize > 22:
        msize -= 2
    s.text(21, 176, c["metric"], "display", msize, t["hl"], tracking=-1)
    s.text(22, 196, c["label"], "mono", 10.5, t["dim"], tracking=0.9)

    s.add(f'<line x1="22" y1="{H - 34}" x2="{W - 22}" y2="{H - 34}" stroke="{t["line"]}"/>')
    ssize = 11
    while text_width(c["stack"], "mono", ssize) > W - 44 and ssize > 9:
        ssize -= 0.5
    s.text(22, H - 14, c["stack"], "mono", ssize, t["faint"])
    return s.render()


def stack(theme: str) -> str:
    W = 880
    row_h = 52
    H = row_h * len(STACK) + 20
    s = Svg(W, H, "Stack", "; ".join(f"{g}: {', '.join(items)}" for g, items in STACK), theme)
    t = s.t
    s.add(f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="16" fill="{t["card"]}" stroke="{t["line"]}"/>')
    for i, (group, items) in enumerate(STACK):
        y = 10 + i * row_h
        if i:
            s.add(f'<line x1="20" y1="{y}" x2="{W - 20}" y2="{y}" stroke="{t["line"]}"/>')
        s.text(22, y + 31, group, "mono", 11, t["dim"], tracking=1.2)
        x = 150
        for item in items:
            w = text_width(item, "mono", 12.5) + 20
            s.add(f'<rect x="{x:.1f}" y="{y + 12}" width="{w:.1f}" height="28" rx="7" fill="{t["card2"]}" stroke="{t["line"]}"/>')
            s.text(round(x + 10, 1), y + 31, item, "mono", 12.5, t["text2"])
            x += w + 7
    return s.render()


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    out = {}
    for theme in THEMES:
        out[f"header-{theme}.svg"] = header(theme)
        out[f"metrics-{theme}.svg"] = metrics(theme)
        out[f"stack-{theme}.svg"] = stack(theme)
        for key, idx, title, meta in SECTIONS:
            out[f"sec-{key}-{theme}.svg"] = section(key, idx, title, meta, theme)
        for c in CARDS:
            out[f"card-{c['slug']}-{theme}.svg"] = card(c, theme)
    for name, svg in out.items():
        (ASSETS / name).write_text(svg, encoding="utf-8")
    total = sum(len(v) for v in out.values())
    print(f"wrote {len(out)} files, {total / 1024:.0f} KB total")


if __name__ == "__main__":
    main()
