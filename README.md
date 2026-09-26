<p align="center">
  <picture><source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg"><img alt="Rizky Nanda Praditia, AI automation engineer. I ship AI agents that survive real customers." src="assets/header-light.svg" width="100%"></picture>
</p>

<p align="center">
  <a href="https://portfolio-rizkynandapr.vercel.app/"><img src="https://img.shields.io/badge/portfolio-open-C4EE2F?style=flat-square&labelColor=0E1218&logo=vercel&logoColor=C4EE2F" alt="Portfolio"/></a>
  <a href="https://dev.to/rizkynandapr"><img src="https://img.shields.io/badge/writing-dev.to-0E1218?style=flat-square&logo=devdotto&logoColor=white" alt="dev.to"/></a>
  <a href="https://www.linkedin.com/in/rizky-nanda-praditia/"><img src="https://img.shields.io/badge/LinkedIn-0E1218?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="https://huggingface.co/nandutt"><img src="https://img.shields.io/badge/Hugging%20Face-0E1218?style=flat-square&logo=huggingface&logoColor=FFD21E" alt="Hugging Face"/></a>
  <a href="mailto:rizkynandapr@gmail.com"><img src="https://img.shields.io/badge/email-say%20hi-0E1218?style=flat-square&logo=gmail&logoColor=white" alt="Email"/></a>
  <img src="https://komarev.com/ghpvc/?username=rizkynandapr&label=profile%20visits&color=8F88FF&style=flat-square" alt="Profile visits"/>
</p>

I build AI agents for small businesses and then try hard to break them before a customer does.

Most of my work sits between "the demo works" and "a real person typed something strange". A caller mentions a gas smell halfway through a normal complaint. A buyer asks for a price three times. Someone claims to be the owner and tells the bot to print its instructions. I write the prompts, the guardrails and the test calls that catch those moments, and I wire the agents into WhatsApp, n8n and whatever tools the business already runs.

From 5 October I'm on the IT Delivery team at [Cekat.AI](https://cekat.ai). Before that I was an AI Trainer at Aksoro, writing and debugging prompts for client bots.

<p align="center">
  <picture><source media="(prefers-color-scheme: dark)" srcset="assets/metrics-dark.svg"><img alt="81.8% Hit Rate@5 on LegalitasAI, under 30 minutes to onboard a business on the WhatsApp template, 98% accuracy on the clickbait LSTM, 43 tests in CI, 13 browser-only tools in Fileloka, 30 scripted test calls in Dispatch Kit." src="assets/metrics-light.svg" width="100%"></picture>
</p>

<br>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/sec-bench-dark.svg"><img alt="01 On the bench" src="assets/sec-bench-light.svg" width="100%"></picture>

**Dispatch Kit** · [rizkynandapr.gumroad.com/l/dispatch-kit](https://rizkynandapr.gumroad.com/l/dispatch-kit)<br>
Prompts, eight guardrails and 30 scripted test calls for AI phone agents that take calls for HVAC, plumbing and roofing companies. A runner scores every call on ten criteria, from "did it catch the emergency" to "did it write exactly one record after the caller hung up". Building it turned up 13 bugs. Most were my own: two instructions that contradicted each other, or a test harness that scored something wrong.

**[n8n-intake-record-guard](https://github.com/rizkynandapr/n8n-intake-record-guard)** · free, MIT<br>
An n8n workflow that sits after the agent and pages a human when an emergency comes in with no address or callback number. It also flags placeholder values like `123 Main St`, numbers in the 555-01xx range that exist only in fiction, and callback numbers that don't match the caller ID.

**[8 of my AI agent's 30 test calls failed. Every one was my fault.](https://dev.to/rizkynandapr/8-of-my-ai-agents-30-test-calls-failed-every-one-was-my-fault-3kff)** · dev.to<br>
The write-up behind both. One reader found two real bugs from the comments alone, and both fixes shipped.

<br>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/sec-shipped-dark.svg"><img alt="02 Shipped" src="assets/sec-shipped-light.svg" width="100%"></picture>

<p>
  <a href="https://github.com/rizkynandapr/legalitasai"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-legalitasai-dark.svg"><img alt="LegalitasAI: legal RAG that won't answer without proof. Hit Rate@5 81.8%." src="assets/card-legalitasai-light.svg" width="49%"></picture></a> <a href="https://fileloka.id"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-fileloka-dark.svg"><img alt="Fileloka: PDF and image tools that never upload your file. 13 tools in the browser." src="assets/card-fileloka-light.svg" width="49%"></picture></a>
</p>

<p>
  <a href="https://github.com/rizkynandapr/n8n-whatsapp-ai-chatbot"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-whatsapp-dark.svg"><img alt="WhatsApp AI Chatbot: n8n template, a new business live in under 30 minutes." src="assets/card-whatsapp-light.svg" width="49%"></picture></a> <a href="https://github.com/rizkynandapr/applyiq-web"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-applyiq-dark.svg"><img alt="ApplyIQ: resume in, ranked jobs and cover letters out." src="assets/card-applyiq-light.svg" width="49%"></picture></a>
</p>

<p>
  <a href="https://github.com/rizkynandapr/TalentScout-AI-Recruitment"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-talentscout-dark.svg"><img alt="TalentScout: CV screening on fixed weights, 40/30/20/10." src="assets/card-talentscout-light.svg" width="49%"></picture></a> <a href="https://huggingface.co/spaces/nandutt/clickbait_detektor"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-clickbait-dark.svg"><img alt="Clickbait Detector: LSTM headline classifier, 98% accuracy." src="assets/card-clickbait-light.svg" width="49%"></picture></a>
</p>

<br>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/sec-stack-dark.svg"><img alt="03 Stack" src="assets/sec-stack-light.svg" width="100%"></picture>

<p>
  <picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack-dark.svg"><img alt="AI and LLM: Claude API, RAG with BM25 and dense retrieval, Langfuse, Cekat AI, TensorFlow, Hugging Face. Automation: n8n, WhatsApp Cloud API, webhooks, Google Sheets. Code and data: Python, SQL, Pandas, FastAPI, Streamlit. Web and infra: React, Vite, Supabase, Qdrant, Docker, Vercel." src="assets/stack-light.svg" width="100%"></picture>
</p>

<br>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/sec-background-dark.svg"><img alt="04 Background" src="assets/sec-background-light.svg" width="100%"></picture>

- IT Delivery, Cekat.AI (from October 2026)
- AI Trainer, Aksoro (June to September 2026)
- S.Kom, Informatics, Universitas Muhammadiyah Yogyakarta (2021–2025)
- Data Science Bootcamp, Hacktiv8 Indonesia (2026, 480+ hours of Python, SQL and ML)
- AI Fluency, Anthropic Academy

<p align="center">
  <picture><source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats-alpha-plum-70.vercel.app/api?username=rizkynandapr&amp;show_icons=true&amp;count_private=true&amp;hide_border=false&amp;bg_color=0E1218&amp;title_color=C4EE2F&amp;icon_color=8F88FF&amp;text_color=C9D1DC&amp;border_color=1F2732&amp;border_radius=16"><img alt="GitHub stats" src="https://github-readme-stats-alpha-plum-70.vercel.app/api?username=rizkynandapr&amp;show_icons=true&amp;count_private=true&amp;hide_border=false&amp;bg_color=FAFBFC&amp;title_color=3A2EF0&amp;icon_color=3A2EF0&amp;text_color=1C2433&amp;border_color=D8DEE6&amp;border_radius=16" height="165"></picture>
  <picture><source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats-alpha-plum-70.vercel.app/api/top-langs/?username=rizkynandapr&amp;layout=compact&amp;langs_count=8&amp;hide_border=false&amp;bg_color=0E1218&amp;title_color=C4EE2F&amp;icon_color=8F88FF&amp;text_color=C9D1DC&amp;border_color=1F2732&amp;border_radius=16"><img alt="Top languages" src="https://github-readme-stats-alpha-plum-70.vercel.app/api/top-langs/?username=rizkynandapr&amp;layout=compact&amp;langs_count=8&amp;hide_border=false&amp;bg_color=FAFBFC&amp;title_color=3A2EF0&amp;icon_color=3A2EF0&amp;text_color=1C2433&amp;border_color=D8DEE6&amp;border_radius=16" height="165"></picture>
</p>

<p align="center"><sub>Building something with AI agents? <a href="mailto:rizkynandapr@gmail.com">rizkynandapr@gmail.com</a> · <a href="https://portfolio-rizkynandapr.vercel.app/">portfolio</a></sub></p>
