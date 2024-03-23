class Student:
    def __init__(self, first_name:str, last_name:str, student_id:int, age:str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.age = age

class StudentManagement(Student):
    def __init__(self):
        self.Students = []

    def accept(self, student:Student):
        for st in self.Students:
            if st.student_id == student.student_id:
                print(f'Student with ID {st.student_id} already exists')
            else:
                self.Students.append(student)

    def display(self, id):
        st = self.search(id)
        if st:
            print(f'{st.first_name} {st.last_name} is {st.age}-years old and has an ID of {st.student_id}.')

    def search(self, id):
         for st in self.Students:
            if st.student_id == id:
                 return st
            else:
                 print(f'Student with ID {id} does not exist.')

    def delete(self, id):
        st = self.search(id)
        if st:
            self.Students.remove(st)

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