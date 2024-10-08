import random
numbers = [1, 2, 3]

new_numbers = [n+1 for n in numbers]

name = "Amelia"
letters_list = [letter for letter in name]

num = range(1,5)
new_num = [n *2 for n in range(1, 5)]

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
long_name = [name.upper() for name in names if len(name)>5]

# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value}

students_scores = {student:random.randint(1, 100) for student in names}

passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}

student_dict = {
    "student": ["Angela", "james", "lily" ],
    "score":[56,78,90]
}

for (key,value) in student_dict.items():
    print(value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for (index, row) in student_data_frame.inerrows():
    if row.student =="Angela"