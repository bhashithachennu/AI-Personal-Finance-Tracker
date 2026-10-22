#  AI Personal Finance Tracker

A beginner-friendly personal finance management application built using Python and Streamlit.

This project helps users track their income and expenses, analyze their spending patterns, visualize financial data, and receive simple financial insights.

The project was developed as an experiment to understand AI-assisted software development using GitHub Copilot.

---

##  Features

###  Transaction Management
- Add income and expense transactions
- Store transactions locally using SQLite database
- View all saved transactions

###  Financial Dashboard
- Calculate total income
- Calculate total expenses
- Display current balance

###  Data Visualization
- Expense breakdown by category
- Income vs expense comparison charts

###  Smart Insights
- Identify highest spending category
- Compare expenses with income
- Provide simple financial observations using rule-based logic

---

##  Technologies Used

| Technology | Purpose |
|------------|---------|
| Python     | Core programming language |
| Streamlit  | User interface and web application  |
| SQLite     | Local database storage |
| Pandas     | Data analysis and calculations |
| Matplotlib | Data visualization |
| GitHub Copilot | AI-assisted development |

---

##  Project Structure

```
AI-Personal-Finance-Tracker/

│
├── app.py              # Main Streamlit application
├── database.py         # SQLite database operations
├── analysis.py         # Financial calculations using Pandas
├── charts.py           # Visualization functions
├── insights.py         # Spending insight generation
│
├── requirements.txt    # Required Python packages
├── README.md           # Project documentation
└── .gitignore          # Files excluded from GitHub
```

---

##  Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AI-Personal-Finance-Tracker.git
```

### 2. Navigate into the project folder

```bash
cd AI-Personal-Finance-Tracker
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## Application Workflow

```
User Input
    ↓
Streamlit Interface
    ↓
SQLite Database
    ↓
Pandas Analysis
    ↓
Charts + Financial Insights
```

---

##  Future Improvements

- Add user authentication
- Add monthly budget tracking
- Add AI-generated financial summaries using LLMs
- Add export reports (PDF/Excel)
- Add cloud database support

---

##  Learning Outcomes

Through this project, I explored:

- Building a complete Python application
- Structuring a software project into multiple modules
- Database integration using SQLite
- Data analysis using Pandas
- Data visualization
- AI-assisted development using GitHub Copilot

---

##  Author

**Bhashitha Chennu**
