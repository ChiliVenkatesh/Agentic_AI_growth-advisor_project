# 🌱 AI Business Growth & Market Strategy Advisor

A multi-agent AI system that generates a full market strategy brief for a company — research, SWOT analysis, ranked growth recommendations, and a final report — powered by Google Gemini and served through a Streamlit UI.

## Overview

Given a **company/product**, **industry**, and **target market**, the pipeline runs four agents in sequence, each consuming the previous agent's output:

```
Research Agent → Analysis Agent → Strategy Agent → Report Agent
```

| Agent | Role |
|---|---|
| **Research Agent** | Gathers competitor and market signal (live via SerpAPI if configured, otherwise a mock dataset) and structures it into competitors, market size/growth, and recent news |
| **Analysis Agent** | Turns the research into a SWOT analysis plus 3 key growth metrics with estimates |
| **Strategy Agent** | Produces 3 ranked, actionable growth recommendations tied to the analysis |
| **Report Agent** | Assembles everything into one final markdown brief |

The Streamlit app shows live status cards for each agent as the pipeline runs, then displays the result in tabs (Summary / Market data / Recommendations) with a markdown download button.

## Tech Stack

- **UI:** Streamlit
- **LLM:** Google Gemini (`google-genai`)
- **Search:** SerpAPI (optional)
- **Data handling:** pandas, BeautifulSoup4

## Project Structure

```
.
├── app.py                 # Streamlit UI
├── orchestrator.py        # Runs the 4 agents in sequence
├── research_agent.py
├── analysis_agent.py
├── strategy_agent.py
├── report_agent.py
├── llm_client.py          # Gemini API wrapper
├── requirements.txt
└── __init__.py
```

> **Note:** `orchestrator.py` and the agent files currently reference `agents.<agent>` and `utils.llm_client` as import paths. Either move the agent files into an `agents/` package and `llm_client.py` into a `utils/` package, or update the imports to match your actual flat layout, before running.

## Setup

1. **Clone the repo**
   ```bash
   git clone <your-repo-url>
   cd <repo-folder>
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**

   Create a `.env` file in the project root:
   ```env
   GEMINI_API_KEY=your_gemini_api_key
   GEMINI_MODEL=gemini-3.1-flash-lite   # optional, this is the default
   SERPAPI_KEY=your_serpapi_key         # optional — enables live web search
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

## Usage

1. Enter a **company/product**, **industry**, and **target market**.
2. Click **Run analysis**.
3. Watch each agent card update as the pipeline progresses.
4. Review the generated brief across the Summary, Market data, and Recommendations tabs.
5. Download the final report as a `.md` file.

## Notes

- If `SERPAPI_KEY` is not set, the Research Agent falls back to a mock dataset so the full pipeline still runs end-to-end.
- The Report Agent is template-based by default (no extra LLM call) to keep the pipeline fast and cheap — swap it for an `ask_llm()` call if you want the model to polish the final tone.

## License

MIT (or update as needed).
