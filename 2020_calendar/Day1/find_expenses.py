import sys

def read_input():
    fileName = sys.argv[1]

    lines = []
    with open(fileName) as file:
        for line in file:
            lines.append(int(line))

    return lines

def find_2020_nums(expenses, add_search):
    for num_1 in expenses:
         less_than = add_search - num_1
         for num_2 in expenses:
             if (num_2 <= less_than):
                 if num_1 + num_2 == add_search:
                     return (num_1, num_2)


def main ():
    add_search = 2020
    expense_report = read_input()
    expense_report.sort()
    num_1, num_2 = find_2020_nums(expense_report, add_search)
    print(num_1 * num_2)


main()
