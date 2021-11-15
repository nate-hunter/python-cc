# 5.11:  11/15/21


numbers = list(range(1,10))
# numbers = list(range(1,40))

if numbers:
	for n in numbers:
		right_num = int(str(n)[-1])
		if right_num == 1:
			print(f'{n}st')
		elif right_num == 2:
			print(f'{n}nd')
		elif right_num == 3:
			print(f'{n}rd')
		else:
			print(f'{n}th') 
else:
	print('There are number to analyze.')
