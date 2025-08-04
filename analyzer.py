def get_top_students(df, n=10):
    return df.sort_values(by='GPA', ascending=False).head(n)

def get_failed_students(df):
    return df[df['Status'] == 'Fail']

def get_student_by_id(df, student_id):
    return df[df['ID'] == student_id]

def get_student_by_name(df, name):
    return df[df['Name'].str.contains(name, case=False)]