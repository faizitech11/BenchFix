<img width="1366" height="768" alt="Screenshot 2026-08-29 045825" src="https://github.com/user-attachments/assets/e3e5b2ca-27de-4454-b7ba-a71fa684c88f" />
<img width="1366" height="768" alt="Screenshot 2026-08-29 050141" src="https://github.com/user-attachments/assets/ab5a8077-1d53-43d2-9f6e-ae3d11d835e7" />
<img width="629" height="496" alt="Screenshot_29-8-2026_5224_localhost" src="https://github.com/user-attachments/assets/aa6a42b2-3cef-448b-adf0-f715248dedca" />
<img width="1366" height="768" alt="Screenshot 2026-08-29 050405" src="https://github.com/user-attachments/assets/37864350-52e5-412b-af29-c66a0bba4fa9" />
<img width="1366" height="768" alt="Screenshot 2026-08-29 050431" src="https://github.com/user-attachments/assets/781a6521-6bd6-4626-a5cb-37806de78225" />
<img width="1366" height="768" alt="Screenshot 2026-08-29 050509" src="https://github.com/user-attachments/assets/30187442-8fa3-4eba-a4a4-78bdf93996e8" />
 BenchFix
BenchPulse is a real-time bench management dashboard that optimizes developer allocations, tracks bench costs, and generates client-ready proposal PDFs.

BenchFix — Real-Time Bench Intelligence & Resource Allocation Dashboard

BenchFix is a data-driven resource management dashboard built specifically for software houses and IT consulting agencies. It helps HR managers, Resource Managers, and Project Leads track unassigned bench talent, monitor hourly financial burn costs, match candidate skills with project requirements, and generate client-ready proposal PDF in one click.

Key Capabilities

Live Financial & Utilization Analytics: Real-time KPI tracking for active bench developer count, total hourly burn cost ($), and company-wide utilization rate (%).

Role-Based Access Control: Toggle effortlessly between HR / Admin View (full cost visibility) and Client / PM View (automatically hides sensitive hourly rates).

Automated Developer Onboarding: Auto-generates unique IDs (DEV-101, DEV-102) with auto-clearing input forms upon successful database entry.

Dynamic Visual Feedback: Interactive Plotly gauge meters and donut charts update live whenever a developer is assigned to a project.

Intelligent Team Matching Engine: Calculates candidate skill match scores (%) based on required tech stacks, budget caps, and relevant experience.

Client-Ready PDF Proposal Generator: Automatically identifies top-matched candidates as designated Project Leads and compiles detailed proposal PDFs via ReportLab.

AI CV Skill Extractor: Scans uploaded PDF resumes to auto-detect core technology stack keywords.

Tech Stack & Dependencies

Frontend & UI: Streamlit (Custom Dark Purple CSS Theme)

Backend Core: Python, Pandas, SQLAlchemy, PyMySQL

Database Engine: MySQL Server (XAMPP / Localhost)

Data Visualizations: Plotly Interactive Graphs

Document Processing: ReportLab (PDF Engine) & PyPDF (Resume Parser)

Quick Setup Guide

Prerequisites
Ensure you have Python 3.9+ and XAMPP Control Panel installed on your system.

Database Initialization

Launch XAMPP Control Panel and start Apache and MySQL.

Open http://localhost/phpmyadmin in your browser.

Create a new database named benchpulse_db.

Run the following SQL query to create the developers table:

CREATE TABLE developers (
id VARCHAR(20) PRIMARY KEY,
name VARCHAR(100) NOT NULL,
skills TEXT NOT NULL,
experience_years INT NOT NULL,
hourly_rate DECIMAL(10,2) NOT NULL,
on_bench BOOLEAN DEFAULT TRUE
);

Repository Installation & Run

git clone https://github.com/faizitech11/BenchFix.git
cd BenchFix

pip install streamlit pandas plotly sqlalchemy pymysql pypdf reportlab

streamlit run app.py
