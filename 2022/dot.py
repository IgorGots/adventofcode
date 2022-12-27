from aocd import get_data, submit

YEAR = 2022
DAY = 2

TEST_MODE = True
TEST_DATA = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''
TEST_RES = 157


def parse_data(data):
    parsed_data = ''

    return parsed_data

def task_a(data):
    result = ''

    return result


if __name__ == "__main__":
    if TEST_MODE is True:
        data = TEST_DATA
    else:
        data = get_data(day=DAY, year=YEAR)

    parsed_data = parse_data(data)
    result_a = task_a(parsed_data)
    
    if TEST_MODE is True:
        if result_a == TEST_RES:
            print(f'Correct answer: {result_a}')
        else:
            print(f'Incorrect answer: {result_a}. Should be: {TEST_RES}')
    else:
        submit(result_a, part='a', day=DAY, year=YEAR)

