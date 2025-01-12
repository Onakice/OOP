class Student:
    def __init__(self, student_id, student_name, student_year):
        self.student_id = student_id
        self.student_name = student_name
        self.student_year = student_year
        self.student_menter = None

    def add_menter(self, menter):
        self.student_menter = menter
        
def find_menter(student_id, student_list):
    menter_list = []
    for student in student_list:
        if student.student_id == student_id:
            cur = student.student_menter
    while cur!=None:
        menter_list.append(cur.student_name)
        cur = cur.student_menter
    return menter_list

def CheckMenter(student_id1,student_id2):
    for student in student_list:
        if student.student_id == student_id1:
            ID1 = student.student_name
        if student.student_id == student_id2:
            ID2 = student.student_name
    if ID2 in find_menter(student_id1, student_list) or ID1 in find_menter(student_id2, student_list):
        return True
    else:
        return False

stu1 = Student('66011428', 'A', '1')
stu2 = Student('65010428', 'B', '2')
stu3 = Student('64009428', 'C', '3')
stu4 = Student('63008428', 'D', '4')

student_list = [stu1, stu2, stu3, stu4]

stu1.add_menter(stu2)
stu2.add_menter(stu3)
stu3.add_menter(stu4)

print(find_menter('66011428',student_list))
print(CheckMenter('66011428','65010428'))
print(find_menter('64009428',student_list))