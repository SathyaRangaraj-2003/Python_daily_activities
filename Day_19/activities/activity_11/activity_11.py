
#activity_11:
try:
    with open("guests.txt", "r") as file:
        guests = file.readlines()
        print("Current guests:")
        for guest in guests:
            print(guest.strip())
except FileNotFoundError:
    print("No guest list found")
new_guest = input("Enter the name of the new guest: ")
with open("guests.txt", "a") as file:
    file.write(new_guest + "\n")
print(f"{new_guest} added to the guest list")