from aocd import get_data, submit

YEAR = 2022
DAY = 2

TEST_MODE = True
TEST_DATA = '''zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'''
TEST_RES_A = 11
TEST_RES_B = 157


def parse_data(data):
    return data

def task_a(data):
    pass

def task_b(data):
    pass

if __name__ == "__main__":
    if TEST_MODE is True:
        data = TEST_DATA
    else:
        data = get_data(day=DAY, year=YEAR)

    parsed_data = parse_data(data)
    result_a = task_a(parsed_data)
    result_b = task_b(parsed_data)
    
    if TEST_MODE is True:
        if result_a == TEST_RES_A:
            print(f'Correct answer: {result_a}')
        else:
            print(f'Incorrect answer: {result_a}. Should be: {TEST_RES_A}')
        if result_a == TEST_RES_B:
            print(f'Correct answer: {result_b}')
        else:
            print(f'Incorrect answer: {result_b}. Should be: {TEST_RES_B}')
    else:
        submit(result_a, part='a', day=DAY, year=YEAR)
        submit(result_b, part='b', day=DAY, year=YEAR)

