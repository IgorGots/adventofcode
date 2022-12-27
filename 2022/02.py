from aocd import get_data, submit
from enum import IntEnum 

YEAR = 2022
DAY = 2

class Item(IntEnum):
    A = 1
    B = 2
    C = 3
    X = 1
    Y = 2
    Z = 3

    # @classmethod
    def winner(cls):        
        if cls.value == 3:
            return 1
        else:
            return cls.value + 1
    
    # @classmethod
    def loser(cls):
        if cls.value == 1:
            return 3
        else:
            return cls.value - 1 

    # @classmethod
    def draw(cls):
        return cls.value

    def __gt__(self, other):
        if self.value > other.value:
            if self.value != 3:
                return True
            elif self.value == 3:
                return False
            else:
                assert('Compare error')
        

        
        
        

def parse_data(data):
    """ Parse data

    Args:
        data (str): string with strategy

    Returns:
        list: list of list 
    """
    strategy = []

    for _line in data.split('\n'):
        elf, me = _line.split()
        strategy.append(
            {'elf': elf, 'me': me}
        )
        
    return strategy

def score(round):

    me = round['me']
    elf = round['elf']

    _score = Item[me].value

    if Item[me] == Item[elf]:
        _score += 3
    elif Item[me] > Item[elf]:       
        _score += 6
    
    elif Item[me] == 1 and Item[elf]==3:
        _score += 6
    
    return _score

def score1(round):
    target = round['me']
    elf = round['elf']

    if target == 'X':
        _score = 0 + Item[elf].loser()
    elif target == 'Y':
        _score = 3 + Item[elf].draw()
    elif target == 'Z':
        _score = 6 + Item[elf].winner()

    return _score

if __name__ == "__main__":
    data = get_data(day=DAY, year=YEAR)
    # data = "A Y\nB X\nC Z"
    strategy = parse_data(data)
    total_score = 0    
    for round in strategy:
        total_score += score(round)

    if total_score != 9759:
        print(f'Incorrect answer {total_score}')
    else:
        print(f'Answer1: {total_score}')
        # submit(total_score, part='a', day=DAY, year=YEAR)

    total_score1 = 0    
    for round in strategy:
        total_score1 += score1(round)

    if total_score1 != 12429:
        print(f'Incorrect answer {total_score}')
    else:
        print(f'Answer2: {total_score}')
        # submit(total_score, part='b', day=DAY, year=YEAR)