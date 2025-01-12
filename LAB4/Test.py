class Student:
    id = ''
    name = ''

stu1 = Student()
stu1.id = '001'
stu1.name = "John"

stu2 = Student()
stu2.id = '002'
stu2.name = "Peter"

print(stu1.id)
print(stu1.name)
print(stu2.id)
print(stu2.name)

class StudentWithDef:
    def __init__(self, id, name):
        self.id = id
        self.name = name

stu11 = StudentWithDef('001', 'John')
stu22 = StudentWithDef('002', 'Peter')

print(stu11.id)
print(stu22.id)