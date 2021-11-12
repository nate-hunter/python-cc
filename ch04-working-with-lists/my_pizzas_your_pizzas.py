# 4.11:  11/11/21


pizzas = ['pepperoni', 'buffalo chicken ranch', 'mushroom and olive']
friend_pizzas = pizzas[:]

pizzas.append('combination')
friend_pizzas.append('cheese')

print('\nMy favorite pizzas are:')
for pizza in pizzas:
	print(f'- {pizza.title()}')

print('\nMy friend\'s favorite pizzas are:')
for pizza in friend_pizzas:
	print(f'- {pizza.title()}')

