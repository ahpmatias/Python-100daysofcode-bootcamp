import random
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']
# names_list = [name.upper() for name in names if len(name) > 4]
# print(names_list)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']

students_scores = {student:random.randint(1,100)  for student in names}

passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)
