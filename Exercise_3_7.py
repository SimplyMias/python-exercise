# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive
# in time for the dinner, and you have space for only two guests.



guest = ["Imaad","Musheer","arzim","sahil"]
# print(f"Hey {guest[0].title()}, I am inviting you for a dinner at my place.")
# print(f"Hey {guest[1].title()}, I am inviting you for a dinner at my place.")
# print(f"Hey {guest[2].title()}, I am inviting you for a dinner at my place.")
# print(f"Hey {guest[3].title()}, I am inviting you for a dinner at my place.")

guest[1] = "Hammad" #Modifying my guest list

print("Printing modified list ")
# Print a second set of invitation messages, one for each person who is still in your list.
# print(f"Hey {guest[0].title()}, I am inviting you for a dinner at my place.")
# print(f"Hey {guest[1].title()}, I am inviting you for a dinner at my place.")
# print(f"Hey {guest[2].title()}, I am inviting you for a dinner at my place.")
# print(f"Hey {guest[3].title()}, I am inviting you for a dinner at my place.")

# print("Hey guys I have found a bigger dinner table.")

# Use insert() to add one new guest to the beginning of your list
guest.insert(0,"Nidal")

# Use insert() to add one new guest to the middle of your list.
guest.insert(3,"Sarosh Alam")

# Use append() to add one new guest to the end of your list.
guest.append("Husain")

# Print a new set of invitation messages, one for each person in
# your list
# print(f"Hey {guest[0].title()}, I’d love to invite you for dinner—are you free? ")
# print(f"Hey {guest[1].title()}, I’d love to invite you for dinner—are you free? ")
# print(f"Hey {guest[2].title()}, I’d love to invite you for dinner—are you free? ")
# print(f"Hey {guest[3].title()}, I’d love to invite you for dinner—are you free? ")
# print(f"Hey {guest[4].title()}, I’d love to invite you for dinner—are you free? ")
# print(f"Hey {guest[5].title()}, I’d love to invite you for dinner—are you free? ")
# print(f"Hey {guest[6].title()}, I’d love to invite you for dinner—are you free? ")

# Start with your program from Exercise 3-6. Add a new line
# that prints a message saying that you can invite only two
# people for dinner.

print("Sorry guys I can invite only two people for dinner ")


# Use pop() to remove guests from your list one at a time until
# only two names remain in your list. Each time you pop a
# name from your list, print a message to that person letting
# them know you’re sorry you can’t invite them to dinner.
g1 = guest.pop()
print(f" I am Sorry {g1.title()} I can't invite you for dinner")
g2 = guest.pop()
print(f" I am Sorry {g2.title()} I can't invite you for dinner")
g3 = guest.pop()
print(f" I am Sorry {g3.title()} I can't invite you for dinner")
g4 = guest.pop()
print(f" I am Sorry {g4.title()} I can't invite you for dinner")
g5 = guest.pop()
print(f" I am Sorry {g5.title()} I can't invite you for dinner")

# Print a message to each of the two people still on your list,
# letting them know they’re still invited.
print(f"Don't worry {guest[0]} and {guest[1]} you're still invited....")

# Use del to remove the last two names from your list, so you
# have an empty list. Print your list to make sure you actually
# have an empty list at the end of your program.
del guest[0]
del guest[0]
print(guest)