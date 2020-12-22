import sys

def read_input_anyone():
    "reads in the command line file and converts to a list of ints"
    fileName = sys.argv[1]

    lines = []
    with open(fileName) as file:
        whole_file = file.read()
        for group in whole_file.split('\n\n'):
            q_set = set([])
            group = group.replace('\n', '')
            group = group.strip()
            for char in group:
                q_set.add(char)
            lines.append(q_set)

    return lines

def read_input_everyone():
    "reads in the command line file"
    fileName = sys.argv[1]

    lines = []
    with open(fileName) as file:
        whole_file = file.read()
        for group in whole_file.split('\n\n'):
            q_set = set([])
            group = group.strip()
            for i, qs in enumerate(group.split('\n')):
                if i == 0:
                    for char in qs:
                        q_set.add(char)
                else:
                    q_tmp = set([])
                    for char in qs:
                        q_tmp.add(char)
                    q_set = q_set & q_tmp
            lines.append(q_set)

    return lines

def sum_qs(forms):
    sum = 0
    for q_set in forms:
        sum += len(q_set)
    return sum

def main():
    forms = read_input_everyone()
    # print(forms)
    print(sum_qs(forms))

main()
