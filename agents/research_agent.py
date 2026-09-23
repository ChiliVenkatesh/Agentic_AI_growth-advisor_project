"""
Research Agent
--------------
Job: gather raw market + competitor signal for the given company/industry.

If SERPAPI_KEY is set, does a real web search and hands the snippets to the
LLM to structure. Otherwise falls back to a mock dataset so the pipeline is
runnable end-to-end without any paid API besides Anthropic.
"""

import os
import requests
from utils.llm_client import ask_llm

SYSTEM_PROMPT = """You are a market research analyst. Given raw search snippets
about a company, its industry, and its target market, extract and structure:
- 3-5 direct competitors with one line on each
- estimated market size / growth rate if mentioned
- 3-5 relevant recent industry news items
Return clean markdown, no preamble."""


def _serpapi_search(query: str) -> str:
    api_key = os.getenv("SERPAPI_KEY")
    if not api_key:
        return ""
    try:
        resp = requests.get(
            "https://serpapi.com/search",
            params={"q": query, "api_key": api_key, "num": 8},
            timeout=15,
        )
        resp.raise_for_status()
        data = resp.json()
        snippets = [
            r.get("snippet", "") for r in data.get("organic_results", [])
        ]
        return "\n".join(s for s in snippets if s)
    except Exception as e:
        return f"[search failed: {e}]"


def _mock_snippets(company: str, industry: str, market: str) -> str:
    return f"""
{company} operates in the {industry} space, targeting {market}.
Recent reports show double-digit growth in this category over the last year.
Several regional and national players compete for the same customer base,
with differentiation mostly on price, delivery speed, and localization.
Funding activity in this space has picked up in the last two quarters.
"""


def run(company: str, industry: str, market: str) -> str:
    query = f"{company} {industry} {market} competitors market size 2026"
    raw = _serpapi_search(query)
    if not raw:
        raw = _mock_snippets(company, industry, market)

    user_prompt = f"""Company: {company}
Industry: {industry}
Target market: {market}

Raw research snippets:
{raw}

Structure this into the format described in your instructions."""

    return ask_llm(SYSTEM_PROMPT, user_prompt)
