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
            return

    def display(self, st_id):
        st = self.search(st_id)
        if st:
            print(f'{st.first_name} {st.last_name} is {st.age}-years old and has an ID of {st.student_id}.')
        return

    def search(self, id):
        for st in self.students:
            if st.student_id == id:
                 return st
            else:
                 print(f'Student with ID {id} does not exist.')
                 return

    def delete(self, id):
        st = self.search(id)
        if st:
            self.students.remove(st)
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