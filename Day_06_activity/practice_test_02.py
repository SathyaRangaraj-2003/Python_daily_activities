'''Take a string, remove all spaces, convert to uppercase, replace every 'A' with 'XXX', then extract characters at positions that are multiples of 3, and finally reverse the result.
 
input:
text = "amazing python language"
 
output:
"GNGXXXA"'''


text=input()  #user input

spaces=text.replace(" ","")  #removing all empty spaces in text input

upper_text=spaces.upper() #converting to upper case

replace_char=upper_text.replace('A','XXX') # replace 'A' with 'XXX'

print(replace_char[::3][::-1]) #extract every third character and reverse.

