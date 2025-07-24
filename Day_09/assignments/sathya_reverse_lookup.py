#dictionary with student names and marks
scores = {
    "Anita": 92,
    "Ravi": 85,
    "Kiran": 76,
    "Zoya": 88,
}
#user input
user_score = int(input("Enter score:"))

#process
d1=dict(zip(scores.values(),scores.keys()))

#printing 1st student
print(d1.get(user_score,"Not found"))