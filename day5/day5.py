def binaryToNumber(b):
    return int(b, 2)

def seatId(row, seat):
    return binaryToNumber(row) * 8 + binaryToNumber(seat) 

with open("./input.txt", "r") as f:
    seats = []
    for line in f:
        line = line.rstrip()
        row = line[:7].replace('F','0').replace('B','1')
        seat = line[7:].replace('R','1').replace('L','0')
        seats.append(seatId(row,seat))

    print(f'part 1: {sorted(seats, reverse=True)[0]}')

    sortedSeats = sorted(seats)
    seatRange = range(sortedSeats[0], sortedSeats[len(sortedSeats)-1])
    for r in seatRange:
        if r not in sortedSeats:
            print (r)