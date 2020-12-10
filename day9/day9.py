from copy import deepcopy
import itertools
# brute force means of producing sum of two numbers
def two_of_five(numbers):
    result = []
    j = 0
    the_copy = deepcopy(numbers)
    iterations = len(the_copy)
    while j < iterations: 
        i =0
        a = the_copy.pop(0)
        while i < len(the_copy):
            result.append(a + the_copy[i])
            i += 1
        j += 1
    return result

# alternate means of producing sum of two numbers
def combo(numbers):
    result = []
    for c in itertools.combinations(numbers, 2):
        result.append(c[0] + c[1])
    return result

def unit_test_sum_of_any_two(actual):
    expected = [55,50,60,82, 35,45,67,40,62,72]
    for i, n in enumerate(expected):
        if expected[i] != actual[i]:
            print(f'e: {expected[i]}')
            print(f'a: {actual[i]}')
            break

def part1(input):
    ptr = 25
    # unit_test_sum_of_any_two(input[ptr-5:ptr])
    while True:
        if input[ptr] not in combo(input[ptr-25:ptr]):
            print(f'part1: {input[ptr]}')
            break
        ptr += 1

def part2(input):
    # 128499090 is too low
    # 133664652 is too low
    # 171265123
    # 1212510616 is too high
    part1_answer = 1212510616
    a = 0
    b = 0
    while True:
        if sum(input[a:b]) != part1_answer and b < len(input):
            b += 1
        elif sum(input[a:b]) == part1_answer:
            print(f'sum: {sum(input[a:b])}')
            print(f'min:{min(input[a:b])} + max:{max(input[a:b])} = {min(input[a:b])+max(input[a:b])}')
            break
        else:
            a = a+1
            b = a
            print(a)
        

with open("./input.txt", "r") as f:
    input = [int(line.rstrip()) for line in f]

part1(input)
part2(input)
# part 1 : 1212510616