grid = []
with open("./short.txt", "r") as f:
    for line in f:
        grid.append(list(line.rstrip()))

def make_forest_csv():
    with open("./short.txt", "r") as f:
        for line in f:
            print(','.join(line.rstrip()))



def toboggan(right, down):
    trees = 0
    r = down
    while r < len(grid):
        length_of_row = len(grid[r])
        c = (r * right) % length_of_row
        print(r, c)
        if grid[r][c] == '#':
            trees = trees + 1
        r = r + down
    print(f'Right {right}, down {down}: {trees}')

def toboggan_down_2(right, down):
    trees = 0
    r = down
    while r < len(grid):
        length_of_row = len(grid[r])
        c = (r -1 * right) % length_of_row
        print(r, c)
        if grid[r][c] == '#':
            trees = trees + 1
        r = r + down
    print(f'Right {right}, down {down}: {trees}')


def part1():
    toboggan(3, 1)
    

def part2():
    toboggan(1,1)
    toboggan(3,1)
    toboggan(5,1)
    toboggan(7,1)
    toboggan_down_2(1,2)


part1()
part2()
#make_forest_csv()