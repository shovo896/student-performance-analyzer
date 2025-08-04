
import numpy as np
import pandas as pd
import random
from student_utils import get_random_name

def generate_student_data(num_students=100):
    ids = [f"S{1000 + i}" for i in range(num_students)]
    names = [get_random_name() for _ in range(num_students)]
    scores_math = np.random.randint(40, 100, num_students)
    scores_physics = np.random.randint(40, 100, num_students)
    scores_programming = np.random.randint(40, 100, num_students)
    attendance = np.random.randint(60, 100, num_students)

    df = pd.DataFrame({
        'ID': ids,
        'Name': names,
        'Math': scores_math,
        'Physics': scores_physics,
        'Programming': scores_programming,
        'Attendance(%)': attendance
    })

    df['Total'] = df[['Math', 'Physics', 'Programming']].sum(axis=1)
    df['GPA'] = df['Total'] / 30
    df['Grade'] = df['GPA'].apply(lambda g: 'A' if g >= 9 else ('B' if g >= 8 else ('C' if g >= 7 else 'F')))
    df['Status'] = df['Grade'].apply(lambda x: 'Pass' if x != 'F' else 'Fail')

    return df