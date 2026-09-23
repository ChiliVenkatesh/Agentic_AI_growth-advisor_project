"""
Strategy Agent
--------------
Job: turn the Analysis Agent's SWOT + metrics into ranked, actionable
growth recommendations. This is the "advisor" voice of the system.
"""

from utils.llm_client import ask_llm

SYSTEM_PROMPT = """You are a senior growth strategist advising a founder.
Given a SWOT analysis and growth metrics, produce exactly 3 ranked
recommendations. For each:
- a short, specific action title (imperative voice)
- 1-2 sentences on why this ranks where it does, tied to the analysis
Order by expected impact, highest first. Return clean markdown, no preamble."""


def run(company: str, analysis_output: str) -> str:
    user_prompt = f"""Company: {company}

Analysis:
{analysis_output}

Produce exactly 3 ranked recommendations as instructed."""

    return ask_llm(SYSTEM_PROMPT, user_prompt)
