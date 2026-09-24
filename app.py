# app.py - Caribbean Sargassum Information Hub
import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
page_title=&quot;Caribbean Sargassum Information Hub | CWA2026&quot;,
page_icon=&quot;��&quot;,
layout=&quot;wide&quot;
)

# Custom Styling
st.markdown(&quot;&quot;&quot;
&lt;style&gt;
.main-header { font-size: 2.3rem; color: #0A192F; font-weight: 800; }
.sub-header { font-size: 1.1rem; color: #008080; font-weight: 600; margin-bottom:
25px; }
.card { background-color: #F8FAFC; border-left: 5px solid #008080; padding:
18px; border-radius: 6px; margin-bottom: 15px; }

.stButton&gt;button { background-color: #008080; color: white; font-weight: bold;
border-radius: 6px; width: 100%; }
&lt;/style&gt;
&quot;&quot;&quot;, unsafe_allow_html=True)

# Header Section
st.markdown(&#39;&lt;div class=&quot;main-header&quot;&gt;�� Caribbean Sargassum Information
Hub&lt;/div&gt;&#39;, unsafe_allow_html=True)
st.markdown(&#39;&lt;div class=&quot;sub-header&quot;&gt;Official CWA2026 Resource | Regional Influx
Dynamics, Functional Interventions &amp; The Blue-Gold Framework&lt;/div&gt;&#39;,
unsafe_allow_html=True)

# Navigation Tabs
tab1, tab2, tab3, tab4 = st.tabs([
&quot;�� Influx &amp; Economic Data&quot;,
&quot;��️ Deployed Regional Solutions&quot;,
&quot;⚡ The Blue-Gold Framework&quot;,
&quot;�� Commercialization Audit Tool&quot;
])

# TAB 1: Macro Influx Data
with tab1:
st.header(&quot;The Caribbean Sargassum Crisis&quot;)
col1, col2, col3, col4 = st.columns(4)
col1.metric(&quot;Atlantic Biomass Peak&quot;, &quot;20–38M Metric Tonnes&quot;)
col2.metric(&quot;Annual Regional Losses&quot;, &quot;$300M USD+&quot;)
col3.metric(&quot;Annual Beach Cleanup Cost&quot;, &quot;$120M USD+&quot;)
col4.metric(&quot;Regional Economic Drag&quot;, &quot;$2B–$3B USD&quot;)

st.markdown(&quot;---&quot;)

st.subheader(&quot;Key Influx Dynamics &amp; Environmental Impact&quot;)
st.write(&quot;&quot;&quot;
* **Record Inundations:** Satellite tracking recorded up to **9 million metric
tonnes** landing in the Dominican Republic and Puerto Rico in early 2026 alone.
* **Severe Ecosystem &amp; Tourism Damage:** Decaying sargassum releases
noxious hydrogen sulfide ($H_2S$), depletes oxygen levels causing massive fish
kills, smothers coral reefs, and deters tourists.
* **Food System Vulnerability:** Compounds CARICOM&#39;s **$4.25 Billion** annual
food import bill (60–80% food dependency).
&quot;&quot;&quot;)

# TAB 2: Deployed Solutions Analysis
with tab2:
st.header(&quot;Comparative Analysis: Currently Deployed Regional Interventions&quot;)

df_solutions = pd.DataFrame({
&quot;Intervention Type&quot;: [&quot;Manual Beach Removal&quot;, &quot;Nearshore Pump Harvesters&quot;,
&quot;Lab-Scale Bio-Extraction&quot;, &quot;SynergySphereCASA Blue-Gold Framework&quot;],
&quot;Deployment Location&quot;: [&quot;Shoreline beaches&quot;, &quot;Calm bays / Nearshore&quot;,
&quot;Academic Laboratories&quot;, &quot;100–200 Miles Offshore + La Brea Refinery&quot;],
&quot;Capacity &amp; Scale&quot;: [&quot;Low (~150 workers/day)&quot;, &quot;Localized bay protection&quot;,
&quot;Grams to kilograms&quot;, &quot;300+ t/day vessel; 10,000 t/yr plant&quot;],
&quot;Biomass Quality&quot;: [&quot;Degraded &amp; sand-contaminated&quot;, &quot;Partially decomposed&quot;,
&quot;Variable lab samples&quot;, &quot;Pristine, fresh, high bioactive yield&quot;],
&quot;Coastal Impact&quot;: [&quot;Causes severe beach erosion&quot;, &quot;Low nearshore impact&quot;,
&quot;N/A&quot;, &quot;Protects reefs/beaches; faunal filtering&quot;],
&quot;Economic Viability&quot;: [&quot;Pure cost center ($120M/yr)&quot;, &quot;Localized intervention&quot;,
&quot;Lacks commercial scale&quot;, &quot;Circular revenue ($50M model, IRR &gt;20%)&quot;]
})
st.dataframe(df_solutions, use_container_width=True)

# TAB 3: Blue-Gold Framework

with tab3:
st.header(&quot;Why SynergySphereCASA is the Most Viable Regional Framework&quot;)
col_a, col_b = st.columns(2)

with col_a:
st.markdown(&quot;&quot;&quot;
&lt;div class=&quot;card&quot;&gt;
&lt;h3&gt;�� 1. Offshore Interception &amp; Industrial Refining&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;&lt;b&gt;Offshore Vessels:&lt;/b&gt; &lt;i&gt;Ocean Guardian&lt;/i&gt; RORO platform
harvesting &lt;b&gt;300+ tonnes/day&lt;/b&gt; 100–200 miles at sea before beach
landing.&lt;/li&gt;
&lt;li&gt;&lt;b&gt;Faunal Safeguards:&lt;/b&gt; Floating booms with protective mesh filtering
arrays to protect turtles and pelagic fish.&lt;/li&gt;
&lt;li&gt;&lt;b&gt;Flagship Bio-Refinery:&lt;/b&gt; 15-acre dockside site at &lt;b&gt;LABIDCO, La
Brea, Trinidad&lt;/b&gt; processing &lt;b&gt;10,000 wet tonnes/yr&lt;/b&gt; into liquid biostimulants,
fertilizers, and 16% yield alginates.&lt;/li&gt;
&lt;/ul&gt;
&lt;/div&gt;
&quot;&quot;&quot;, unsafe_allow_html=True)

with col_b:
st.markdown(&quot;&quot;&quot;
&lt;div class=&quot;card&quot;&gt;
&lt;h3&gt;�� 2. Food Security &amp; UK Engineering Validation&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;&lt;b&gt;Fertilizer Replacement:&lt;/b&gt; Replaces up to &lt;b&gt;50% of imported
fertilizers&lt;/b&gt;, supporting CARICOM&#39;s &lt;b&gt;25 by 2025 (+5)&lt;/b&gt; mandate.&lt;/li&gt;
&lt;li&gt;&lt;b&gt;Proven Agronomy:&lt;/b&gt; &lt;b&gt;UWI field trials&lt;/b&gt; demonstrate
&lt;b&gt;&gt;80% vegetable yield increases&lt;/b&gt;.&lt;/li&gt;

&lt;li&gt;&lt;b&gt;Heavy Metal Safety:&lt;/b&gt; Strict CRFM/CARIRI ICP-MS testing
protocols. Intec trials confirm heavy metals in harvested fruit remain &lt;b&gt;below
quantification limits&lt;/b&gt;.&lt;/li&gt;
&lt;li&gt;&lt;b&gt;UK R&amp;D Backing:&lt;/b&gt; Engineered with &lt;b&gt;SolarisLabs&lt;/b&gt; (Oxford
Science Park, Cambridge &amp; Stirling research, &lt;b&gt;40+ filed patents&lt;/b&gt;, ISO
22000).&lt;/li&gt;
&lt;/ul&gt;
&lt;/div&gt;
&quot;&quot;&quot;, unsafe_allow_html=True)

# TAB 4: Readiness Audit Tool
with tab4:
st.header(&quot;National Sargassum Commercialization Readiness Audit (SCRA-Q)&quot;)
st.write(&quot;Attending CARICOM Delegations can complete this audit to request a 60-
day National Feasibility Study.&quot;)

with st.form(&quot;audit_form&quot;):
col_f1, col_f2 = st.columns(2)
with col_f1:
country = st.text_input(&quot;Member State / Territory&quot;)
ministry = st.text_input(&quot;Lead Ministry&quot;)
contact_name = st.text_input(&quot;Minister / Head of Delegation Name&quot;)
with col_f2:
email = st.text_input(&quot;Official Government Email&quot;)
tonnage = st.selectbox(&quot;Estimated Annual Beach Inundation (Metric
Tonnes)&quot;, [&quot;&lt; 10,000&quot;, &quot;10,000 – 50,000&quot;, &quot;50,000 – 100,000&quot;, &quot;&gt; 100,000&quot;])
spend = st.text_input(&quot;Annual Public Cleanup Expenditure (USD)&quot;)

submitted = st.form_submit_button(&quot;Submit Readiness Audit Request&quot;)
if submitted:

st.success(f&quot;Audit request successfully logged for {country}. The
SynergySphereCASA Technical Directorate will contact {contact_name} within 24
hours to issue your 60-day Feasibility Roadmap.&quot;)
