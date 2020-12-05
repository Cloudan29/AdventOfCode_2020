inp = open("inputs/day04.txt")

def is_valid_passport(passport_keys, needed_keys):
    if (not 'cid' in passport_keys and len(passport_keys) == len(needed_keys)) or (len(passport_keys) == len(needed_keys) + 1):
        return True

def part1():
    num_valid = 0
    needed_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    seen = []

    for line in inp:
        if line == '\n':
            if is_valid_passport(seen, needed_keys):
                num_valid += 1

            seen = []
            continue

        keyval_pairs = line.split(' ')
        for keyval in keyval_pairs:
            seen.append(keyval.split(':')[0])

    # Off by one
    if is_valid_passport(seen, needed_keys):
        num_valid += 1

    seen = []
    return num_valid




print(part1())

