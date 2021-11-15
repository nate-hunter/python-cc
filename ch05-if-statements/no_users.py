# 5.9:  11/15/21


# usernames = ['panda', 'sake', 'admin', 'litehouse', 'nhunter']
usernames = []

if usernames:
	for username in usernames:
		if username == 'admin':
			print(f'Hello admin, would you like to see a status report?')
		else: 
			print(f'Welcome {username}!')
else:
	print('We need to find some users!')