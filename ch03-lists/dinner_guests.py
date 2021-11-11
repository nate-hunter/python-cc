# 3.9:  11/10/21 

guest_list = ["Barack Obama", "Bob Marley", "JFK", "Hugh Masekela"]

print(f'Current Guest List: {len(guest_list)}')

print("We've found a bigger table so more guests are on the way!")

guest_list.remove("JFK")
print(f'Current Guest List: {len(guest_list)}')

guest_list.insert(2, "Frida Khalo")
print(f'Current Guest List: {len(guest_list)}')
guest_list.insert(0, "Ghengis Khan")
print(f'Current Guest List: {len(guest_list)}')
guest_list.insert(3, "Queen Liliuokalani")
print(f'Current Guest List: {len(guest_list)}')
guest_list.append("Mother Mary")
print(f'Current Guest List: {len(guest_list)}')

for guest in guest_list: 
	print(f'Would you like to come to dinner {guest}?')