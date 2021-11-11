a_list = []

an_obj = { "name": "Panda Boogie"}
another_obj = { "name": "Rocky Balboa"}

a_list.append(an_obj)
a_list.append(another_obj)
a_list.append("Yo")
a_list.append([8, "mac", [3,2,1]])
a_list.append(24)

# for obj in a_list:
# 	print(obj, f'  |  Type of element:  {type(obj)}')

"""
# Works:
for obj in a_list: 
	print(obj['name'])

# Does not work:
for obj in a_list: 
	print(obj.'name')
"""

# standings = ["Jazz", "Kings", "Blazers"]
# print(standings)
# standings.insert(0, "Warriors")
# print(standings)
# standings.append("Lakers")
# standings.insert(2, "Clippers")
# print(standings)
# standings.insert(4, "Thunder")
# print(standings)
# del standings[-2]
# print(standings)
# standings.pop()
# print(standings)
# popped_team = standings.pop(1)
# print('\tPopped team:', popped_team)
# print(standings)
# # clippers = standings.remove("Clippers")  => returns 'None'
# print(standings, clippers)

# an_obj = { 3: "yo", 2: "yee", 5: "panda"}
# print(an_obj)
# # print(an_obj.sort()) => Does not work on dictionarys