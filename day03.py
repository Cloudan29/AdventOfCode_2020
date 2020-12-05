inp = open("inputs/day03.txt")
slope = []

for line in inp:
    slope.append(line.strip())


def part1():
    num_trees = 0
    width = 0
    height = 0
    mod_number = len(slope[0])

    while height < len(slope) - 1:
        width = (width + 3) % mod_number
        height += 1

        if slope[height][width] == '#':
            num_trees += 1
    
    return num_trees

def part2():

    num_trees = [0, 0, 0, 0, 0]
    path_number = -1
    slope_paths = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    mod_number = len(slope[0])

    for slope_path in slope_paths:
        path_number += 1
        width = 0
        height = 0

        while height < len(slope) - 1:
            width = (width + slope_path[0]) % mod_number
            height += slope_path[1]

            if slope[height][width] == '#':
                num_trees[path_number] += 1

    answer = 1
    for tree_count in num_trees:
        answer *= tree_count
        
    return answer




print(part1())
print(part2())