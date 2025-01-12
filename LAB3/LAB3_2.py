def add_score(subject_score, student, subject, score):
  if student in subject_score:
    subject_score[student].update({subject: score})
    return subject_score
  subject_score.update({student: {subject: score}})
  return subject_score

def calc_average_score(subject_score):
  return {student: "{:.2f}".format(sum(subject_score[student].values()) / len(subject_score[student])) for student in subject_score}

subject_score = {}
student1 = '65010001'
subject1 = 'python'
score1 = 50
subject_score = add_score(subject_score, student1, subject1, score1)
print(subject_score)

student2 = '65010002'
subject2 = 'calculus'
score2 = 60
subject_score = add_score(subject_score, student2, subject2, score2)
print(subject_score)

print(calc_average_score(subject_score))