import sys

def read_input():
    "reads in the command line file and converts to a list of lists"
    fileName = sys.argv[1]

    lines = []
    with open(fileName) as file:
        for line in file:
            line_list = []
            for char in line:
                if char != '\n':
                    line_list.append(char)
            lines.append(line_list)

    return lines

def pretty_print_landscape(landscape):
    for line in landscape:
        for char in line:
            print(char, end='')
        print('\n')

def tree_or_not(landscape, i, j):
    """
    Determines if a tree is in the given location in the landscape
    Takes into account if the index is over to the right since the
    landscape repeats
    Returns: a bool of whether or not there is a tree
    """
    landscape_width = len(landscape[0])
    if i >= landscape_width:
        i = i % landscape_width
    if landscape[j][i] == '#':
        return True
    return False


def count_trees(landscape, over, down):
    """
    Finds the number of trees in the path starting at 0,0
    """
    trees = 0
    j = 0
    i = 0
    while j < len(landscape):
        if tree_or_not(landscape, i, j):
            trees += 1
            # landscape[j][i] = 'X'
        # else:
        #     landscape[j][i] = 'O'
        j += down
        i += over
    return trees

def check_slopes(landscape, over, down):
    "loops through possible slopes and gets the number of trees for each"
    slope_trees = []
    for s in range(len(over)):
        slope_trees.append(count_trees(landscape, over[s], down[s]))
    return slope_trees


def main ():
    over = [1, 3, 5, 7, 1]
    down = [1, 1, 1, 1, 2]
    landscape = read_input()
    print(len(landscape))
    pretty_print_landscape(landscape)
    trees = check_slopes(landscape, over, down)
    print(trees)

    total = 1
    for num in trees:
        total *= num

    print(total)



main()
