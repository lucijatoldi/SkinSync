# SkinSync - An Ontology-Based Expert System for Skin Disease Diagnosis

**SkinSync** is a web application that functions as an expert system, providing users with informational support in identifying potential skin diseases based on selected symptoms and affected body parts.

The core of the system is a **knowledge base modeled as an RDF ontology**. Queries against the knowledge base are executed using the **SPARQL** query language, enabling logical inference.

## 🚀 Live Demo

You can access and test the live version of this application, deployed on Railway, at the following URL:

**https://skinsync-production.up.railway.app**


## ✨ Key Features

*   **Intelligent Diagnostics:** Dynamically constructs SPARQL queries to search the knowledge graph based on user input.
*   **Detailed Results:** Displays recommended treatments and known triggers for each potential diagnosis.
*   **User Authentication & Profiles:** A complete user management system for registration and authentication.
*   **PDF Report Generation:** Logged-in users can generate and download a personalized PDF with their diagnosis results.
*   **Cloud Deployed:** The application has been successfully deployed to the Railway cloud platform, including a database migration from SQLite to PostgreSQL.
*   **Automated Testing:** Includes unit and integration tests using Django's test framework to ensure code quality.


## 🛠️ Tech Stack

*   **Backend:** Python, Django
*   **Database:** PostgreSQL
*   **Knowledge Base:** `rdflib` (for working with the RDF graph), SPARQL
*   **Document Generation:** ReportLab
*   **Deployment:** Railway
*   **Testing:** Django Test Framework
*   **Frontend:** HTML, CSS, JavaScript

## QA (Summary)

This repository includes a short QA package focused on manual testing:
- Test plan: [QA_TEST_PLAN_SkinSync.md](./docs/qa/QA_TEST_PLAN_SkinSync.md)
- Test cases: [TEST_CASES_SkinSync.md](./docs/qa/TEST_CASES_SkinSync.md)
- Results and evidence (screenshots): [QA_RESULTS_SkinSync.md](./docs/qa/QA_RESULTS_SkinSync.md), [qa/evidence](./docs/qa/evidence/)



## 🚀 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

*   Python 3.x installed
*   A local PostgreSQL server installed and running

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/lucijatoldi/SkinSync.git
    cd SkinSync
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/Scripts/activate  # On Windows (Git Bash)
    ```
3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure your database:**
    *   Make sure your local PostgreSQL server is running.
    *   Create a `.env` file in the project root and add your database connection string:
        ```
        DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/DB_NAME
        ```
5.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```
6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000/`.

---

> _**Disclaimer:** This application is an academic project and is intended for informational purposes only. It is not a substitute for a professional medical diagnosis or consultation._
