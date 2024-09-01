student_scores={
    'Harry': 88,
    'Ron': 75,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

print(student_scores)

student_grades={}

for key in student_scores:
    if student_scores[key]>=71 and student_scores[key]<=80:
        student_grades[key]="Acceptable"
    elif student_scores[key]>=81 and student_scores[key]<=90:
        student_grades[key]="Exceeds Expectations"
    elif student_scores[key]>=91 and student_scores[key]<=100:
        student_grades[key]="Outstanding"
    else:
        student_grades[key]="Fail"

print(student_grades)
    