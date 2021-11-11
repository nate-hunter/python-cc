# 3.6:  11/10/21

guest_list = ["Barack Obama", "Bob Marley", "JFK", "Hugh Masekela"]

print("We've found a bigger table so more guests are on the way!")

guest_list.remove("JFK")

guest_list.insert(2, "Frida Khalo")
guest_list.insert(0, "Ghengis Khan")
guest_list.insert(3, "Queen Liliuokalani")
guest_list.append("Mother Mary")

for guest in guest_list: 
	print(f'Would you like to come to dinner {guest}?')