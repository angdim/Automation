class Student:
    def __init__(self, first_name:str, last_name:str, student_id:int, age:str):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.age = age

class StudentManagement(Student):
    def __init__(self):
        self.students = []

    def accept(self, student:Student):
        if self.search(student.student_id):
            print(f'Student with ID {student.student_id} already exists')
        else:
            self.students.append(student)
            '''The following command is added to bring more clarity of what's going on behind the scenes'''
            print(f'Student {student.first_name} {student.last_name} with ID {student.student_id} is added.')
            return

    def display(self, st_id):
        if self.search(st_id):
            st = self.search(st_id)
            print(f'{st.first_name} {st.last_name} is {st.age}-years old and has an ID of {st.student_id}.')
            return
        else:
            print(f'Student with ID {st_id} does not exist.')
            return

    def search(self, id):
        for st in self.students:
            if st.student_id == id:
                return st
        return False

    def delete(self, id):
        if self.search(id):
            self.students.remove(self.search(id))
            print(f'Student with ID {id} is removed.')
            return
        else:
            print(f'Student with ID {id} does not exist.')
            return

if __name__ == "__main__":
    student1 = Student("John", "Doe", 1, 18)
    student2 = Student("Peter", "Oswell", 1, 15)
    student3 = Student("Lilliam", "Pumpernickle", 2, 22)

    student_management = StudentManagement()
    student_management.accept(student1)
    student_management.accept(student2)
    student_management.accept(student3)
    student_management.display(3)
    student_management.display(2)
    student_management.delete(1)
    student_management.display(1)