
'''
You are the at Eagle Airbase. A severe sandstorm has damaged all computer tracking systems. Multiple fighter jets were sent on patrol missions this morning, but the storm is making radio communication difficult.
MISSION DATA:

Your ground crew chief provides you with handwritten flight logs:

601, 602, 603, 608, 612, 615, 618

601, 603, 608, 612, 615, 618


YOUR TASK:

Using the aircraft numbers provided and basic mathematical operations, determine which specific aircraft has not returned to base.
SYSTEM CONSTRAINTS:
Your emergency calculator can only do basic math operations
No advanced programming features available
Cannot use lists, loops, or complex functions
Must use only simple mathematical calculations
'''



# practice 01:

#inputs
A = 601, 602, 603, 608, 612, 615, 618

B = 601, 603, 608, 612, 615, 618

#operations
sumA = sum(A)
sumB = sum(B)


#result
print(abs(sumA - sumB))


# practice 02:

#inputs
A = {618, 615, 612, 608, 603, 601, 618, 615, 612, 608, 603, 602, 601}

#result
print(618 ^ 615 ^ 612 ^ 608 ^ 603 ^ 601 ^ 618 ^ 615 ^ 612 ^ 608 ^ 603 ^ 602^ 601)
