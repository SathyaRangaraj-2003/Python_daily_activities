#activity 03

#declaring dictionary
students={
"Anita" : {"Math" : 95 , "Science" : 89},
"Ravi" : {"Math" : 80 , "Science" : 92},
"Pavi" : {"Math" : 88 , "Science" : 85}
}

#user inputs

stud_name = input("Enter the student name : ") 
sub_name = input("Enter the subject name : ")

#printing score for student and subject

print(students.get(stud_name,{}).get(sub_name,"Invalid input"))

