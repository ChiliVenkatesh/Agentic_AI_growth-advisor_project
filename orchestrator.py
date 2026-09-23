"""
Orchestrator
------------
Runs the 4 agents in sequence, each one consuming the previous agent's
output. Yields (stage_name, output) as it goes so the UI can update live.
"""

from agents import research_agent, analysis_agent, strategy_agent, report_agent


def run_pipeline(company: str, industry: str, market: str):
    research = research_agent.run(company, industry, market)
    yield "research", research

    analysis = analysis_agent.run(company, research)
    yield "analysis", analysis

    strategy = strategy_agent.run(company, analysis)
    yield "strategy", strategy

    report = report_agent.run(company, industry, market, research, analysis, strategy)
    yield "report", report
