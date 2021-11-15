# 5.10:  11/15/21


current_users = ['panda', 'Sake', 'Admin', 'litehouse', 'nhunter']

new_users = ['panda', 'sake', 'bubbles', 'logi', 'jazz']

if current_users and new_users:
	existing_users = [user.lower() for user in current_users]
	for new_user in new_users:
		if new_user in existing_users:
			print(f'The username \'{new_user}\' is already taken. Please enter a new username.')
		else:	
			print(f'The username \'{new_user}\' is available.')

else:
	print("There aren't any users in this application.")

