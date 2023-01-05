from aocd import get_data, submit

YEAR = 2022
DAY = 8

TEST_MODE = True
TEST_DATA = '''30373
25512
65332
33549
35390'''
TEST_RES_A = 21
TEST_RES_B = 8


def parse_data(data):
    result = list()
    for line in data.split('\n'):
        result.append(list(line))

    return result

def task_a(data):
    visible_trees = 0
    for i in range(0,len(data[0])):
        for j in range(0, len(data)):
            if i == 0 or i==len(data[0])-1 or j == 0 or j == len(data) - 1:
                visible_trees += 1
            else:
                height = data[i][j]                
                if max(data[i][:j]) < height or max(data[i][j+1:]) < height:
                    visible_trees += 1
                else:
                    high_slice = list()
                    low_slice = list()
                    for k in range(0,i):
                        high_slice.append(data[k][j])
                    for k in range(i+1,len(data)):
                        low_slice.append(data[k][j])
                    if max(high_slice) < height or max(low_slice) < height:
                        visible_trees += 1
               
    return visible_trees

def task_b(data):
    max_score = 0
    for i in range(0,len(data[0])):
        for j in range(0, len(data)):
            height = data[i][j]
            # to left
            counter_left = 0
            for k in range(j,0,-1):
                if data[i][k] < height:
                    counter_left += 1
                elif data[i][k] == height:

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
        print(f'{result_a = }')
        print(f'{result_b = }')
        # submit(result_a, part='a', day=DAY, year=YEAR)
        # submit(result_b, part='b', day=DAY, year=YEAR)

