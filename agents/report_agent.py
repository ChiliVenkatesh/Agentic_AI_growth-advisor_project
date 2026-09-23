"""
Report Agent
------------
Job: combine every other agent's output into one clean final brief.
This is the orchestrator's last step, not a separate LLM call by default —
kept as a template-fill function so the pipeline stays fast and cheap.
If you want the model to also polish tone, swap the return line for
an ask_llm() call.
"""


def run(company: str, industry: str, market: str,
        research: str, analysis: str, strategy: str) -> str:
    return f"""# Growth & Strategy Brief — {company}

**Industry:** {industry}  **Target market:** {market}

---

## Market Research
{research}

---

## Analysis
{analysis}

---

## Recommendations
{strategy}
"""
