import io
import re
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pypdf import PdfReader
from sqlalchemy import create_engine, text

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# ==========================================
# 1. Page Config & Modern IoT Layout CSS
# ==========================================
st.set_page_config(
    page_title="Modern IoT Dashboard PySide6",
    page_icon="🔮",
    layout="wide"
)

st.markdown("""
    <style>
    /* Main Dark Theme Background */
    .stApp {
        background-color: #121225;
        color: #E2E8F0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Left Control Navigation Panel */
    .nav-panel {
        background-color: #1A1A32;
        border-radius: 16px;
        padding: 20px 15px;
        border: 1px solid #282846;
        height: 100%;
    }
    .nav-title {
        color: #FFFFFF;
        font-weight: 700;
        font-size: 16px;
        margin-bottom: 25px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .nav-item {
        color: #94A3B8;
        padding: 10px 12px;
        border-radius: 10px;
        font-size: 14px;
        font-weight: 500;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        gap: 10px;
        cursor: pointer;
    }
    .nav-item.active {
        background-color: #282846;
        color: #FFFFFF;
        font-weight: 600;
    }

    /* Top Row Label Cards */
    .kpi-card {
        background: #1A1A32;
        border-radius: 14px;
        padding: 16px 20px;
        border: 1px solid #282846;
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 15px;
    }
    .kpi-title { font-size: 13px; color: #94A3B8; font-weight: 600; }
    .kpi-val { font-size: 20px; color: #FFFFFF; font-weight: 700; margin-top: 4px; }
    
    .badge-purple { background: #7C3AED; color: white; padding: 6px 14px; border-radius: 8px; font-weight: bold; font-size: 12px; border:none; }
    .badge-green { background: #10B981; color: white; padding: 6px 14px; border-radius: 8px; font-weight: bold; font-size: 12px; border:none; }
    .badge-orange { background: #F59E0B; color: white; padding: 6px 14px; border-radius: 8px; font-weight: bold; font-size: 12px; border:none; }

    /* Custom Form & Cards */
    div[data-testid="stForm"], .card-panel {
        background-color: #1A1A32 !important;
        border-radius: 16px !important;
        border: 1px solid #282846 !important;
        padding: 20px !important;
    }

    .stButton>button, div[data-testid="stForm"] button {
        background: linear-gradient(90deg, #7C3AED 0%, #6366F1 100%) !important;
        color: white !important;
        font-weight: 700 !important;
        border-radius: 10px !important;
        border: none !important;
        padding: 8px 20px !important;
    }

    .stTextInput input, .stSelectbox div[data-baseweb="select"] {
        background-color: #121225 !important;
        border: 1px solid #282846 !important;
        border-radius: 10px !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. XAMPP MySQL Connection & Helper Actions
# ==========================================
MYSQL_URL = "mysql+pymysql://root:@localhost:3306/benchpulse_db"

@st.cache_resource
def get_db_engine():
    return create_engine(MYSQL_URL)

def fetch_devs():
    try:
        engine = get_db_engine()
        df = pd.read_sql("SELECT * FROM developers;", con=engine)
        df['on_bench'] = df['on_bench'].astype(bool)
        df['skills_list'] = df['skills'].apply(lambda x: [s.strip() for s in str(x).split(',')])
        return df, None
    except Exception as e:
        return pd.DataFrame(), str(e)

def assign_developer(dev_id):
    try:
        engine = get_db_engine()
        with engine.connect() as conn:
            conn.execute(
                text("UPDATE developers SET on_bench = FALSE WHERE id = :id;"),
                {"id": dev_id}
            )
            conn.commit()
        return True
    except Exception as e:
        return False

df_devs, db_err = fetch_devs()

# ==========================================
# 3. Advanced Full Project Proposal PDF Generator
# ==========================================
def generate_detailed_proposal_pdf(project_name, team_df, req_skills):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
    styles = getSampleStyleSheet()
    story = []

    # Custom PDF Styles
    title_style = ParagraphStyle('DocTitle', parent=styles['Title'], fontName='Helvetica-Bold', fontSize=22, textColor=colors.HexColor('#7C3AED'), leading=26)
    heading_style = ParagraphStyle('SectionHeading', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=14, textColor=colors.HexColor('#1A1A32'), spaceBefore=12, spaceAfter=6)
    body_style = ParagraphStyle('BodyTextCustom', parent=styles['Normal'], fontName='Helvetica', fontSize=10, textColor=colors.HexColor('#334155'), leading=14)
    highlight_style = ParagraphStyle('HighlightText', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=10, textColor=colors.HexColor('#10B981'), leading=14)

    # 1. Header Section
    story.append(Paragraph(f"<b>Comprehensive Project & Resource Proposal</b>", title_style))
    story.append(Spacer(1, 6))
    story.append(Paragraph(f"<b>Project Name:</b> {project_name} | <b>Required Tech Stack:</b> {', '.join(req_skills)}", body_style))
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#7C3AED'), spaceAfter=15))

    # Identify Lead Developer (Highest Match Percentage)
    sorted_df = team_df.copy()
    sorted_df['numeric_score'] = sorted_df['match'].str.rstrip('%').astype(float)
    sorted_df = sorted_df.sort_values(by='numeric_score', ascending=False)
    lead_dev = sorted_df.iloc[0]

    # 2. Executive Summary & Recommended Lead Developer
    story.append(Paragraph("1. Executive Summary & Recommended Lead Developer", heading_style))
    summary_text = f"""
    Based on the technical requirements for <b>{project_name}</b>, our automated matching engine has identified 
    <b>{lead_dev['name']} ({lead_dev['id']})</b> as the primary Lead Developer for this project with a top skill match score of 
    <font color="#10B981"><b>{lead_dev['match']}</b></font>.
    """
    story.append(Paragraph(summary_text, body_style))
    story.append(Spacer(1, 10))

    # Top Candidate Highlight Box
    lead_info = [
        [Paragraph("<b>Lead Developer Name:</b>", body_style), Paragraph(str(lead_dev['name']), body_style)],
        [Paragraph("<b>Developer ID:</b>", body_style), Paragraph(str(lead_dev['id']), body_style)],
        [Paragraph("<b>Relevant Experience:</b>", body_style), Paragraph(f"{lead_dev['exp']} Years", body_style)],
        [Paragraph("<b>Skill Match Score:</b>", body_style), Paragraph(f"{lead_dev['match']}", highlight_style)],
        [Paragraph("<b>Matching Stack:</b>", body_style), Paragraph(str(lead_dev['skills']), body_style)]
    ]
    t_lead = Table(lead_info, colWidths=[150, 370])
    t_lead.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#7C3AED')),
        ('PADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_lead)
    story.append(Spacer(1, 15))

    # 3. Execution Plan & Architecture Overview
    story.append(Paragraph("2. Technical Execution Plan", heading_style))
    execution_text = f"""
    The project implementation will be spearheaded by <b>{lead_dev['name']}</b>. The architecture design and core module development 
    will leverage target technologies including <b>{', '.join(req_skills)}</b>. Key delivery phases include Architecture Blueprinting, 
    Agile Sprint Execution, Continuous Testing, and Final Deployment.
    """
    story.append(Paragraph(execution_text, body_style))
    story.append(Spacer(1, 15))

    # 4. Complete Resource Pool Breakdown Table
    story.append(Paragraph("3. Full Matched Developer Team", heading_style))
    
    table_data = [["Dev ID", "Name", "Experience", "Match Score", "Matching Skills"]]
    for _, row in sorted_df.iterrows():
        table_data.append([
            str(row['id']),
            str(row['name']),
            f"{row['exp']} Yrs",
            str(row['match']),
            str(row['skills'])
        ])

    t_team = Table(table_data, colWidths=[65, 110, 75, 80, 190])
    t_team.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1A1A32')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E1')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F1F5F9')])
    ]))
    story.append(t_team)

    doc.build(story)
    buffer.seek(0)
    return buffer

# ==========================================
# 4. Main Grid Layout
# ==========================================
col_nav, col_main = st.columns([0.22, 0.78])

# --- LEFT CONTROL PANEL ---
with col_nav:
    st.markdown("""
        <div class="nav-panel">
            <div class="nav-title">⚙️ Modern IoT Dashboard</div>
            <div class="nav-item active">📊 IoT Dashboard</div>
            <div class="nav-item">📱 Smart Devices</div>
            <div class="nav-item">📡 WiFi Devices</div>
            <div class="nav-item">🎛️ Remote Controls</div>
            <div class="nav-item">📈 System Metrics</div>
            <div class="nav-item">⚙️ Settings</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Tools inside panel
    with st.expander("👤 Role Access"):
        user_role = st.radio("Select View", ["HR / Admin View", "Client / PM View"])

    # --- ADD DEVELOPER WITH AUTO-CLEAR FORM INPUTS ---
    with st.expander("➕ Add Developer"):
        next_id_num = len(df_devs) + 101
        auto_dev_id = f"DEV-{next_id_num}"

        with st.form("add_dev_form", clear_on_submit=True):
            st.text_input("Dev ID (Auto-Generated)", value=auto_dev_id, disabled=True)
            n_name = st.text_input("Full Name")
            n_skills = st.text_input("Skills (comma-separated, e.g. Python, React)")
            n_exp = st.number_input("Experience (Years)", 0, 30, 3)
            n_rate = st.number_input("Hourly Rate ($)", 10, 200, 40)
            
            if st.form_submit_button("Save to DB"):
                if n_name and n_skills:
                    try:
                        engine = get_db_engine()
                        with engine.connect() as conn:
                            conn.execute(
                                text("INSERT INTO developers (id, name, skills, experience_years, hourly_rate, on_bench) VALUES (:id, :name, :skills, :exp, :rate, TRUE);"),
                                {"id": auto_dev_id, "name": n_name, "skills": n_skills, "exp": n_exp, "rate": n_rate}
                            )
                            conn.commit()
                        st.success(f"{n_name} ({auto_dev_id}) successfully added!")
                        st.rerun()
                    except Exception as ex:
                        st.error(f"Error saving to database: {ex}")
                else:
                    st.warning("Please fill in Name and Skills.")

    with st.expander("📄 AI Resume Parser"):
        up_pdf = st.file_uploader("Upload CV", type=["pdf"])
        if up_pdf:
            txt = "".join([p.extract_text() for p in PdfReader(up_pdf).pages if p.extract_text()])
            found = [s for s in ["Python", "FastAPI", "React", "Docker", "Node.js"] if re.search(r'\b'+s+r'\b', txt, re.I)]
            st.info(f"Found: {', '.join(found)}")

# --- RIGHT MAIN DASHBOARD CONTENT ---
with col_main:
    if db_err:
        st.error(f"MySQL Error: {db_err}")
        st.warning("Make sure XAMPP MySQL is turned ON!")
        st.stop()

    total_devs = len(df_devs)
    bench_df = df_devs[df_devs['on_bench'] == True]
    allocated_devs = total_devs - len(bench_df)
    bench_devs = len(bench_df)
    hourly_burn = bench_df['hourly_rate'].sum() if not bench_df.empty else 0
    utilization_rate = round((allocated_devs / total_devs) * 100) if total_devs > 0 else 0

    # --- TOP ROW LABEL CARDS ---
    k1, k2 = st.columns(2)
    with k1:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"""
                <div class="kpi-card">
                    <div><div class="kpi-title">Bench Developers</div><div class="kpi-val">{bench_devs} Devs</div></div>
                    <button class="badge-purple">Export</button>
                </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown(f"""
                <div class="kpi-card">
                    <div><div class="kpi-title">Hourly Burn Cost</div><div class="kpi-val">${hourly_burn if user_role=='HR / Admin View' else '***'}</div></div>
                    <button class="badge-green">Documentation</button>
                </div>
            """, unsafe_allow_html=True)
            
    with k2:
        c3, c4 = st.columns(2)
        with c3:
            st.markdown(f"""
                <div class="kpi-card">
                    <div><div class="kpi-title">Utilization Rate</div><div class="kpi-val">{utilization_rate}%</div></div>
                    <button class="badge-purple">Status</button>
                </div>
            """, unsafe_allow_html=True)
        with c4:
            st.markdown(f"""
                <div class="kpi-card">
                    <div><div class="kpi-title">Total Dev Pool</div><div class="kpi-val">{total_devs} Total</div></div>
                    <button class="badge-orange">Pool</button>
                </div>
            """, unsafe_allow_html=True)

    # --- MIDDLE ROW WIDGETS ---
    m_left, m_right = st.columns([1, 1.2])

    with m_left:
        g1, g2 = st.columns(2)
        with g1:
            fig_gauge = go.Figure(go.Indicator(
                mode="gauge+number", value=utilization_rate,
                number={'suffix': "%", 'font': {'color': '#FFF', 'size': 26}},
                gauge={
                    'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#282846"},
                    'bar': {'color': "#F59E0B"},
                    'bgcolor': "#1A1A32",
                    'steps': [{'range': [0, 50], 'color': "#1A1A32"}, {'range': [50, 100], 'color': "#282846"}]
                }
            ))
            fig_gauge.update_layout(paper_bgcolor="#1A1A32", font=dict(color="#FFF"), height=190, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(fig_gauge, width="stretch")

        with g2:
            fig_donut = go.Figure(data=[go.Pie(
                labels=['Bench', 'Allocated'], 
                values=[bench_devs, allocated_devs], 
                hole=.68, marker=dict(colors=['#7C3AED', '#10B981'])
            )])
            fig_donut.update_layout(
                showlegend=False, paper_bgcolor="#1A1A32", height=190, margin=dict(l=10, r=10, t=10, b=10),
                annotations=[dict(text=f'{utilization_rate}%<br><span style="font-size:10px;">Allocated</span>', x=0.5, y=0.5, font_size=15, font_color="#FFF", showarrow=False)]
            )
            st.plotly_chart(fig_donut, width="stretch")

    with m_right:
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        fig_waves = go.Figure()
        fig_waves.add_trace(go.Scatter(
            x=days, y=[100, 230, 120, 180, 250, 210, 220], mode='lines', fill='tozeroy',
            line=dict(color='#10B981', width=3, shape='spline'), fillcolor='rgba(16, 185, 129, 0.25)'
        ))
        fig_waves.add_trace(go.Scatter(
            x=days, y=[150, 180, 280, 120, 290, 310, 270], mode='lines', fill='tozeroy',
            line=dict(color='#7C3AED', width=3, shape='spline'), fillcolor='rgba(124, 58, 237, 0.25)'
        ))
        fig_waves.update_layout(
            showlegend=False, paper_bgcolor="#1A1A32", plot_bgcolor="#1A1A32",
            font=dict(color="#94A3B8"), height=190, margin=dict(l=10, r=10, t=10, b=10),
            xaxis=dict(showgrid=False), yaxis=dict(showgrid=False)
        )
        st.plotly_chart(fig_waves, width="stretch")

    # --- BOTTOM ROW: TEAM MATCHING & PROPOSAL GENERATION ---
    all_skills = sorted(list(set([sk for sub in df_devs['skills_list'] for sk in sub]))) if not df_devs.empty else []

    st.markdown("### 🎯 Match Project Team")
    with st.form("match_form"):
        cx, cy, cz = st.columns(3)
        p_name = cx.text_input("Project Name", "Enterprise Payment Gateway")
        req_sk = cy.multiselect("Skills", options=all_skills, default=all_skills[:2] if all_skills else [])
        m_rate = cz.number_input("Max Rate ($/hr)", 10, 200, 50)
        btn = st.form_submit_button("⚡ Run Team Matching Engine")

    if btn or 'last_matches' in st.session_state:
        if btn:
            req_set = set(req_sk)
            matches = []
            for _, d in df_devs.iterrows():
                if not d['on_bench']: continue
                if user_role == "HR / Admin View" and d['hourly_rate'] > m_rate: continue
                
                m_set = req_set.intersection(set(d['skills_list']))
                score = (len(m_set)/len(req_set))*100 if req_set else 0
                if score > 0:
                    matches.append({
                        "id": d['id'], "name": d['name'], 
                        "exp": d['experience_years'], "rate": d['hourly_rate'], 
                        "match": f"{round(score)}%", "skills": ", ".join(m_set)
                    })
            st.session_state['last_matches'] = matches
            st.session_state['last_pname'] = p_name
            st.session_state['last_req_sk'] = req_sk

        matches = st.session_state.get('last_matches', [])
        p_name = st.session_state.get('last_pname', p_name)
        req_sk = st.session_state.get('last_req_sk', req_sk)

        if matches:
            res = pd.DataFrame(matches)
            
            # Highlight Top Lead Developer
            sorted_res = res.copy()
            sorted_res['num_score'] = sorted_res['match'].str.rstrip('%').astype(float)
            top_dev = sorted_res.sort_values(by='num_score', ascending=False).iloc[0]

            st.info(f"🏆 **Recommended Project Lead:** {top_dev['name']} ({top_dev['id']}) with **{top_dev['match']}** Skill Match Score!")

            if user_role != "HR / Admin View":
                res_display = res.drop(columns=['rate'])
            else:
                res_display = res
                
            st.dataframe(res_display, width="stretch")
            
            # Interactive Developer Assignment
            st.markdown("#### 📌 Assign Developer to Project")
            assign_cols = st.columns([3, 1])
            with assign_cols[0]:
                selected_dev_id = st.selectbox("Select Developer to Assign", options=res['id'].tolist())
            with assign_cols[1]:
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("🚀 Assign & Update Graph"):
                    if assign_developer(selected_dev_id):
                        st.success(f"{selected_dev_id} assigned to project! Database and Graphs updated.")
                        if 'last_matches' in st.session_state:
                            del st.session_state['last_matches']
                        st.rerun()
                    else:
                        st.error("Failed to update status in DB.")

            # Full Detailed Project Proposal PDF Download Button
            pdf_bytes = generate_detailed_proposal_pdf(p_name, res, req_sk)
            st.download_button(
                label="📄 Download Detailed Project Proposal PDF (Lead Focused)",
                data=pdf_bytes,
                file_name=f"{p_name.replace(' ', '_')}_Lead_Proposal.pdf",
                mime="application/pdf"
            )
        else:
            st.error("No matching bench developers found for the given criteria.")