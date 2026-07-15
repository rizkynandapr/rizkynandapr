<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=26&pause=1200&color=D97757&center=true&vCenter=true&width=650&lines=Hi%2C+I'm+Rizky+Nanda+Praditia;AI+Engineer+%C2%B7+Automation+Builder;I+design+AI+agents+that+run+on+their+own" alt="Typing SVG" />

**AI Automation Engineer** · Yogyakarta, Indonesia

I build AI agents that handle real work for small businesses in Indonesia —<br/>answering customers, taking orders, and keeping things moving when nobody's around to.

<br/>

<a href="https://www.linkedin.com/in/rizky-nanda-praditia/"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?logo=linkedin&logoColor=white&style=for-the-badge" alt="LinkedIn"/></a>
<a href="https://portfolio-zeta-ruby-65.vercel.app/"><img src="https://img.shields.io/badge/Portfolio-Visit-000000?logo=vercel&logoColor=white&style=for-the-badge" alt="Portfolio"/></a>
<a href="https://huggingface.co/nandutt"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Spaces-FFD21E?style=for-the-badge" alt="Hugging Face"/></a>

<a href="mailto:rizkynandapr@gmail.com">rizkynandapr@gmail.com</a>

<img src="https://komarev.com/ghpvc/?username=rizkynandapr&label=Profile%20Views&color=D97757&style=flat-square" alt="Profile Views"/>

</div>

---

## Who I am

I'm an AI Engineer, and I build automation for a living. These days that's at Aksoro, where I design customer service agents on the Malika (Cekat) platform and hook them into n8n.

Most of my job lives in one specific gap: the demo works, then a real customer types something weird and the whole thing falls apart. That's where AI projects usually die. A prompt that was fine yesterday chokes on an edge case today. An agent picks the wrong tool. A knowledge base answers fast, confident, and completely wrong. My actual work is making sure that doesn't happen once real people are on the other end.

So a normal week is some mix of designing prompts and agent behavior, wiring LLMs into WhatsApp and whatever internal tools a client runs, building n8n flows to shuffle data between APIs, and digging through production logs when something breaks in a way nobody predicted.

I started out in data science, so when a problem actually needs Python or a trained model instead of a prompt, I've got that in my back pocket. But the thing I'm good at now is narrower and clearer: taking a language model and turning it into something that does real work without a human babysitting it.

```yaml
role:        AI Engineer · Automation Builder
building:    LLM agents · RAG with citation guardrails · n8n automations
good at:     making AI hold up with real users, not just in demos
learning:    LLM Zoomcamp 2026, one production bug at a time
```

---

## Tech stack

**AI / LLM Engineering**

![Claude](https://img.shields.io/badge/Claude%20API-D97757?logo=anthropic&logoColor=white)
![Cekat](https://img.shields.io/badge/Cekat%20AI-2D2D2D)
![n8n](https://img.shields.io/badge/n8n-EA4B71?logo=n8n&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?logo=tensorflow&logoColor=white)
![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-FFD21E)

**Languages & Data**

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?logo=mysql&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)

**Web & Infra**

![React](https://img.shields.io/badge/React.js-61DAFB?logo=react&logoColor=black)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3FCF8E?logo=supabase&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?logo=vercel&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)

---

## Featured projects

<img src="https://capsule-render.vercel.app/api?type=waving&color=D97757&height=3&section=header" width="100%"/>

<table>
<tr>
<td width="50%" valign="top">

### [LegalitasAI](https://github.com/rizkynandapr/legalitasai)
`RAG` `FastAPI` `BM25 + RRF` `Claude` `Langfuse`

60 million small businesses here, and the rules that bind them sit in dozens of legal documents nobody wrote for a shop owner to read. Ask a normal LLM and you get a confident answer that's sometimes wrong. In legal territory, wrong means fines.

So I built a RAG that **isn't allowed to answer without proof**. Every claim has to cite the actual Pasal and Ayat, and a validator checks that citation exists in the source before the answer ships. Can't prove it, it refuses.

It also knows which regulations got revoked. Moving that filter into the ranking step took Hit Rate@5 from 63.6% to **81.8%** — revoked docs were outscoring live ones and eating the whole top-5.

**43 tests**, CI with an eval-gate, 7 ADRs.

</td>
<td width="50%" valign="top">

### [WhatsApp AI Chatbot for SMBs](https://github.com/rizkynandapr/n8n-whatsapp-ai-chatbot)
`n8n` `WhatsApp Cloud API` `Claude API` `Sheets`

My cousin makes raincoats. Every rainy season, one person drowns trying to answer a flood of WhatsApp orders by hand. Every SMB here has some version of that, so I built the fix **once** as a reusable template.

It turns a WhatsApp Business number into an agent that answers with conversation memory, spots a complete order and logs it to Sheets, pings the owner right away, and chases up leads that went quiet. Everything client-specific sits in one node, so standing it up for the next business takes **under 30 minutes.**

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [ApplyIQ](https://github.com/rizkynandapr/applyiq-web)
`React 19` `Vite` `n8n` `Supabase` `LLM`

The repetitive parts of job hunting, done for you: match your resume to roles worth applying to, then draft a cover letter for each one.

The resume is parsed **in the browser** (pdf.js, mammoth) so nothing leaves as a raw file. An n8n pipeline scores each listing against your profile, and the results land on a Supabase dashboard with match meters and one-click copy.

</td>
<td width="50%" valign="top">

### [TalentScout](https://github.com/rizkynandapr/TalentScout-AI-Recruitment)
`Workflow Automation` `Prompt Engineering` `LLM`

Screening CVs by hand doesn't scale, and two reviewers rarely agree on who's qualified anyway.

It takes a CV and a job description, runs an LLM gap analysis against the requirements, and scores fit on **fixed weights** (40% hard skills, 30% experience, 20% education, 10% achievements) so every candidate gets judged the same way. Output is an HTML dashboard a hiring manager can actually act on.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [Clickbait Detector](https://github.com/rizkynandapr/clickbait-detector)
`TensorFlow` `LSTM` `Streamlit` `HF Spaces`

An LSTM trained on ~32k balanced English headlines — **~98% accuracy, 0.99 precision** on the clickbait class.

I put it behind a live Streamlit app so people could paste a headline and get an answer instead of trusting the number blind.

→ **[Try the live demo](https://huggingface.co/spaces/nandutt/clickbait_detektor)**

</td>
<td width="50%" valign="top">
</td>
</tr>
</table>

<img src="https://capsule-render.vercel.app/api?type=waving&color=D97757&height=3&section=footer" width="100%"/>

---

## Education & certifications

- **S.Kom, Informatics** — Universitas Muhammadiyah Yogyakarta · 2021–2025
- **Data Science Bootcamp** — Hacktiv8 Indonesia · 2026 *(480+ hrs — Python, SQL, ML)*
- **AI Fluency** — Anthropic Academy

---

<div align="center">

## GitHub in numbers

<img src="https://github-readme-stats-alpha-plum-70.vercel.app/api?username=rizkynandapr&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" alt="GitHub stats" height="165"/>
<img src="https://github-readme-stats-alpha-plum-70.vercel.app/api/top-langs/?username=rizkynandapr&layout=compact&theme=tokyonight&hide_border=true&langs_count=8" alt="Top languages" height="165"/>

<br/>

<img src="https://streak-stats.demolab.com?user=rizkynandapr&theme=tokyonight&hide_border=true&border_radius=8" alt="GitHub streak" height="165"/>

<br/><br/>

*Building AI that does the work, so people don't have to.*

</div>
