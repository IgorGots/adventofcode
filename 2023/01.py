from aocd import get_data


DIGITS_MAP = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def get_digit(s: str) -> str:

    if s[0].isdigit():
        return int(s[0])

    d = next(filter(s.startswith, DIGITS_MAP), None)
    return DIGITS_MAP.get(d, 0)


sum1 = sum2 = 0

for line in get_data(day=1, year=2023).split('\n'):

    # task1
    sum1 += 10 * int(next(filter(str.isdigit, line)))
    sum1 += int(next(filter(str.isdigit, line[::-1])))

    # task2
    for i in range(len(line)):
        num1 = get_digit(line[i:])
        if num1:
            break
    for i in range(len(line) - 1, -1, -1):
        num2 = get_digit(line[i:])
        if num2:
            break

    sum2 += 10*num1 + num2


print(f'Task1: {sum1}')
print(f'Task2: {sum2}')
