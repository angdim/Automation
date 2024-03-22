class_diary = {}
total_grade = 0
student = input('Enter student\'s name and their grade in this format "Name:grade". Enter "end" for ending: ')

while student != 'end':
    st = student.split(':')
    class_diary[st[0]] = int(st[1])
    total_grade += int(st[1])
    student = input('Enter next student: ')

print(f'The average class grade is: {total_grade/len(class_diary):.2f}')
