# app.py - Caribbean Sargassum Information Hub
import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Caribbean Sargassum Information Hub | CWA2026",
    page_icon="🌊",
    layout="wide"
)

# Custom Styling
st.markdown("""
<style>
    .main-header { font-size: 2.3rem; color: #0A192F; font-weight: 800; }
    .sub-header { font-size: 1.1rem; color: #008080; font-weight: 600; margin-bottom: 25px; }
    .card { background-color: #F8FAFC; border-left: 5px solid #008080; padding: 18px; border-radius: 6px; margin-bottom: 15px; }
    .stButton>button { background-color: #008080; color: white; font-weight: bold; border-radius: 6px; width: 100%; }
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<div class="main-header">🌊 Caribbean Sargassum Information Hub</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Official CWA2026 Resource | Regional Influx Dynamics, Functional Interventions & The Blue-Gold Framework</div>', unsafe_allow_html=True)

# Navigation Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Influx & Economic Data", 
    "🛠️ Deployed Regional Solutions", 
    "⚡ The Blue-Gold Framework", 
    "📝 Commercialization Audit Tool"
])

# TAB 1: Macro Influx Data
with tab1:
    st.header("The Caribbean Sargassum Crisis")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Atlantic Biomass Peak", "20–38M Metric Tonnes")
    col2.metric("Annual Regional Losses", "$300M USD+")
    col3.metric("Annual Beach Cleanup Cost", "$120M USD+")
    col4.metric("Regional Economic Drag", "$2B–$3B USD")

    st.markdown("---")
    st.subheader("Key Influx Dynamics & Environmental Impact")
    st.write("""
    * **Record Inundations:** Satellite tracking recorded up to **9 million metric tonnes** landing in the Dominican Republic and Puerto Rico in early 2026 alone.
    * **Severe Ecosystem & Tourism Damage:** Decaying sargassum releases noxious hydrogen sulfide ($H_2S$), depletes oxygen levels causing massive fish kills, smothers coral reefs, and deters tourists.
    * **Food System Vulnerability:** Compounds CARICOM's **$4.25 Billion** annual food import bill (60–80% food dependency).
    """)

# TAB 2: Deployed Solutions Analysis
with tab2:
    st.header("Comparative Analysis: Currently Deployed Regional Interventions")
    
    df_solutions = pd.DataFrame({
        "Intervention Type": ["Manual Beach Removal", "Nearshore Pump Harvesters", "Lab-Scale Bio-Extraction", "SynergySphereCASA Blue-Gold Framework"],
        "Deployment Location": ["Shoreline beaches", "Calm bays / Nearshore", "Academic Laboratories", "100–200 Miles Offshore + La Brea Refinery"],
        "Capacity & Scale": ["Low (~150 workers/day)", "Localized bay protection", "Grams to kilograms", "300+ t/day vessel; 10,000 t/yr plant"],
        "Biomass Quality": ["Degraded & sand-contaminated", "Partially decomposed", "Variable lab samples", "Pristine, fresh, high bioactive yield"],
        "Coastal Impact": ["Causes severe beach erosion", "Low nearshore impact", "N/A", "Protects reefs/beaches; faunal filtering"],
        "Economic Viability": ["Pure cost center ($120M/yr)", "Localized intervention", "Lacks commercial scale", "Circular revenue ($50M model, IRR >20%)"]
    })
    st.dataframe(df_solutions, use_container_width=True)

# TAB 3: Blue-Gold Framework
with tab3:
    st.header("Why SynergySphereCASA is the Most Viable Regional Framework")
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("""
        <div class="card">
        <h3>🚢 1. Offshore Interception & Industrial Refining</h3>
        <ul>
            <li><b>Offshore Vessels:</b> <i>Ocean Guardian</i> RORO platform harvesting <b>300+ tonnes/day</b> 100–200 miles at sea before beach landing.</li>
            <li><b>Faunal Safeguards:</b> Floating booms with protective mesh filtering arrays to protect turtles and pelagic fish.</li>
            <li><b>Flagship Bio-Refinery:</b> 15-acre dockside site at <b>LABIDCO, La Brea, Trinidad</b> processing <b>10,000 wet tonnes/yr</b> into liquid biostimulants, fertilizers, and 16% yield alginates.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_b:
        st.markdown("""
        <div class="card">
        <h3>🌾 2. Food Security & UK Engineering Validation</h3>
        <ul>
            <li><b>Fertilizer Replacement:</b> Replaces up to <b>50% of imported fertilizers</b>, supporting CARICOM's <b>25 by 2025 (+5)</b> mandate.</li>
            <li><b>Proven Agronomy:</b> <b>UWI field trials</b> demonstrate <b>>80% vegetable yield increases</b>.</li>
            <li><b>Heavy Metal Safety:</b> Strict CRFM/CARIRI ICP-MS testing protocols. Intec trials confirm heavy metals in harvested fruit remain <b>below quantification limits</b>.</li>
            <li><b>UK R&D Backing:</b> Engineered with <b>SolarisLabs</b> (Oxford Science Park, Cambridge & Stirling research, <b>40+ filed patents</b>, ISO 22000).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# TAB 4: Readiness Audit Tool
with tab4:
    st.header("National Sargassum Commercialization Readiness Audit (SCRA-Q)")
    st.write("Attending CARICOM Delegations can complete this audit to request a 60-day National Feasibility Study.")
    
    with st.form("audit_form"):
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            country = st.text_input("Member State / Territory")
            ministry = st.text_input("Lead Ministry")
            contact_name = st.text_input("Minister / Head of Delegation Name")
        with col_f2:
            email = st.text_input("Official Government Email")
            tonnage = st.selectbox("Estimated Annual Beach Inundation (Metric Tonnes)", ["< 10,000", "10,000 – 50,000", "50,000 – 100,000", "> 100,000"])
            spend = st.text_input("Annual Public Cleanup Expenditure (USD)")
            
        submitted = st.form_submit_button("Submit Readiness Audit Request")
        if submitted:
            st.success(f"Audit request successfully logged for {country}. The SynergySphereCASA Technical Directorate will contact {contact_name} within 24 hours to issue your 60-day Feasibility Roadmap.")
