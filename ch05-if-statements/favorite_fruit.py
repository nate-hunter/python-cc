# 5.7:  11/12/21

fruits = ["watermelon", "apple", "mango", "pineapple", "orange", "banana"]

if "watermelon" in fruits:
	print("I like watermelon.")

favorite_fruits = fruits[:3]

user_input = input("Please name a fruit: ")

if user_input in favorite_fruits:
	print(f"You like {user_input}s!")

if "banana" in favorite_fruits:
	print("You like banana.")

if "apple" in favorite_fruits:
	print("You like apple.")

if "kiwi" in favorite_fruits:
	print("You like kiwi.")

if "pineapple" in favorite_fruits:
	print("You like pineaple.")

if "watermelon" in favorite_fruits:
	print("You like watermelon.")