from aocd import get_data, submit

YEAR = 2022
DAY = 1

def parse_data(data):
    """ Parse data

    Args:
        data (str): string with calories

    Returns:
        dict: {elf_num: list_of_numbers}
    """    ''''''
    elfs = {}

    elf_num = 0
    elfs[elf_num] = []
    for _line in data.split('\n'):
        if len(_line) == 0:
            elf_num += 1
            elfs[elf_num] = []
            continue
        else:
            elfs[elf_num].append(int(_line))
        
    return elfs

def search_highloaded_elf(elfs):
    """ Search for most loaded elf

    Args:
        elfs (dict[list]): elfs with calories

    Returns:
        int: higest load
    """    ''''''

    max = 0
    for elf_num, elf_load in elfs.items():
        if sum(elf_load) > max:
            max = sum(elf_load)            

    return max


if __name__ == "__main__":
    data = get_data(day=DAY, year=YEAR)
    elfs = parse_data(data)
    heavy_elf = search_highloaded_elf(elfs)
    submit(heavy_elf, day=DAY, year=YEAR)
