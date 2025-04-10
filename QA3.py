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

# Questions for each category
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

# ---------------------- QUESTION CLASS ---------------------- #
class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def check_answer(self, selected):
        return self.answer == selected

# ---------------------- MAIN APPLICATION ---------------------- #
class QuizBowlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Bowl App")
        self.main_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def main_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Quiz Bowl Application", font=('Arial', 20)).pack(pady=20)
        tk.Button(self.root, text="Administrator Login", width=30, command=self.admin_login).pack(pady=10)
        tk.Button(self.root, text="Take a Quiz", width=30, command=self.select_category).pack(pady=10)

    def admin_login(self):
        self.clear_screen()
        tk.Label(self.root, text="Admin Login", font=('Arial', 16)).pack(pady=10)
        tk.Label(self.root, text="Enter Password:").pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)
        tk.Button(self.root, text="Login", command=self.check_admin_password).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.main_screen).pack(pady=5)

    def check_admin_password(self):
        if self.password_entry.get() == "Hello123":
            self.admin_menu()
        else:
            messagebox.showerror("Error", "Incorrect password")

    def admin_menu(self):
        self.clear_screen()
        tk.Label(self.root, text="Admin Menu", font=('Arial', 16)).pack(pady=10)
        tk.Button(self.root, text="Add Question", command=self.add_question_form).pack(pady=5)
        tk.Button(self.root, text="View Questions", command=self.view_questions).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.main_screen).pack(pady=5)

    def add_question_form(self):
        self.clear_screen()
        self.q_vars = {}
        tk.Label(self.root, text="Add Question", font=('Arial', 16)).pack(pady=10)
        self.q_vars['category'] = ttk.Combobox(self.root, values=categories)
        self.q_vars['category'].pack(pady=5)
        self.q_vars['question'] = tk.Entry(self.root, width=60)
        self.q_vars['question'].pack(pady=5)
        for i in range(1, 5):
            self.q_vars[f'option{i}'] = tk.Entry(self.root, width=40)
            self.q_vars[f'option{i}'].pack(pady=5)
        self.q_vars['answer'] = tk.Entry(self.root, width=40)
        self.q_vars['answer'].pack(pady=5)
        tk.Button(self.root, text="Submit", command=self.submit_question).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.admin_menu).pack(pady=5)

    def submit_question(self):
        cat = self.q_vars['category'].get()
        if cat not in categories:
            messagebox.showerror("Error", "Please select a valid category")
            return
        try:
            cursor.execute(f"INSERT INTO {cat} (question, option1, option2, option3, option4, answer) VALUES (?, ?, ?, ?, ?, ?)",
                (self.q_vars['question'].get(),
                self.q_vars['option1'].get(),
                self.q_vars['option2'].get(),
                self.q_vars['option3'].get(),
                self.q_vars['option4'].get(),
                self.q_vars['answer'].get()))
            conn.commit()
            messagebox.showinfo("Success", "Question added successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def view_questions(self):
        self.clear_screen()
        tk.Label(self.root, text="Select Category", font=('Arial', 16)).pack(pady=10)
        self.cat_select = ttk.Combobox(self.root, values=categories)
        self.cat_select.pack(pady=5)
        tk.Button(self.root, text="View", command=self.display_questions).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.admin_menu).pack(pady=5)

    def display_questions(self):
        cat = self.cat_select.get()
        if cat not in categories:
            messagebox.showerror("Error", "Invalid category")
            return
        self.clear_screen()
        tk.Label(self.root, text=f"Questions in {cat}", font=('Arial', 16)).pack(pady=10)
        rows = cursor.execute(f"SELECT * FROM {cat}").fetchall()
        for row in rows:
            q_text = f"{row[0]}. {row[1]} ({row[6]})"
            tk.Label(self.root, text=q_text, wraplength=500).pack(anchor='w', padx=10)
        tk.Button(self.root, text="Back", command=self.view_questions).pack(pady=10)

    def select_category(self):
        self.clear_screen()
        tk.Label(self.root, text="Select Quiz Category", font=('Arial', 16)).pack(pady=10)
        self.quiz_category = ttk.Combobox(self.root, values=categories)
        self.quiz_category.pack(pady=5)
        tk.Button(self.root, text="Start Quiz", command=self.start_quiz).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.main_screen).pack(pady=5)

    def start_quiz(self):
        cat = self.quiz_category.get()
        if cat not in categories:
            messagebox.showerror("Error", "Select a valid category")
            return
        self.questions = [
            Question(q[1], [q[2], q[3], q[4], q[5]], q[6])
            for q in cursor.execute(f"SELECT * FROM {cat}").fetchall()
        ]
        self.q_index = 0
        self.score = 0
        self.quiz_screen()

    def quiz_screen(self):
        self.clear_screen()
        if self.q_index >= len(self.questions):
            tk.Label(self.root, text=f"Quiz Over! Your Score: {self.score}/{len(self.questions)}", font=('Arial', 16)).pack(pady=20)
            tk.Button(self.root, text="Back to Main Menu", command=self.main_screen).pack(pady=10)
            return

        q = self.questions[self.q_index]
        tk.Label(self.root, text=f"Q{self.q_index + 1}: {q.question}", font=('Arial', 14), wraplength=500).pack(pady=10)
        self.selected_option = tk.StringVar()
        for opt in q.options:
            tk.Radiobutton(self.root, text=opt, variable=self.selected_option, value=opt).pack(anchor='w', padx=20)
        tk.Button(self.root, text="Submit Answer", command=self.submit_answer).pack(pady=10)

    def submit_answer(self):
        selected = self.selected_option.get()
        if not selected:
            messagebox.showwarning("Warning", "Please select an answer")
            return
        correct = self.questions[self.q_index].check_answer(selected)
        if correct:
            self.score += 1
            messagebox.showinfo("Correct", "That's correct!")
        else:
            messagebox.showinfo("Incorrect", f"Wrong! The correct answer was: {self.questions[self.q_index].answer}")
        self.q_index += 1
        self.quiz_screen()

# ---------------------- START APP ---------------------- #
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x600")
    app = QuizBowlApp(root)
    root.mainloop()
