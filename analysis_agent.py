"""
Analysis Agent
--------------
Job: take the Research Agent's output and turn it into a structured
SWOT + growth-metric read. Pure reasoning over data already gathered —
no external calls.
"""

from utils.llm_client import ask_llm

SYSTEM_PROMPT = """You are a business analyst. Given structured market research,
produce:
1. A SWOT analysis (Strengths, Weaknesses, Opportunities, Threats) for the
   company described, relative to its competitors.
2. Three key growth metrics worth tracking, with a plausible current estimate
   for each based on the research (label clearly as estimates).
Return clean markdown, no preamble."""


def run(company: str, research_output: str) -> str:
    user_prompt = f"""Company: {company}

Research findings:
{research_output}

Produce the SWOT and growth metrics as instructed."""

    return ask_llm(SYSTEM_PROMPT, user_prompt)
