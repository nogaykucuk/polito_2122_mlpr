# Laboratory 1 Extra
# Exercise 2 (adapted from Computer Sciences exam 23/06/2014)

# Please note that, for this exercise I've decided to pass the size of
# the room N, from the command line as well
from sys import argv


def put_one_half(r, c, room, N):
    if (r-1) >= 0:
        room[r-1][c] += 0.5
        if (c-1) >= 0:
            room[r-1][c-1] += 0.5
        if (c+1) < N:
            room[r-1][c+1] += 0.5
    if (r+1) < N:
        room[r+1][c] += 0.5
        if (c-1) >= 0:
            room[r+1][c-1] += 0.5
        if (c+1) < N:
            room[r+1][c+1] += 0.5
    if (c-1) >= 0:
        room[r][c-1] += 0.5
    if (c+1) < N:
        room[r][c+1] += 0.5


def put_one_fifth(r, c, room, N):
    if (r-2) >= 0:
        room[r-2][c] += 0.2
        if (c-1) >= 0:
            room[r-2][c-1] += 0.2
        if (c+1) < N:
            room[r-2][c+1] += 0.2
        if (c-2) >= 0:
            room[r-2][c-2] += 0.2
        if (c+2) <= N:
            room[r-2][c+2] += 0.2
    if (r+2) < N:
        room[r+2][c] += 0.2
        if (c-1) >= 0:
            room[r+2][c-1] += 0.2
        if (c+1) < N:
            room[r+2][c+1] += 0.2
        if (c-2) >= 0:
            room[r+2][c-2] += 0.2
        if (c+2) <= N:
            room[r+2][c+2] += 0.2
    if (c-2) >= 0:
        room[r][c-2] += 0.2
        if (r-1) >= 0:
            room[r-1][c-2] += 0.2
        if(r+1) < N:
            room[r+1][c-2] += 0.2
    if (c+2) <= N:
        room[r][c+2] += 0.2
        if (r-1) >= 0:
            room[r-1][c+2] += 0.2
        if(r+1) < N:
            room[r+1][c+2] += 0.2


def main():
    f_name = argv[1]
    N = int(argv[2])
    room = []
    for i in range(0, N):
        rows = []
        for j in range(0, N):
            rows.append(0.0)
        room.append(rows)
    with open(f_name) as f:
        for line in f:
            row, column = line.split()
            row = int(row)
            column = int(column)
            room[row][column] += 1.0
            put_one_half(row, column, room, N)
            put_one_fifth(row, column, room, N)
    # converted float matrix to string matrix for better readibility of
    # the output
    for i in range(0, N):
        for j in range(0, N):
            room[i][j] = ("%.1f" % room[i][j])
    print("Output:")
    for i in range(0, N):
        print("\t", room[i])


if __name__ == "__main__":
    main()
