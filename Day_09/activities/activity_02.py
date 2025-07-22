
#get grade from user input name

#declaring dictionary
grades={
    "Anita" : 92,
    "Ravi" : 85,
    "Kiran" :76,
    "Zoya" :88
}

#user input
stud_name=input("Enter the student name : ")

#getting grade from name given by user ,if not print "Student not found".
print(grades.get(stud_name,"Student not found"))