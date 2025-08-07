
#activity_06

from greeter import personal_greet
name=input("Enter the your name:")
print(personal_greet(name))


 #activity_04:
# #greeter.py

# def personal_greet(name):
#     print(f"Hello {name}")

# if __name__ == "__main__":
#     user_name = input("Enter your name:")
#     personal_greet(user_name)


# This checks if the script is being run directly (not imported as a module). =>if __name__ == "__main__":

# if i imported
# from greeter import personal_greet
# personal_greet("sathya")

# =>it asks to "Enter your name" in main.py if we use if __name__ == "__main__": it does not ask

# def personal_greet(name):
#     print(f"Hello {name}")
# user_name = input("Enter your name:")
# personal_greet(user_name)