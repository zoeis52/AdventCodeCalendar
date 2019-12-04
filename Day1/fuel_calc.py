import sys
import math

def calc_fuel(mass):
    fuel = math.floor(mass / 3) - 2

    return fuel


def read_input():
    fileName = sys.argv[1]

    modules = []
    with open(fileName) as file:
        for line in file:
            modules.append(line.split())

    return modules


def main ():
    modules = read_input()

    print(modules)

    total = 0
    for m in modules:
        fuel = calc_fuel(int(m[0]))
        total += fuel

    print(total)



main()
