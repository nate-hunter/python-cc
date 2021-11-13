# 5.1:  11/11/21


team = "Warriors"
print('It is true... the \'team\' is the \'Warriors\'')
print(team.lower() == 'warriors')

print('It is \'NOT\' true... the \'team\' is the \'Knicks\'')
print(team.lower() == 'knicks')

warriors_score = 124 
warriors_city = "San Francisco"
nets_score = 109   
nets_city = "Brooklyn"
game_location = "Brooklyn"

print(f'\nThe Warriors won: {warriors_score > nets_score}')
print(f'\nThe Nets won: {warriors_score < nets_score}')
print(f'\nThe game was a tie: {warriors_score == nets_score}')
print(f'\nThe Warriors scored over 100 points: {warriors_score >= 100}')
print(f'\nThe Nets scored over 100 points: {nets_score >= 100}')
print(f'\nIt was a home game for the Warriors: {warriors_city == game_location}')
print(f'\nIt was a home game for the Nets: {nets_city == game_location}')
print(f'\nIt was a home game for either team: {warriors_city == game_location or nets_city == game_location}')
print(f'\nIt was a home game for neither team: {warriors_city != game_location and nets_city != game_location}')