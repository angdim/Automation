diary = {}
def avg_grade(class_diary):
    avg = sum([student[1] for student in class_diary.items()])
    return print(f'The average grade of this class is: \
    {avg/len(class_diary):.2f}')


if __name__ == '__main__':
    student = input('Enter student and their grade in format \
    \"Name:grade\". For end enter \"end\": ')
    while student != 'end':
        name, grade = student.split(':')
        diary[name] = int(grade)
        student = input('Enter next student: ')

    avg_grade(diary)