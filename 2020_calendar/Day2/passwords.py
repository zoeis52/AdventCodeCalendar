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
    """
    parses the given rule password pair for the
    numbers and the letter for the rule
    """
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

def find_valid_sled_passwords(rule_password_pairs):
    """
    determines if passwords are valid based on the rule that the
    password contains the given letter some number of times
    (based on the first and second numbers in rule)
    """
    valid_passwords = 0
    for pair in rule_password_pairs:
        first_num, second_num, letter = interpret_rules(pair)
        letter_count = pair[1].count(letter)
        if (letter_count >= first_num) and (letter_count <= second_num):
            valid_passwords += 1

    return valid_passwords

def find_valid_tobaggan_passwords(rule_password_pairs):
    """
    determines if passwords are valid based on the rule that the
    password contains the given letter at either the first provided
    index or the second, but not both
    """
    valid_passwords = 0
    for pair in rule_password_pairs:
        first_num, second_num, letter = interpret_rules(pair)
        password = pair[1]
        if (password[first_num] == letter) != (password[second_num] == letter):
            valid_passwords += 1

    return valid_passwords


def main ():
    # Find the valid passwords
    rule_password_pairs = read_input()
    print(find_valid_sled_passwords(rule_password_pairs))
    print(find_valid_tobaggan_passwords(rule_password_pairs))


main()
