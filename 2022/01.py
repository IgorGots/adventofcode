from aocd import get_data, submit

YEAR = 2022
DAY = 1


def parse_data(data):
    """ Parse data

    Args:
        data (str): string with calories

    Returns:
        dict: {elf_num: list_of_numbers}
    """
    elfs = {}

    elf_num = 0
    elfs[elf_num] = []
    for _line in data.split('\n'):
        if len(_line) == 0:
            elf_num += 1
            elfs[elf_num] = []
        else:
            elfs[elf_num].append(int(_line))

    return elfs


def search_highloaded_elf(elfs):
    """ Search for most loaded elf

    Args:
        elfs (dict[list]): elfs with calories

    Returns:
        int: higest load
    """
    
    var = 2

    if var == 1:
        _max = None
        for elf_num, elf_load in elfs.items():
            if _max is None or sum(elf_load) > _max:
                _max = sum(elf_load)
        return _max
    elif var == 2:
        return(
            max(
                [sum(value) for _, value in elfs.items()]
            )
        )

if __name__ == "__main__":
    data = get_data(day=DAY, year=YEAR)
    elfs = parse_data(data)
    heavy_elf = search_highloaded_elf(elfs)
    print(heavy_elf)
    # submit(heavy_elf, day=DAY, year=YEAR)
