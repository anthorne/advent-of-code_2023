# Advent of Code 2023 - Day 2

part_one_max = {'red': 12, 'green': 13, 'blue': 14}

# data = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
#         "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
#         "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
#         "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
#         "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

data = []
file_obj = open('d2_input.txt')
for row in file_obj:
    data.append(row)
file_obj.close()

games = {}
for game in data:
    game_id = game.split(':')[0].strip()
    games[game_id] = {'id': int(game_id.split(' ')[1].strip()), 'red': 0, 'green': 0, 'blue': 0, 'part_one_possible': True}
    sets = game.split(':')[1].strip().split('; ')
    for game_set in sets:
        cubes = game_set.split(', ')
        for cube in cubes:
            count = int(cube.split(' ')[0].strip())
            color = cube.split(' ')[1].strip()
            if count > games[game_id][color]:
                games[game_id][color] = count
            if count > part_one_max[color]:
                games[game_id]['part_one_possible'] = False

# Part one
part_one_sum = 0
for game_id, game_info in games.items():
    if game_info.get('part_one_possible'):
        part_one_sum += int(game_info.get('id'))
print(' Part one - The sum of the game IDs is: ' + str(part_one_sum))

# Part two
part_two_sum = 0
for game_id, game_info in games.items():
    power = game_info.get('red') * game_info.get('blue') * game_info.get('green')
    part_two_sum += power
print(' Part two - The sum of the power of the sets is: ' + str(part_two_sum))

