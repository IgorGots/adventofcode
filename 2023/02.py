from aocd import get_data
import re


def is_possible(sets: str) -> bool:

    limits = {'red': 12, 'green': 13, 'blue': 14}

    matches = re.findall(r'(\d+) (\w+)', sets)

    for match in matches:
        if int(match[0]) > limits[match[1]]:
            return False

    return True


def get_power(sets: str) -> int:

    red = green = blue = 0

    matches = re.findall(r'(\d+) (\w+)', sets)
    for match in matches:
        value = int(match[0])
        color = match[1]
        red = max(value, red) if color == 'red' else red
        green = max(value, green) if color == 'green' else green
        blue = max(value, blue) if color == 'blue' else blue

    return red * green * blue


answer1 = answer2 = 0

for line in get_data(day=2, year=2023).split('\n'):
    game, sets = line.split(':')

    answer1 += int(game[5:]) if is_possible(sets) else 0
    answer2 += get_power(sets)


print(f'Task1: {answer1}')
print(f'Task2: {answer2}')
