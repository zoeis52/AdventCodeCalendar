import sys
import math

def recursive_fuel(fuel):
    total = 0
    while (fuel > 0):
        fuel = calc_fuel(fuel)
        if (fuel > 0):
            total += fuel

    return total


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

    total = 0
    for m in modules:
        fuel = recursive_fuel(int(m[0]))
        total += fuel

    # total += recursive_fuel(total)

    print(total)



main()
