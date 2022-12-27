from aocd import get_data, submit

YEAR = 2022
DAY = 4

TEST_MODE = False
TEST_DATA = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''
TEST_RES_A = 2
TEST_RES_B = 70


if TEST_MODE is False:
    TEST_DATA = get_data(day=DAY, year=YEAR)

overlap_ranges = 0
overlap_parts = 0
for line in TEST_DATA.split('\n'):
    sections = line.split(',')
    s1 = [int(i) for i in sections[0].split('-')]
    s2 = [int(i) for i in sections[1].split('-')]


    # overlap ranges
    if s1[0] >= s2[0] and s1[1] <= s2[1]:
        overlap_ranges += 1
    elif s2[0] >= s1[0] and s2[1] <= s1[1]:
        overlap_ranges += 1

    # overlap sections
    if len(
        set(range(s1[0], s1[1]+1)).intersection(range(s2[0], s2[1]+1))
    ) > 0:
        overlap_parts += 1



if TEST_MODE is False:
    submit(overlap_ranges, part='a', day=DAY, year=YEAR)
    submit(overlap_parts, part='b', day=DAY, year=YEAR)

print(overlap_ranges)
print(overlap_parts)
    