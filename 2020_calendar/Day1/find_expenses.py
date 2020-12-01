import sys

def read_input():
    "reads in the command line file and converts to a list of ints"
    fileName = sys.argv[1]

    lines = []
    with open(fileName) as file:
        for line in file:
            lines.append(int(line))

    return lines

def find_2020_nums(expenses, add_search):
    """
    finds the 2 numbers in expenses that
    sum to add_search
    inputs: list of expenses as ints
        and the number searching for
    """
    for num_1 in expenses:
         less_than = add_search - num_1
         for num_2 in expenses:
             # try to reduce to computations that could possibily be add_search
             if (num_2 <= less_than):
                 if num_1 + num_2 == add_search:
                     return (num_1, num_2)

# terrible run time, is there a better solution?
def find_three_2020_nums(expenses, add_search):
    """
    finds the 3 numbers in expenses that
    sum to add_search
    inputs: list of expenses as ints
        and the number searching for
    """
    for num_1 in expenses:
         for num_2 in expenses:
             for num_3 in expenses:
                 if num_1 + num_2 + num_3 == add_search:
                     return (num_1, num_2, num_3)


def main ():
    add_search = 2020
    expense_report = read_input()
    expense_report.sort()
    num_1, num_2 = find_2020_nums(expense_report, add_search)
    print(num_1 * num_2)

# for part 2
    num_1, num_2, num_3 = find_three_2020_nums(expense_report, add_search)
    print(num_1 * num_2 * num_3)


main()
