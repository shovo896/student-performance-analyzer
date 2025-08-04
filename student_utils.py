# ------------------- student_utils.py -------------------
import random

def get_random_name():
    first_names = ['Ayaan', 'Nora', 'Liam', 'Maya', 'Ethan', 'Zara', 'Noah', 'Ava', 'Leo', 'Ella']
    last_names = ['Ahmed', 'Chowdhury', 'Khan', 'Rahman', 'Haque', 'Islam', 'Kabir', 'Hasan', 'Morshed']
    return f"{random.choice(first_names)} {random.choice(last_names)}"

