# if True and True and False:
# 	print('yo')
# else:
# 	print('nope')

some_list = []

keep_going = True

while keep_going: 
	if some_list:
		for item in some_list:
			print('item: ', item)
	else:
		user_input = input('what do you want to add: ')
		some_list.append(user_input) 
	keep_going = input("Keep going? True or False: ")