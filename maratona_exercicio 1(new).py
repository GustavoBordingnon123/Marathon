names_and_notes_of_the_students = []
studensts_names = 'students'
failed_student = "fail_student9" 
early_student = '9'
note = '9'

print()
total_of_students = int(input("the total of students in the class is: "))
print()

while total_of_students > 100 or total_of_students < 1:
    total_of_students = int(input("invalid number, please digit on number in range 1 - 100: "))
for contador in range(total_of_students):
    names_and_notes_of_the_students.append(input("please, digit the name of one student and after, how many exercises he did: "))
    studensts_names = names_and_notes_of_the_students[contador] 
    while len(studensts_names) > 30 or len(studensts_names) < 1:
        names_and_notes_of_the_students[contador] = (input("invalid number, digit the name of one student and after, how many exercises he did: "))
        studensts_names = names_and_notes_of_the_students

for cont in range(total_of_students):
    for cont2 in range(total_of_students):
        early_student = note
        alunox = names_and_notes_of_the_students[cont]
        tamanho = len(alunox) - 1
        note = (alunox[tamanho])
        if note == '0':
            tamanho = len(alunox) - 2
            note = (alunox[tamanho])
            if note == '1': 
                note = '9'
        elif note > early_student:
            note = early_student
        elif note < early_student: 
            failed_student = alunox
        elif note == early_student:
            if failed_student < alunox:
                failed_student = alunox

print()
print("the student that failed is", failed_student[0:len(failed_student)-2])
