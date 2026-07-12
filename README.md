<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=26&pause=1200&color=D97757&center=true&vCenter=true&width=650&lines=Hi%2C+I'm+Rizky+Nanda+Praditia;AI+Engineer+%C2%B7+Automation+Builder;I+design+AI+agents+that+run+on+their+own" alt="Typing SVG" />

**AI Automation Engineer** · Yogyakarta, Indonesia 🇮🇩

I design and ship AI agents that handle real work — answering customers, taking orders,<br/>and running the busywork on their own — for small businesses across Indonesia.

<br/>

<a href="https://www.linkedin.com/in/rizky-nanda-praditia/"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?logo=linkedin&logoColor=white&style=for-the-badge" alt="LinkedIn"/></a>
<a href="https://portfolio-zeta-ruby-65.vercel.app/"><img src="https://img.shields.io/badge/Portfolio-Visit-000000?logo=vercel&logoColor=white&style=for-the-badge" alt="Portfolio"/></a>
<a href="https://huggingface.co/nandutt"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Spaces-FFD21E?style=for-the-badge" alt="Hugging Face"/></a>

<a href="mailto:rizkynandapr@gmail.com">📧 rizkynandapr@gmail.com</a>

<img src="https://komarev.com/ghpvc/?username=rizkynandapr&label=Profile%20Views&color=D97757&style=flat-square" alt="Profile Views"/>

</div>

<img src="https://raw.githubusercontent.com/Platane/snk/output/github-contribution-grid-snake-dark.svg" alt="snake animation" width="100%"/>

---

##  Who I am

I'm an **AI Engineer** who builds automation for a living. Right now I'm an AI Trainer at **Aksoro**, designing customer service agents on the Malika (Cekat) platform and wiring them into n8n pipelines.

My work sits in the gap between *"the AI demo looks amazing"* and *"the AI actually holds up when real customers type into it."* That gap is where most AI projects quietly fail — a prompt that worked yesterday breaks on an edge case today, an agent routes to the wrong tool, a knowledge base answers confidently and wrongly. Closing that gap is the job I actually do.

So a normal week for me looks like: designing system prompts and agent behavior, connecting LLMs to WhatsApp and clients' internal tools, building n8n workflows that move data between APIs, and debugging the messy production failures that decide whether a bot is a toy or a tool.

I came into this from **data science** — so when a problem needs Python, pandas, or a trained model instead of a prompt, I reach for that too. But my craft today is clear: **turning language models into systems that do reliable work without someone watching them.**

```yaml
role:        AI Engineer · Automation Builder
building:    LLM agents · RAG systems · n8n automations
comfort:     making AI survive real users, not just demos
learning:    LLM Zoomcamp 2026 — one production bug at a time
```

---

##  Tech stack

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
![Supabase](https://img.shields.io/badge/Supabase-3FCF8E?logo=supabase&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?logo=vercel&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)

---

##  Featured projects

<img src="https://capsule-render.vercel.app/api?type=waving&color=D97757&height=3&section=header" width="100%"/>

<table>
<tr>
<td width="50%" valign="top">

###  [WhatsApp AI Chatbot for SMBs](https://github.com/rizkynandapr/n8n-whatsapp-ai-chatbot)
`n8n` `WhatsApp Cloud API` `Claude API` `Sheets`

My cousin makes raincoats. Every rainy season, one person drowns trying to answer a flood of WhatsApp orders by hand. Every SMB here has some version of that — so I engineered the fix **once**, as a reusable template.

It turns a WhatsApp Business number into an agent that answers with conversation memory, detects a complete order and logs it to Sheets, pings the owner instantly, and follows up on leads that went quiet. All client-specific config lives in one node → **a new business goes live in under 30 minutes.**

</td>
<td width="50%" valign="top">

###  [ApplyIQ](https://github.com/rizkynandapr/applyiq-web)
`React 19` `Vite` `n8n` `Supabase` `LLM`

The repetitive parts of job hunting, automated: match a resume to roles worth applying to, then draft a tailored cover letter for each.

The resume is parsed **in the browser** (pdf.js, mammoth) so nothing leaves as a raw file. An n8n pipeline scores each listing against the profile, and results land on a Supabase dashboard with match meters and one-click copy.

</td>
</tr>
<tr>
<td width="50%" valign="top">

###  [TalentScout](https://github.com/rizkynandapr/TalentScout-AI-Recruitment)
`Workflow Automation` `Prompt Engineering` `LLM`

Screening CVs by hand doesn't scale, and two reviewers rarely agree on who's qualified anyway.

It takes a CV + job description, runs an LLM gap analysis against the requirements, and scores fit on **fixed weights** (40% hard skills, 30% experience, 20% education, 10% achievements) so every candidate is judged the same way. Output is an HTML dashboard a hiring manager can act on.

</td>
<td width="50%" valign="top">

###  [Clickbait Detector](https://github.com/rizkynandapr/clickbait-detector)
`TensorFlow` `LSTM` `Streamlit` `HF Spaces`

An LSTM trained on ~32k balanced English headlines — **~98% accuracy, 0.99 precision** on the clickbait class.

I put it behind a live Streamlit app so people could paste a headline and get an answer instead of trusting the number blind.

→ **[Try the live demo](https://huggingface.co/spaces/nandutt/clickbait_detektor)**

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

<br/><br/>

*Building AI that does the work — so people don't have to.*

</div>
