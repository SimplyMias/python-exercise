# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner,
# so you need to send out a new set of invitations. You’ll have to think of someone else to
# invite
guest = ["Imaad","Musheer","arzim","sahil"]
print(f"Hey {guest[0].title()}, I am inviting you for a dinner at my place.")
print(f"Hey {guest[1].title()}, I am inviting you for a dinner at my place.")
print(f"Hey {guest[2].title()}, I am inviting you for a dinner at my place.")
print(f"Hey {guest[3].title()}, I am inviting you for a dinner at my place.")

#Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who
#can’t make it
print(f"{guest[1].title()} is not coming.")

# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
guest[1] = "Hammad" #Modifying my guest list

print("Printing modified list ")
# Print a second set of invitation messages, one for each person who is still in your list.
print(f"Hey {guest[0].title()}, I am inviting you for a dinner at my place.")
print(f"Hey {guest[1].title()}, I am inviting you for a dinner at my place.")
print(f"Hey {guest[2].title()}, I am inviting you for a dinner at my place.")
print(f"Hey {guest[3].title()}, I am inviting you for a dinner at my place.")
