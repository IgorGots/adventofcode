from aocd import get_data, submit
from pathlib import Path

YEAR = 2022
DAY = 7

TEST_MODE = False
TEST_DATA = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
dir none
8033020 d.log
5626152 d.ext
7214296 k'''


TEST_RES_A = 95437
TEST_RES_B = 24933642 # 23595140


def parse_data(data):
    # result_dict = dict()    
    result_dict = {'/':[]}
    current_path = Path()
    for line in data.split('\n'):
        if '$' in line:
        # command
            if 'cd' in line:
                _, _, directory = line.split(' ')
                if '..' in directory:
                    current_path = current_path.parent
                else:
                    current_path = current_path.joinpath(directory)

            elif 'ls' in line:
                pass
            else:
                assert 0, 'Unknown command'
        else: 
        # output
            if 'dir' in line:
                pass
            else:
                size, name = line.split()
                c_p = current_path
                while str(c_p) != current_path.root:
                    if str(c_p) not in result_dict:
                        result_dict[str(c_p)] = list()
                    result_dict[str(c_p)].append(int(size))
                    c_p = c_p.parent
                result_dict['/'].append(int(size))    
                
    return result_dict
                
        
def task_a(data):
    result = 0
    for key, value in data.items():
        if sum(value) < 100000:
            result += sum(value)
    
    return result

def task_b(data):
    need_to_free = 30_000_000 - (70_000_000 - sum(data['/']))
    for_delete = []
    for key, value in data.items():
        if sum(value) >= need_to_free:
            for_delete.append(sum(value))
        # else:
        #     print(f'{key:15} - {sum(value)}')
    
    return min(for_delete)


if __name__ == "__main__":
    if TEST_MODE is True:
        data = TEST_DATA
    else:
        data = get_data(day=DAY, year=YEAR)

    parsed_data = parse_data(data)
    # print(parsed_data)
    result_a = task_a(parsed_data)
    result_b = task_b(parsed_data)
    
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
        # submit(result_a, part='a', day=DAY, year=YEAR)
        # submit(result_b, part='b', day=DAY, year=YEAR)
        print(f'{result_b = } == 7268994')

