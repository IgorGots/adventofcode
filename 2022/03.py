from aocd import get_data, submit

YEAR = 2022
DAY = 3

TEST_MODE = False
TEST_DATA = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''
TEST_RES_A = 157
TEST_RES_B = 70

def elf_ord(symbol):
    if ord(symbol) >= 97:
        return ord(symbol) - 96
    else:
        return ord(symbol) - 38
    



def parse_data(data):
    parsed_data = []
    for line in data.split('\n'):
        # comp1, comp2 = [data[:len(data)/2], data[len(data/2):]]        
        parsed_data.append(
            [ line[:len(line)//2], line[len(line)//2:] ]
        )

    return parsed_data

def task_a(data):
    sum = 0
    for backpack in data:
        same_symbols = set(backpack[0]).intersection(backpack[1])
        for symbol in same_symbols:
            sum += elf_ord(symbol)

    return sum

def task_b(data):
    sum = 0

    parsed_data = data.split('\n')

    for step in range(0, len(parsed_data)-2, 3):
        same_symbols_1 = set(parsed_data[step]).intersection(parsed_data[step+1])
        same_symbols = set(same_symbols_1.intersection(parsed_data[step+2]))
        for symbol in same_symbols:
            sum += elf_ord(symbol)
    return sum


if __name__ == "__main__":
    if TEST_MODE is True:
        data = TEST_DATA
    else:
        data = get_data(day=DAY, year=YEAR)

    parsed_data = parse_data(data)
    result_a = task_a(parsed_data)
    result_b = task_b(data)
    
    if TEST_MODE is True:
        if result_a == TEST_RES_A:
            print(f'Correct answer: {result_a}')
        else:
            print(f'Incorrect answer: {result_a}. Should be: {TEST_RES_A}')
        if result_b == TEST_RES_B:
            print(f'Correct answer: {result_b}')
        else:
            print(f'Incorrect answer: {result_b}. Should be: {TEST_RES_B}')


    else:
        submit(result_a, part='a', day=DAY, year=YEAR)
        submit(result_b, part='b', day=DAY, year=YEAR)

