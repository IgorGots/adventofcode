from aocd import get_data, submit
import parse

YEAR = 2022
DAY = 5

TEST_MODE = True
TEST_DATA = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''
TEST_RES_A = 'CMZ'
TEST_RES_B = 'MCD'


def parse_data(data):
    parsed_data = dict()
    in_stacks = True
    instructions = list()
    for line in data.split('\n'):
        len_line = len(line) + 1

        if len(parsed_data) == 0:
            for i in range(1,len_line//4+1):
                parsed_data[i] = []

        if len_line > 2 and in_stacks is True:
            stack = 1
            for i in range(1, len_line, 4):
                if 'A' <= line[i] <= 'Z':
                    parsed_data[stack].insert(0, line[i])
                stack += 1
        elif len(line) < 2 and in_stacks is True:
            in_stacks = False
        elif in_stacks is not True:
            PATTERN = parse.compile(
                "move {count:d} from {source:d} to {destination:d}"
            )
            match = PATTERN.search(line)
            instructions.append({'count': match['count'], 'source': match['source'], 'destination': match['destination']})

    return parsed_data, instructions

def task_a(data, instructions):
    for task in instructions:
        _buffer = data[task['source']][-task['count']:]
        del(data[task['source']][-task['count']:])
        _buffer.reverse()        
        data[task['destination']].extend(_buffer)

    result = ''
    for key, value in data.items():
        if len(value) > 0:
            result += value[-1]
    return result

def task_b(data, instructions):
    for task in instructions:
        _buffer = data[task['source']][-task['count']:]
        del(data[task['source']][-task['count']:])
        data[task['destination']].extend(_buffer)
    
    result = ''
    for key, value in data.items():
        if len(value) > 0:
            result += value[-1]
    return result    



if __name__ == "__main__":
    if TEST_MODE is True:
        data = TEST_DATA
    else:
        data = get_data(day=DAY, year=YEAR)

    parsed_data, instructions = parse_data(data)
    result_a = task_a(parsed_data, instructions)
    parsed_data, instructions = parse_data(data)
    result_b = task_b(parsed_data, instructions)
    
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

