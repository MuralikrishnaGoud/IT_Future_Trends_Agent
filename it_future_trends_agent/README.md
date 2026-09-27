# IT Future Trends Agent

Workshop project using the OpenAI Responses API + built-in web search.

## Two versions
- `agent_chat.py` - terminal interactive agent
- `streamlit_app.py` - Streamlit chat application

## Architecture
User -> LLM/Agent -> Web Search Tool -> Current Information -> LLM Analysis -> Answer -> Follow-up

## Setup
Requires Python 3.10+ and an OpenAI API key with API access/billing.

```bash
python -m venv .venv
pip install -r requirements.txt
```

PowerShell:
```powershell
$env:OPENAI_API_KEY="your_key_here"
```

Windows CMD:
```cmd
set OPENAI_API_KEY=your_key_here
```

macOS/Linux:
```bash
export OPENAI_API_KEY="your_key_here"
```

Never commit your real API key to GitHub.

## Run terminal version
```bash
python agent_chat.py
```

## Run Streamlit version
```bash
streamlit run streamlit_app.py
```

## Good workshop questions
1. What is the current situation of the IT industry in 2026?
2. Which technologies are changing software jobs?
3. How is Agentic AI different from Generative AI?
4. What skills should B.Tech CSE students learn for the next 3-5 years?
5. Create a 90-day roadmap for Data + AI.
6. Suggest a real-world Python + Data + Agentic AI project.

## Teaching point
The model is the reasoning/generation layer. Web search is the tool that gives the
agent access to current public information. The model receives the tool result,
analyzes it, and generates the answer.

Future trends are uncertain, so the system prompt asks the agent to distinguish
current facts from emerging signals and future scenarios.

## Git
`.gitignore` excludes common secret and virtual-environment files.

```bash
git add .
git commit -m "Add IT Future Trends Agent"
git push
```

OpenAI API and web-search usage may incur charges.
