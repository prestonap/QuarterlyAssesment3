import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# ---------------------- DATABASE SETUP ---------------------- #
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()

categories = ["BusinessApps", "ReligiousStudies", "Analytics", "Databases"]

# Create each category table
for category in categories:
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {category} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            option1 TEXT NOT NULL,
            option2 TEXT NOT NULL,
            option3 TEXT NOT NULL,
            option4 TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    """)
#Questions for each category
questions_data = {
    "BusinessApps": [
        ("Which software is commonly used for spreadsheet tasks?", "Excel", "Word", "Access", "PowerPoint", "Excel"),
        ("Which tool is best for creating professional presentations?", "Word", "Excel", "PowerPoint", "Outlook", "PowerPoint"),
        ("What is Microsoft Access used for?", "Emailing", "Database Management", "Document Editing", "Scheduling", "Database Management"),
        ("Which application is used for email communication in Office?", "Excel", "Access", "Outlook", "Word", "Outlook"),
        ("Which shortcut saves a document?", "Ctrl+C", "Ctrl+V", "Ctrl+S", "Ctrl+Z", "Ctrl+S"),
        ("What does CRM stand for?", "Customer Resource Management", "Client Relationship Management", "Customer Relationship Management", "Corporate Resource Management", "Customer Relationship Management"),
        ("Which software helps manage company resources and planning?", "ERP", "CRM", "VPN", "SaaS", "ERP"),
        ("What is cloud computing primarily used for?", "Local Storage", "Remote Processing", "Online Banking", "Creating Spreadsheets", "Remote Processing"),
        ("Which tool is most commonly used for remote team collaboration?", "Slack", "Word", "Photoshop", "Excel", "Slack"),
        ("Which application automates repetitive business tasks?", "Excel Macros", "Outlook", "PowerPoint", "Paint", "Excel Macros"),
    ],
    "ReligiousStudies": [
        ("What is the holy book of Islam?", "Torah", "Bible", "Quran", "Vedas", "Quran"),
        ("Which religion believes in the Four Noble Truths?", "Christianity", "Islam", "Buddhism", "Judaism", "Buddhism"),
        ("What is the central text of Christianity?", "Bible", "Quran", "Tripitaka", "Torah", "Bible"),
        ("Who led the Israelites out of Egypt?", "Abraham", "Moses", "Jesus", "Muhammad", "Moses"),
        ("Which religion practices the Five Pillars?", "Christianity", "Judaism", "Islam", "Hinduism", "Islam"),
        ("Who is considered the founder of Buddhism?", "Jesus", "Muhammad", "Buddha", "Moses", "Buddha"),
        ("What is the Hindu term for the cycle of rebirth?", "Karma", "Dharma", "Moksha", "Samsara", "Samsara"),
        ("Where do Jews worship?", "Mosque", "Church", "Temple", "Synagogue", "Synagogue"),
        ("Which text is foundational in Hinduism?", "Bible", "Torah", "Quran", "Bhagavad Gita", "Bhagavad Gita"),
        ("Which religion celebrates Ramadan?", "Christianity", "Judaism", "Islam", "Buddhism", "Islam"),
    ],
    "Analytics": [
        ("What is the primary goal of data analytics?", "Data entry", "Data visualization", "Insight generation", "Data deletion", "Insight generation"),
        ("Which of these is a data visualization tool?", "Excel", "Photoshop", "Illustrator", "Premiere Pro", "Excel"),
        ("What does KPI stand for?", "Key Performance Indicator", "Knowledge Performance Index", "Key Progress Insight", "Known Progress Indicator", "Key Performance Indicator"),
        ("Which programming language is common in data analysis?", "Python", "HTML", "JavaScript", "CSS", "Python"),
        ("Which chart best shows parts of a whole?", "Bar chart", "Pie chart", "Line chart", "Scatter plot", "Pie chart"),
        ("What does a regression analysis measure?", "Color", "Relationship between variables", "Length", "Weight", "Relationship between variables"),
        ("What is a dashboard in analytics?", "Hardware", "Car display", "Visual report", "App installer", "Visual report"),
        ("What tool is widely used for business intelligence?", "Excel", "Power BI", "Word", "Access", "Power BI"),
        ("What is 'Big Data' known for?", "Volume, Variety, Velocity", "Size", "Speed", "Charts", "Volume, Variety, Velocity"),
        ("Which method predicts future trends based on past data?", "Descriptive analytics", "Diagnostic analytics", "Predictive analytics", "Prescriptive analytics", "Predictive analytics"),
    ],
    "Databases": [
        ("What does SQL stand for?", "Simple Query Language", "Structured Query Language", "Standard Query Level", "Sequential Query Logic", "Structured Query Language"),
        ("Which command retrieves data from a database?", "SELECT", "INSERT", "DELETE", "UPDATE", "SELECT"),
        ("Which key uniquely identifies each row?", "Foreign Key", "Unique Key", "Primary Key", "Index Key", "Primary Key"),
        ("Which clause filters results in SQL?", "ORDER BY", "GROUP BY", "WHERE", "SELECT", "WHERE"),
        ("What is a relational database?", "Table-less database", "Database with text only", "Database with related tables", "Flat file", "Database with related tables"),
        ("Which command adds new data?", "INSERT", "SELECT", "UPDATE", "DELETE", "INSERT"),
        ("What is normalization?", "Data duplication", "Data organization", "Data destruction", "Data encryption", "Data organization"),
        ("Which of these is a database management system?", "Python", "MySQL", "Java", "HTML", "MySQL"),
        ("What does a JOIN do in SQL?", "Deletes data", "Combines rows from two tables", "Changes table names", "Updates records", "Combines rows from two tables"),
        ("Which SQL command modifies data?", "UPDATE", "INSERT", "DROP", "SELECT", "UPDATE"),
    ]
}

# Populate database with questions
for category, questions in questions_data.items():
    for q in questions:
        cursor.execute(f"SELECT COUNT(*) FROM {category} WHERE question = ?", (q[0],))
        if cursor.fetchone()[0] == 0:
            cursor.execute(f"INSERT INTO {category} (question, option1, option2, option3, option4, answer) VALUES (?, ?, ?, ?, ?, ?)", q)

conn.commit()
