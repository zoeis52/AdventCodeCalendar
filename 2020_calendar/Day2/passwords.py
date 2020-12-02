import sys

def read_input():
    "reads in the command line file and converts to a list of lists"
    fileName = sys.argv[1]

    lines = []
    with open(fileName) as file:
        for line in file:
            pair = line.split(":")
            lines.append(pair)

    return lines

def interpret_rules(rule_password_pair):
    first_num = 0
    second_num = 0
    letter = ''
    rule = rule_password_pair[0]
    letter = rule[-1]
    tmp = rule.split("-")
    first_num = tmp[0]
    tmp = tmp[1].split(" ")
    second_num = tmp[0]

    return (int(first_num), int(second_num), letter)

def find_valid_passwords(rule_password_pairs):
    valid_passwords = 0
    for pair in rule_password_pairs:
        first_num, second_num, letter = interpret_rules(pair)
        letter_count = pair[1].count(letter)
        if (letter_count >= first_num) and (letter_count <= second_num):
            valid_passwords += 1

    return valid_passwords


def main ():
    rule_password_pairs = read_input()
    print(find_valid_passwords(rule_password_pairs))


main()
