

# v1 = 5
# v2 = 4
# add = v1+v2
# sub = v1-v2
# mul = v1*v2
# div = v1/v2
# print("Addition :",add)
# print("Subraction :",sub)
# print("Multiplication :",mul)


# #is this possible other user can access add,sub


# #datetime module

# import datetime
# print(datetime.datetime.now()) #2025-08-05 13:03:37.842840
# print(type(datetime.datetime.now())) #<class 'datetime.datetime'>

# from datetime import time,date
# t = time(13,45,95)
# print(t)  #13:45:20
# print(t.hour  , t.second)

# d =date(2001,5,3)
# print(d)

# from datetime import datetime
# now = datetime.now()
# print(now.day, now.month, now.year,sep="-")
# print(now.hour, now.minute, now.second)

# print(type(now))

# dt = datetime(2025, 12, 25, 17, 30)
# print(dt)

# file = open('day19.txt', 'r')
# content = file.read()
# print(content)








#  You have a list of students, each with a list of scores. Create a dictionary mapping the names of students who have an average score of 90 or higher to their average score.
# Concepts: nested list, list of dict, filter, map, lambda, dictionary comprehension.

# students = [ {"name": "Brenda", "scores": [90, 92, 95, 88]}, {"name": "David", "scores": [85, 87, 89]}, {"name": "Cathy", "scores": [98, 99, 100]}, {"name": "Alex", "scores": [70, 100]} ]

# avg_score = list(map(lambda  stud : (stud["name"], sum(stud["scores"])/len(stud["scores"])) ,students ))

# print(avg_score)

# print({name: round(score, 2)  for name, score in avg_score if score >= 90})


# def avg_score(scores):
#     return sum(scores) / len(scores) if scores else 0

# data = filter(lambda stud: avg_score(stud["scores"]) >= 90, students)

# print({student["name"]: round(avg_score(student["scores"]), 2) for student in data})


# #without lambda
# print( {
#     stud["name"] : sum(stud["scores"])/len(stud["scores"]) for stud in students if sum(stud["scores"])/len(stud["scores"]) >= 90
# })



# for stud in students:
#     print(stud)

# d = {
#     stud["name"] : stud["scores"] for stud in students
# }

# d={list(map(lambda  : sum(stud["scores"])/len(stud["scores"]) for stud in students))}
# print(list(sum(stud["scores"])/len(stud["scores"]) for stud in students))



