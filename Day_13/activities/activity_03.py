#student score and assign grade and print message

score = int(input("Enter the student score :"))


if (score >= 90) :
	grade ='A'
	print("Excellent work!")
elif (score >= 80 and score <90):
	grade ='B'
	print('Good job!')
elif (score >= 70 and score <80):
	grade ='C'
	print("Satisfactory")
elif (score >= 60 and score <70):
	grade ='D'
	print("Needs improvement")
else:
	grade = 'F'
	print('Please study more')
	

# (1 dict , 1 if) => 25 grades =>1000 inputs

#by using dictionary
score = int(input("Enter the student score :"))
message={
    'A' : "Excellent work!",
    'B' : "Good job!",
    'C' : "Satisfactory",
    'D' : "Needs improvement",
    'F' : "Please study more"
}

if (score >= 90) :
	grade ='A'
elif (score >= 80 and score <90):
	grade ='B'
elif (score >= 70 and score <80):
	grade ='C'
elif (score >= 60 and score <70):
	grade ='D'
else:
	grade = 'F'
print(grade)
print(message[grade])

