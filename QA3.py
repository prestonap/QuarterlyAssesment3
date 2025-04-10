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
    