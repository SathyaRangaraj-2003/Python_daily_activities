#activity_06:

#armstrong number
num = int(input("Enter the number: "))
len_num = len(str(num))

temp = num
sum=0
while(num > 0):
	digit = num % 10
	sum += int(digit ** len_num)
	num = num // 10
print(temp == sum)