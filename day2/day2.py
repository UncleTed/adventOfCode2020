

def make_range(s):
    (l, r) = s.split('-')
    return (int(l),int(r))

def split_the_line(line):
    the_range = make_range(line.split(' ')[0])
    target_character = line.split(' ')[1].rstrip(':')
    password = line.split(' ')[2]
    return (the_range, target_character, password)


def count_characters(r,target,password):
    counter = 0
    for p in password:
        if p == target:
            counter = counter +1
        
    if counter >= r[0] and counter <= r[1]:
        return 1
    else:
        return 0

# 10-11 w: wwwwwtwwwwww
# 517
def part1():    
    total = 0
    with open("./input.txt", "r") as f:
        for line in f:
            (the_range, target_character, password) = split_the_line(line)
            total += count_characters(the_range, target_character, password)

    print(f'part 1: {total}')

#1-3 a: abcde is valid: position 1 contains a and position 3 does not.
def part2():
    total = 0
    with open("./input.txt", "r") as f:
        for line in f:
            (the_range, target_character, password) = split_the_line(line)
            first_char_matches = list(password)[the_range[0]-1] == target_character
            second_char_matches = list(password)[the_range[1]-1] == target_character
            if first_char_matches ^ second_char_matches:
                total = total +1

    print(f'part 2: {total}')

part1()
part2()