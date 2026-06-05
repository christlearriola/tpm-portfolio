import streamlit as st
import pandas as pd

# 1. Page Configuration & Executive Theme Setup
st.set_page_config(page_title="Christle Arriola | TPM Portfolio Sandbox", layout="wide")

st.title("🚀 Technical Program Management: Governance & Automation Sandbox")
st.caption("Interact with the parameters below to simulate how my framework scales to de-risk complex enterprise portfolios.")

# 2. Sidebar Controls (The Executive Parameters)
st.sidebar.header("🎛️ Operational Parameters")

portfolio_scale = st.sidebar.select_slider(
    "Portfolio Budget / Scale",
    options=["$100M - $500M", "$1B - $10B", "$10B+"]
)

team_structure = st.sidebar.selectbox(
    "Team Topology",
    options=["Core PMO (<15)", "Cross-Functional Cohorts", "Matrixed (100+ Engineering Teams)"]
)

primary_risk = st.sidebar.selectbox(
    "Primary Systemic Risk",
    options=["Technical Debt & Legacy Re-work", "Operational / Disruption Flow", "Regulatory & Material Compliance"]
)

# 3. Dynamic Strategy Logic Engine
# This handles the data mapping based on the variables selected above
if portfolio_scale == "$10B+":
    playbook = "Enterprise Core M&A Integration Playbook"
    control_mechanism = "Centralized Event Command Center (24/7 Cutover Cadence)"
    metrics_arch = "Real-time automated milestone telemetry via Executive Steering Dashboards"
    speed_metric = "35% reduction in post-close tool migration latency"
elif portfolio_scale == "$1B - $10B":
    playbook = "SaaS Environment & Internal Tooling Migration Framework"
    control_mechanism = "Automated Segregation of Duties (SoD) Gates & Risk Logs"
    metrics_arch = "Jira / Smartsheet cross-functional portfolio roadmaps"
    speed_metric = "15% optimization in downstream requirement rework velocity"
else:
    playbook = "Continuous Improvement & Agile Delivery Standup Protocol"
    control_mechanism = "Target-State Data Mapping Quality Validation Sprints"
    metrics_arch = "Bi-weekly sprint burn-down telemetry"
    speed_metric = "Standardization of system release pipelines"

# 4. Laying out the Main Dashboard Dashboard UI
st.header("📋 Matched Strategic Governance Playbook")
st.subheader(f"✨ {playbook}")

# Executive Callout KPIs
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Target Execution Control", value=control_mechanism)
with col2:
    st.metric(label="Validated Performance Impact", value=speed_metric)

st.markdown("---")

# 5. Core Case Study Injections based on parameters
st.header("📖 Architectural Execution Blueprint")
if primary_risk == "Regulatory & Material Compliance":
    st.info("💡 **Active Control Strategy:** Designed and enforced rigorous ICFR risk logs, automated segregation of duties (SoD) controls, and target-state data mapping for financial or telecom assets. This secure mapping layer ensures absolute compliance visibility for external audits and post-merger integration tracking.")
elif primary_risk == "Operational / Disruption Flow":
    st.warning("⚠️ **Active Control Strategy:** Established an operational stopgap control center. This framework isolates manual-to-automation workflow transitions (such as deploying autonomous diagnostic agents and predictive support models) to protect continuous consumer buyflow paths during critical cutover windows.")
else:
    st.success("✅ **Active Control Strategy:** Reconstructed fragmented Master Business Requirements Documents (BRDs). Extracted underlying system dependencies and mapped them directly to Salesforce and backend cloud architectures, cutting down ongoing tech debt.")
