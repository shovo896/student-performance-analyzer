import matplotlib.pyplot as plt

def plot_gpa_distribution(df):
    plt.figure(figsize=(8, 5))
    plt.hist(df['GPA'], bins=10, color='skyblue', edgecolor='black')
    plt.title('GPA Distribution')
    plt.xlabel('GPA')
    plt.ylabel('Number of Students')
    plt.grid(True)
    plt.show()

def plot_subject_averages(df):
    subjects = ['Math', 'Physics', 'Programming']
    averages = df[subjects].mean()
    plt.bar(subjects, averages, color='green')
    plt.title('Average Subject Scores')
    plt.ylabel('Average Score')
    plt.show()

def plot_attendance_vs_gpa(df):
    plt.scatter(df['Attendance(%)'], df['GPA'], color='purple')
    plt.title('Attendance vs GPA')
    plt.xlabel('Attendance (%)')
    plt.ylabel('GPA')
    plt.grid(True)
    plt.show()
