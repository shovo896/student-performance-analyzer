 Smart Student Performance Simulator and Analyzer

A Python desktop application that simulates a virtual classroom, generates synthetic student data using NumPy, analyzes academic performance using Pandas, visualizes insights using Matplotlib, and provides an interactive GUI with Tkinter. All data is internally generated — no external CSV files required.


1. Features

-  Generate a virtual class of students with random names, scores, and attendance
-  View GPA distributions, subject averages, and attendance vs GPA scatter plots
-  Identify top performers and failed students
-  Search students by ID or name
- GUI built using Python's Tkinter library
-  Completely offline, no external data files needed


2. Tech Stack
-Python 3.9+
- NumPy – Data generation
-Pandas – Data analysis
-Matplotlib – Data visualization
-Tkinter – GUI framework


 Folder Structure


student_performance_analyzer
 * main.py               # App entry point
 *gui.py                # Tkinter-based interface
 * data_generator.py     # Student data generator (randomized)
 * analyzer.py           # Performance analysis functions
 * visualizer.py         # Matplotlib-based charts
 * student_utils.py      # Random name generator

 Installation

 1. Clone the repo:
bash
git clone https://github.com/shovo896/student-performance-analyzer.git
cd student-performance-analyzer
 2. Install dependencies:

bash
pip install numpy pandas matplotlib

>`tkinter` is usually pre-installed with Python. If not:
>
>  Windows/Linux: Already included
>  macOS: `brew install python-tk`



 Run the App

bash
python main.py

 Future Improvements

* Export data to CSV or Excel
* Add semester-wise performance tracking
* Predict GPA using machine learning
* Role-based login for students and teachers

 License

This project is licensed under the MIT License.
 
 
 
 
 Author

Ahadul Haque Shovo
Avionics, Aviation and Aerospace University



