# by import
import greetings
print(greetings.say_hello("Abi"))
print(greetings.say_bye("Abi"))

#by specific import
from greetings import say_hello ,say_bye
print(say_hello("Abi"))
print(say_bye("Abi"))

#by alias name
from greetings import say_hello as hello ,say_bye as bye
print(hello("Abi"))
print(bye("Abi"))