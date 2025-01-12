class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

class Subject:
    def __init__(self, subject_id, subject_name, section, credit):
        self.subject_id = subject_id
        self.subject_name = subject_name
        self.section = section
        self.credit = credit

class Teacher:
    def __init__(self, teacher_id, teacher_name):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name

# def FindStudent(teacher_id):
#     for subject in [sub1, sub2]:
#         if subject.teacher.teacher_id == teacher_id:
#             return [student.student_name for student in subject.student]
        
def FindStudent(teacher_id):
    Student_List = []
    for subject in [sub1, sub2]:
        if subject.teacher.teacher_id == teacher_id:
            for student in subject.student:
                Student_List.append(student.student_name)
                # Student_List.append(subject.student)
    return Student_List

def FindSubject(student_id):
    Subject_List = []
    for subject in [sub1, sub2]:
        if student_id in [student.student_id for student in subject.student]:
            Subject_List.append(subject.subject_name)
            Subject_List.append(subject.section)
    return Subject_List

stu1 = Student('001', 'A')
stu2 = Student('002', 'B')
stu3 = Student('003', 'C')
stu4 = Student('004', 'D')
stu5 = Student('005', 'E')

teacher1 = Teacher('T001', 'ICE')
teacher2 = Teacher('T002', 'IKKYU')

sub1 = Subject('OOP101', 'object oriented programming', 'Section1', 3)
sub2 = Subject('OOP102', 'object oriented programming', 'Section2', 3)

sub1.student = [stu1, stu2, stu3]
sub2.student = [stu2, stu4, stu5]

sub1.teacher = teacher1
sub2.teacher = teacher2

# print(sub1.teacher.teacher_name)
print(FindStudent('T001'))
print(FindSubject('002'))

# # ทดสอบการทำงาน
# print(stu1.student_name)  # ผลลัพธ์ควรเป็น 'A'
# print(teacher1.teacher_name)  # ผลลัพธ์ควรเป็น 'ICE'
# print(sub1.subject_name)  # ผลลัพธ์ควรเป็น 'Object Oriented Programming'
