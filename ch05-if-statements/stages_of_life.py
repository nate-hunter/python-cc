# 5.6:  11/12/21


user_input = int(input("Please give a stage of life: "))


if user_input < 2:
	print("The person is a baby.")
elif user_input < 4:
	print("The person is a toddler.")
elif user_input < 13:
	print("The person is a kid.")
elif user_input < 20:
	print("The person is a teenager.")
elif user_input < 65:
	print("The person is an adult.")
elif user_input > 65:
	print("The person is an elder.")
else:
	print("Please enter a valid response...")

