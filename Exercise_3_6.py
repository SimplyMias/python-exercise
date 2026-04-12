# 3-6. More Guests: You just found a bigger dinner table, so now more space is available.
# Think of three more guests to invite to dinner.

# Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program informing
# people that you found a bigger dinner table.


guest = ["Imaad","Musheer","arzim","sahil"]
# print(f"Hey {guest[0].title()}, I am inviting you for a dinner at my place.")
# print(f"Hey {guest[1].title()}, I am inviting you for a dinner at my place.")
# print(f"Hey {guest[2].title()}, I am inviting you for a dinner at my place.")
# print(f"Hey {guest[3].title()}, I am inviting you for a dinner at my place.")

guest[1] = "Hammad" #Modifying my guest list

print("Printing modified list ")
# Print a second set of invitation messages, one for each person who is still in your list.
print(f"Hey {guest[0].title()}, I am inviting you for a dinner at my place.")
print(f"Hey {guest[1].title()}, I am inviting you for a dinner at my place.")
print(f"Hey {guest[2].title()}, I am inviting you for a dinner at my place.")
print(f"Hey {guest[3].title()}, I am inviting you for a dinner at my place.")

print("Hey guys I have found a bigger dinner table.")

# Use insert() to add one new guest to the beginning of your list
guest.insert(0,"Nidal")

# Use insert() to add one new guest to the middle of your list.
guest.insert(3,"Sarosh Alam")

# Use append() to add one new guest to the end of your list.
guest.append("Husain")

# Print a new set of invitation messages, one for each person in
# your list
print(f"Hey {guest[0].title()}, I’d love to invite you for dinner—are you free? ")
print(f"Hey {guest[1].title()}, I’d love to invite you for dinner—are you free? ")
print(f"Hey {guest[2].title()}, I’d love to invite you for dinner—are you free? ")
print(f"Hey {guest[3].title()}, I’d love to invite you for dinner—are you free? ")
print(f"Hey {guest[4].title()}, I’d love to invite you for dinner—are you free? ")
print(f"Hey {guest[5].title()}, I’d love to invite you for dinner—are you free? ")
print(f"Hey {guest[6].title()}, I’d love to invite you for dinner—are you free? ")
