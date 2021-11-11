# 3.10:  11/10/21 

standings = ["Jazz", "Kings", "Blazers"]
print(standings)
standings.insert(0, "Warriors")
print(standings)
standings.append("Lakers")
standings.insert(2, "Clippers")
print(standings)
standings.insert(4, "Thunder")
print(standings)
del standings[-2]
print(standings)
standings.pop()
print(standings)
popped_team = standings.pop(1)
print('\tPopped team:', popped_team)
print(standings)
# clippers = standings.remove("Clippers")  => returns 'None'
# print(standings, clippers)

print(f'Sorted standings:', sorted(standings))
print(f'Sorted reversed standings:', sorted(standings, reverse=True))
print('Current standings:', standings)
standings.reverse()
print('Current standings:', standings)
standings.sort(reverse=True)
print('Alpha reversed standings:', standings)
standings.sort()
print('Alpha standings:', standings)