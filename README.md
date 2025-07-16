# SkinSync - An Ontology-Based Expert System for Skin Disease Diagnosis

## 📖 About The Project

**SkinSync** is a web application that functions as an **expert system**, providing users with informational support in identifying potential skin diseases based on selected symptoms and affected body parts.

The core of the system is a **knowledge base modeled as an RDF ontology**. This graph-based approach allows for a flexible and powerful representation of the complex relationships between medical entities. Queries against the knowledge base are executed using the **SPARQL** query language, enabling logical inference.

## ✨ Key Features

* **Intelligent Diagnostics:** The system dynamically constructs SPARQL queries to search the knowledge graph and find conditions that match the user's input.
* **Detailed Results:** For each potential diagnosis, the application displays recommended treatments and known triggers to avoid.
* **User Authentication & Profiles:** A built-in user management system based on Django for registration and authentication.
* **PDF Report Generation:** Logged-in users can generate and download a personalized PDF document with their diagnosis results.
* **Automated Testing:** The project includes both unit and integration tests, written using Django's test framework, to ensure code quality and reliability.

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Knowledge Base:** rdflib (for working with the RDF graph), SPARQL
* **Frontend:** HTML, CSS, JavaScript
* **Document Generation:** ReportLab
* **Testing:** Django Test Framework
* **Database (Users):** SQLite

## 🚀 Getting Started

To get a local copy up and running, follow these simple steps.

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/lucijatoldi/SkinSync.git
   cd SkinSync
   ```
2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv

   # On Windows (Git Bash):
   source venv/Scripts/activate

   # On Windows (CMD/PowerShell):
   .\venv\Scripts\activate
   ```
3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```
4. **Run database migrations (for the user model):**

   ```bash
   python manage.py migrate
   ```
5. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

   The application will be available at `http://127.0.0.1:8000/`.

---

_**Disclaimer:** This application is an academic project and is intended for informational purposes only. It is not a substitute for a professional medical diagnosis or consultation._
