<div align="center">

# 🔮 BenchFix
### Real-Time Bench Intelligence & Resource Allocation Dashboard

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<p align="center">
  <b>BenchFix</b> is a data-driven resource management dashboard built specifically for software houses, agency teams, and IT consulting firms to eliminate bench idle time, optimize developer allocation, monitor hourly burn costs, and instantly generate client-ready proposal PDFs.
</p>

---

<img src="https://github.com/user-attachments/assets/e3e5b2ca-27de-4454-b7ba-a71fa684c88f" alt="BenchFix Dashboard Overview" width="100%" />

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Visual Showcase](#-visual-showcase)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Database Setup](#database-setup)
  - [Installation & Execution](#installation--execution)
- [Database Schema & Seed Data](#-database-schema--seed-data)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

---

## 📖 Overview

In modern software development and consulting agencies, having developers unassigned on "the bench" leads to unmonitored financial burn. **BenchFix** provides an all-in-one real-time command center that:

- **Quantifies Bench Costs**: Calculates live financial burn rates and company-wide resource utilization.
- **Speeds Up Team Matching**: Automatically scores candidate skill overlap against project requirements and budget constraints.
- **Empowers Sales & Management**: Generates polished, executive-level proposal PDFs in a single click with designated Project Leads.
- **Protects Financial Privacy**: Offers role-based switching to mask sensitive hourly developer rates in client-facing scenarios.

---

## ✨ Key Features

- **📊 Live Financial & Utilization Analytics**:
  - Real-time KPI cards for Active Bench Developers, Hourly Burn Rate ($), Utilization Rate (%), and Total Developer Pool.
  - Interactive Plotly gauge meters, allocation donut charts, and workload trend waves that update dynamically upon developer assignment.

- **🔒 Role-Based Access Control (RBAC)**:
  - **HR / Admin View**: Full visibility into developer hourly rates, burn costs, and budget filtering.
  - **Client / PM View**: Masks sensitive financial rates (`$***`) to safely present candidate profiles to clients.

- **➕ Automated Developer Onboarding**:
  - Auto-generated sequential developer IDs (`DEV-101`, `DEV-102`, etc.).
  - Clean modal-style forms with auto-reset upon successful database entry into MySQL.

- **🎯 Intelligent Team Matching Engine**:
  - Matches unassigned bench talent with target project requirements.
  - Calculates percentage-based skill compatibility scores and respects maximum hourly budget limits.

- **🏆 Lead Developer Recommendation & One-Click Assignment**:
  - Automatically identifies the top-ranked candidate as the designated Project Lead.
  - Instant project assignment action that updates developer availability in MySQL and refreshes all dashboard charts in real time.

- **📄 Client-Ready PDF Proposal Generator**:
  - Compiles comprehensive project proposals with Executive Summaries, Lead Developer highlights, delivery roadmaps, and full team breakdowns using ReportLab.

- **🤖 AI Resume / CV Skill Extractor**:
  - Upload PDF developer resumes to automatically detect and extract technology keywords (Python, FastAPI, React, Docker, Node.js, etc.) via PyPDF.

---

## 🖼️ Visual Showcase

| Feature | Screenshot |
| :--- | :--- |
| **Main Dashboard & Live KPIs**<br>Live utilization gauges, donut allocation charts, and trend metrics. | <img src="https://github.com/user-attachments/assets/e3e5b2ca-27de-4454-b7ba-a71fa684c88f" width="550" alt="Dashboard KPIs" /> |
| **Team Matching & Lead Selection**<br>Skill compatibility scoring, Project Lead designation, and assignment. | <img src="https://github.com/user-attachments/assets/ab5a8077-1d53-43d2-9f6e-ae3d11d835e7" width="550" alt="Team Matching Engine" /> |
| **Automated Developer Onboarding**<br>Auto-increment ID assignment, form validation, and database storage. | <img src="https://github.com/user-attachments/assets/37864350-52e5-412b-af29-c66a0bba4fa9" width="550" alt="Add Developer Form" /> |
| **AI Resume Parser**<br>Instant keyword extraction from uploaded developer CV documents. | <img src="https://github.com/user-attachments/assets/781a6521-6bd6-4626-a5cb-37806de78225" width="550" alt="AI Resume Parser" /> |
| **Generated Proposal PDF**<br>Client-ready proposal with technical execution plan and candidate profiles. | <img src="https://github.com/user-attachments/assets/30187442-8fa3-4eba-a4a4-78bdf93996e8" width="550" alt="PDF Proposal Document" /> |
| **Database Schema (phpMyAdmin)**<br>Structured MySQL persistence powering developer records and statuses. | <img src="https://github.com/user-attachments/assets/aa6a42b2-3cef-448b-adf0-f715248dedca" width="550" alt="phpMyAdmin MySQL Table" /> |

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Frontend UI** | [Streamlit](https://streamlit.io/) | Interactive web dashboard with custom dark purple CSS theme |
| **Visualizations** | [Plotly](https://plotly.com/) | Real-time gauge meters, donut charts, and trend graphs |
| **Backend Core** | Python 3.9+ | Application logic, session state, and data filtering |
| **Data Processing** | [Pandas](https://pandas.pydata.org/) | In-memory data manipulation and scoring calculations |
| **Database** | MySQL (XAMPP / Localhost) | Relational storage for developers and assignment states |
| **ORM / Driver** | SQLAlchemy & PyMySQL | Database connectivity and SQL query execution |
| **PDF Generation** | [ReportLab](https://www.reportlab.com/) | Programmatic enterprise proposal PDF export |
| **Document Parsing** | [PyPDF](https://pypdf.readthedocs.io/) | Extracting text and parsing keywords from uploaded resumes |

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed on your machine:
- **Python 3.9+**: [Download Python](https://www.python.org/downloads/)
- **XAMPP / MySQL Server**: [Download XAMPP](https://www.apachefriends.org/) (for Apache and MySQL)
- **Git**: [Download Git](https://git-scm.com/)

---

### Database Setup

1. Launch **XAMPP Control Panel** and start **Apache** and **MySQL** services.
2. Open [http://localhost/phpmyadmin](http://localhost/phpmyadmin) in your web browser.
3. Create a new database named:
   ```sql
   CREATE DATABASE benchpulse_db;
   ```
4. Select `benchpulse_db` and execute the following SQL statement in the **SQL** tab:

   ```sql
   CREATE TABLE developers (
       id VARCHAR(20) PRIMARY KEY,
       name VARCHAR(100) NOT NULL,
       skills TEXT NOT NULL,
       experience_years INT NOT NULL,
       hourly_rate DECIMAL(10,2) NOT NULL,
       on_bench BOOLEAN DEFAULT TRUE
   );
   ```

5. *(Optional but Recommended)* Insert sample seed data to test immediately:

   ```sql
   INSERT INTO developers (id, name, skills, experience_years, hourly_rate, on_bench) VALUES
   ('DEV-101', 'Alex Morgan', 'Python, FastAPI, Docker, PostgreSQL', 5, 45.00, TRUE),
   ('DEV-102', 'Sophia Chen', 'React, TypeScript, Node.js, TailwindCSS', 4, 40.00, TRUE),
   ('DEV-103', 'Marcus Vance', 'Python, React, AWS, GraphQL', 6, 55.00, TRUE),
   ('DEV-104', 'Elena Rostova', 'Flutter, Dart, Firebase, iOS', 3, 35.00, FALSE),
   ('DEV-105', 'David Kim', 'Java, Spring Boot, Microservices, Kubernetes', 7, 60.00, TRUE);
   ```

---

### Installation & Execution

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/faizitech11/BenchFix.git
   cd BenchFix
   ```

2. **Create & Activate a Virtual Environment** *(Recommended)*:
   - **Windows (PowerShell)**:
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - **macOS / Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   *Or install directly via:*
   ```bash
   pip install streamlit pandas plotly sqlalchemy pymysql pypdf reportlab
   ```

4. **Verify Database Connection**:
   In [app.py](file:///d:/python/bencfix/BenchFix/app.py), confirm the MySQL connection string matches your local credentials:
   ```python
   MYSQL_URL = "mysql+pymysql://root:@localhost:3306/benchpulse_db"
   ```

5. **Run the Dashboard**:
   ```bash
   streamlit run app.py
   ```
   The application will automatically open in your default browser at `http://localhost:8501`.

---

## 🗄️ Database Schema & Seed Data

```
+------------------+---------------+------+-----+---------+-------+
| Field            | Type          | Null | Key | Default | Extra |
+------------------+---------------+------+-----+---------+-------+
| id               | varchar(20)   | NO   | PRI | NULL    |       |
| name             | varchar(100)  | NO   |     | NULL    |       |
| skills           | text          | NO   |     | NULL    |       |
| experience_years | int           | NO   |     | NULL    |       |
| hourly_rate      | decimal(10,2) | NO   |     | NULL    |       |
| on_bench         | tinyint(1)    | YES  |     | 1       |       |
+------------------+---------------+------+-----+---------+-------+
```

---

## 📁 Project Structure

```text
BenchFix/
│
├── app.py              # Main Streamlit dashboard, queries, and PDF proposal engine
├── requirements.txt    # Python package dependencies
├── README.md           # Project documentation and setup guide
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check the [issues page](https://github.com/faizitech11/BenchFix/issues) or submit a pull request:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
