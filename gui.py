import tkinter as tk
from tkinter import ttk, messagebox
from analyzer import get_top_students, get_failed_students, get_student_by_id, get_student_by_name
from visualizer import plot_gpa_distribution, plot_subject_averages, plot_attendance_vs_gpa
from data_generator import generate_student_data

class StudentAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Performance Analyzer")
        self.root.geometry("1000x600")
        self.data = generate_student_data()

        self.setup_gui()

    def setup_gui(self):
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Regenerate Data", command=self.regenerate).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Top Performers", command=self.show_top).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="Failed Students", command=self.show_failed).grid(row=0, column=2, padx=10)
        tk.Button(btn_frame, text="GPA Histogram", command=lambda: plot_gpa_distribution(self.data)).grid(row=0, column=3, padx=10)
        tk.Button(btn_frame, text="Subject Averages", command=lambda: plot_subject_averages(self.data)).grid(row=0, column=4, padx=10)
        tk.Button(btn_frame, text="Attendance vs GPA", command=lambda: plot_attendance_vs_gpa(self.data)).grid(row=0, column=5, padx=10)

        search_frame = tk.Frame(self.root)
        search_frame.pack()

        tk.Label(search_frame, text="Search by ID or Name:").pack(side=tk.LEFT)
        self.search_var = tk.StringVar()
        tk.Entry(search_frame, textvariable=self.search_var, width=30).pack(side=tk.LEFT)
        tk.Button(search_frame, text="Search", command=self.search_student).pack(side=tk.LEFT, padx=5)

        self.tree = ttk.Treeview(self.root, columns=list(self.data.columns), show='headings')
        for col in self.data.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor='center')
        self.tree.pack(expand=True, fill=tk.BOTH)

        self.update_table(self.data)

    def regenerate(self):
        self.data = generate_student_data()
        self.update_table(self.data)

    def show_top(self):
        self.update_table(get_top_students(self.data))

    def show_failed(self):
        self.update_table(get_failed_students(self.data))

    def search_student(self):
        keyword = self.search_var.get()
        if keyword.startswith("S"):
            result = get_student_by_id(self.data, keyword)
        else:
            result = get_student_by_name(self.data, keyword)

        if result.empty:
            messagebox.showinfo("Result", "No student found.")
        else:
            self.update_table(result)

    def update_table(self, data):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for _, row in data.iterrows():
            self.tree.insert('', 'end', values=list(row))