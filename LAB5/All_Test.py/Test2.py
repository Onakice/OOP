class Student:
    def __init__(self, stu_id, stu_name):
        self.__stu_id = stu_id
        self.__stu_name = stu_name
    
    def get_id(self):
        return self.__stu_id

    def set_id(self, stu_id):
        if stu_id.isnumeric() and len(stu_id) == 8:
            self.__stu_id = stu_id
        else:
            raise ValueError("Invalid ID")
        
class Subject:
    def __init__(self, subject_id, subject_name):
        self.sub_id = subject_id
        self.sub_name = subject_name
        self.student_list = []

    def add_student(self, student):
        if isinstance(student, Student):
            self.student_list.append(student)

    def add_student_list(self, student_list):
        for st in student_list:
            self.add_student(st)

student1 = Student('66010001', 'John')
student2 = Student('66010002', 'Peter')
print(student1.get_id())
student2.set_id('66010100')

subject1 = Subject('01076140', 'Calculus')
subject1.add_student(student2)

# print(subject1.student_list.student.get_id)
print(subject1)