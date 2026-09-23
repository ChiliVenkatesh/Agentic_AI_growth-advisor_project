import streamlit as st
from dotenv import load_dotenv
from orchestrator import run_pipeline

load_dotenv()

st.set_page_config(page_title="Growth & Strategy Advisor", layout="wide")

st.markdown(
    """
    <style>
    .stApp { background-color: #0E1712; color: #EAF0EA; }
    .agent-card {
        background:#142019; border:1px solid #26362C; border-radius:10px;
        padding:16px; margin-bottom:8px;
    }
    .agent-card h4 { margin:0 0 4px 0; color:#EAF0EA; }
    .agent-card p { margin:0; color:#9FB0A4; font-size:13px; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🌱 AI Business Growth & Market Strategy Advisor")
st.caption("Multi-agent market intelligence — Research → Analysis → Strategy → Report")

col1, col2, col3 = st.columns(3)
with col1:
    company = st.text_input("Company or product", "Nimbus Fresh — grocery delivery app")
with col2:
    industry = st.text_input("Industry", "Consumer / retail tech")
with col3:
    market = st.text_input("Target market", "Tier-2 India cities")

run = st.button("Run analysis", type="primary")

AGENT_META = {
    "research": ("Market Research", "Pulling competitor + market data."),
    "analysis": ("Analysis", "Building SWOT and growth metrics."),
    "strategy": ("Strategy", "Ranking growth recommendations."),
    "report": ("Report", "Assembling the final brief."),
}

if run:
    status_area = st.columns(4)
    placeholders = {}
    for i, key in enumerate(AGENT_META):
        title, desc = AGENT_META[key]
        with status_area[i]:
            placeholders[key] = st.empty()
            placeholders[key].markdown(
                f"""<div class="agent-card"><h4>⏳ {title}</h4><p>{desc}</p></div>""",
                unsafe_allow_html=True,
            )

    results = {}
    try:
        for stage, output in run_pipeline(company, industry, market):
            results[stage] = output
            title, desc = AGENT_META[stage]
            placeholders[stage].markdown(
                f"""<div class="agent-card"><h4>✅ {title}</h4><p>{desc}</p></div>""",
                unsafe_allow_html=True,
            )
    except RuntimeError as e:
        st.error(str(e))
        st.stop()

    st.divider()
    st.subheader("Strategy Brief")

    tabs = st.tabs(["Summary", "Market data", "Recommendations"])
    with tabs[0]:
        st.markdown(results.get("report", ""))
    with tabs[1]:
        st.markdown(results.get("research", ""))
        st.markdown(results.get("analysis", ""))
    with tabs[2]:
        st.markdown(results.get("strategy", ""))

    st.download_button(
        "Download brief (.md)",
        data=results.get("report", ""),
        file_name=f"{company.replace(' ', '_')}_growth_brief.md",
        mime="text/markdown",
    )
else:
    st.info("Fill in the fields above and click **Run analysis** to start the pipeline.")
