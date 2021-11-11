# 3.7:  11/10/21

guest_list = ["Barack Obama", "Bob Marley", "JFK", "Hugh Masekela"]

print("We've found a bigger table so more guests are on the way!")

guest_list.remove("JFK")

guest_list.insert(2, "Frida Khalo")
guest_list.insert(0, "Ghengis Khan")
guest_list.insert(3, "Queen Liliuokalani")
guest_list.append("Mother Mary")

for guest in guest_list: 
	print(f'Would you like to come to dinner {guest}?')

print("No only (2) people can come to dinner. :(")

while len(guest_list) > 2:
	print(f'Sorry, {guest_list.pop()}, but we are not able to invite you. :(')

for remaining_guest in range(len(guest_list)): 
	del guest_list[remaining_guest - 1]

print(guest_list)