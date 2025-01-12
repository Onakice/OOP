# def add_score(subject_score, subject, score):
#   subject_score.update({subject: score})
#   return subject_score


# def calc_average_score(subject_score):
#   return "{:.2f}".format(sum(subject_score.values()) / len(subject_score))

def add_score(subject_score, subject, score):
    subject_score.update({subject: score})
    return subject_score

def calc_average_score(subject_score):
    return "{:.2f}".format(sum(subject_score.values()) / len(subject_score))

dic = {}
print(add_score(dic, 'python', 50))
print(add_score(dic, 'C', 60))
print(calc_average_score(dic))