 BenchFix
BenchPulse is a real-time bench management dashboard that optimizes developer allocations, tracks bench costs, and generates client-ready proposal PDFs.

BenchFix — Real-Time Bench Intelligence & Resource Allocation Dashboard

BenchFix is a data-driven resource management dashboard built specifically for software houses and IT consulting agencies. It helps HR managers, Resource Managers, and Project Leads track unassigned bench talent, monitor hourly financial burn costs, match candidate skills with project requirements, and generate client-ready proposal PDFs in one click.

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
