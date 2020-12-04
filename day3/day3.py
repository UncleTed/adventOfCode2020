grid = []
with open("./input.txt", "r") as f:
    for line in f:
        grid.append(list(line.rstrip()))

def make_forest_csv():
    with open("./short.txt", "r") as f:
        for line in f:
            print(','.join(line.rstrip()))



def toboggan(right, down):
    trees = 0
    for index, row in enumerate(grid):
        length_of_row = len(row)
        c = (index * right) % length_of_row
        if row[c] == '#':
            trees = trees + 1
    print(f'Right {right}, down {down}: {trees}')

def part1():
    toboggan(3, 1)
    

def part2():
    toboggan(1,1)
    toboggan(3,1)
    toboggan(5,1)
    toboggan(7,1)


part1()
part2()
#make_forest_csv()