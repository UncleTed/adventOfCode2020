import re
valid = ['hcl', 'iyr', 'pid', 'ecl', 'hgt','eyr', 'byr' ]

def check_passport_part1(buffer):
    passport = map(lambda x: x.split(':')[0], buffer.split(' '))
    for v in valid:
        if v not in passport:
            return False
    return True

def split_passport(buffer):
    dictionary = {}
    for fields in buffer.split(' '):
        if fields != '':
            f = fields.split(':')
            dictionary[f[0]] = f[1]
    return dictionary

def check_value(field, value):
    if field == 'byr':
        return int(value) >= 1920 and int(value) <= 2002
    if field == 'iyr':
        return int(value) >= 2010 and int(value) <= 2020
    if field == 'eyr':
        return int(value) >= 2020 and int(value) <= 2030
    if field == 'hgt':
        if 'cm' in value:
            h = value[:value.index('cm')]
            return int(h) >= 150 and int(h) <= 193
        if 'in' in value:
            h = value[:value.index('in')]
            return int(h) >= 59 and int(h) <= 76
        return False
    if field == 'hcl':
        return re.match("#[0-9a-f]{6}", value) != None
        
    if field == 'ecl':
        colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        return colors.count(value) == 1
    if field == 'pid':
            return re.match("\d{9}", value) != None



def check_passport_part2(passport):
    for v in valid:
        if not passport.has_key(v):
            return False
        if not check_value(v, passport.get(v)):
            return False
    return True

def part2():
    total = 0
    with open("input.txt", "r") as f:
        buffer = ''
        for line in f:
            if line != '\n':
                buffer = line.rstrip() + ' ' + buffer
            else:
                passport = split_passport(buffer)
                if check_passport_part2(passport):
                    total = total + 1
                buffer = ''
    print (total)


def part1():
    total = 0
    with open("input.txt", "r") as f:
        buffer = ''
        for line in f:
            if line != '\n':
                buffer = line.rstrip() + ' ' + buffer
            else:
                if check_passport_part1(buffer):
                    total = total + 1
                buffer = ''
    print (total)

#part1()
part2()