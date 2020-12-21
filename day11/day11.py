plane = []
rows = 0
columns = 0


def count_occupied(plane):
    count = 0
    for row in plane:
        count += row.count('#')
    return count


def count_occupied_seats(adjecent_seats, plane):
    count = 0
    for seat in adjecent_seats:
        if plane[seat[0]][seat[1]] == '#':
            count += 1
    return count

def get_adjacent(row, col):
    the_eight = [
            (row-1, col-1), (row-1, col),(row-1,col+1),
            (row, col-1), (row, col+1), 
            (row+1, col-1), (row+1, col), (row+1, col+1)
            ]
    first_cut = list(filter(lambda a: a[0]>=0 and a[1]>=0, the_eight))
    return list(filter(lambda b: b[0]<len(plane) and b[1]<len(plane[0]), first_cut))



def make_new_plane(r,c):
    new_plane = []
    i =0
    while i < r:
        new_plane.append(list('Z' * c))
        i += 1
    return new_plane


def apply_rules(a_plane):
    new_plane = make_new_plane(rows, columns)
    # print(new_plane)
    number_of_changes = 0
    for r, row in enumerate(a_plane):
        # print(f'row -> {row}')
        for c, col in enumerate(row):
            if a_plane[r][c] == '.':
                new_plane[r][c] = '.'

            if a_plane[r][c] == 'L':
                if count_occupied_seats(get_adjacent(r,c), a_plane) == 0:
                    new_plane[r][c] ='#'
                    number_of_changes += 1
                else:
                    new_plane[r][c] ='L'
            if a_plane[r][c] == '#':
                if count_occupied_seats(get_adjacent(r,c), a_plane) >= 4:
                    new_plane[r][c] ='L'
                    number_of_changes += 1
                else:
                    new_plane[r][c] ='#'      
    return (new_plane, number_of_changes)


with open("./input.txt", "r") as f:
    for line in f:
        plane.append(list(line.rstrip()))


rows = len(plane)
columns = len(plane[0])

# print(plane)
p = apply_rules(plane)
while p[1] > 0:
    print(p)
    p = apply_rules(p[0])

print(count_occupied(p[0]))