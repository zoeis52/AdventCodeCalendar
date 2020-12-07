import sys
import math

def read_input():
    "reads in the command line file and converts to a list of ints"
    fileName = sys.argv[1]

    lines = []
    with open(fileName) as file:
        for line in file:
            lines.append(line.strip())

    return lines

def find_seat(ticket, max_seat, char_up, char_down):
    range_top = max_seat
    range_bottom = 0
    for i in range(int(math.log(max_seat + 1, 2))):
        seats_left = (range_top - range_bottom) + 1
        if ticket[i] == char_up:
            range_top = (seats_left // 2) + range_bottom - 1
        elif ticket[i] == char_down:
             range_bottom = (seats_left // 2) + range_bottom + 1

    return range_top

def calc_seat_id(ticket):
    row = find_seat(ticket, 127, 'F', 'B')
    col = find_seat(ticket[-3:], 7, 'L', 'R')
    return (row * 8) + col

def find_max_seat_id(tickets):
    max = 0
    for t in tickets:
        id = calc_seat_id(t)
        if id > max:
            max = id
    return max


def main():
    tickets = read_input()
    # print(calc_seat_id('FBFBBFFRLR'))
    print(find_max_seat_id(tickets))

main()
