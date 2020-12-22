import sys

def read_input():
    "reads in the command line file and converts to a list of dictionaries"
    fileName = sys.argv[1]

    bag_rules = {}
    with open(fileName) as file:
        for line in file:
            unparsed_bag_rules = line.split('bag')
            unparsed_bag_rules = unparsed_bag_rules[:-1]
            key_bag = unparsed_bag_rules[0].strip()
            bags_contained = []
            if 'no other' in unparsed_bag_rules[1]:
                bag_rules[key_bag] = bags_contained
            else:
                for j in range(1, len(unparsed_bag_rules)):
                    tmp = unparsed_bag_rules[j].strip('s ,')
                    # get rid of the digits in the bag rules
                    tmp = ''.join([i for i in tmp if not i.isdigit()])
                    tmp = tmp.split('contain')
                    tmp = [i for i in tmp if i]
                    tmp = tmp[0].strip()
                    bags_contained.append(tmp)
                bag_rules[key_bag] = bags_contained

    return bag_rules

def read_bag_num_input():
    "reads in the command line file and converts to a list of bag dictionaries"
    fileName = sys.argv[1]

    bag_rules = {}
    with open(fileName) as file:
        for line in file:
            unparsed_bag_rules = line.split('bag')
            unparsed_bag_rules = unparsed_bag_rules[:-1]
            key_bag = unparsed_bag_rules[0].strip()
            bags_contained = []
            # no more bags will be contained in this
            if 'no other' in unparsed_bag_rules[1]:
                bag_rules[key_bag] = bags_contained
            else:
                # loop over all bags within the bag
                for j in range(1, len(unparsed_bag_rules)):
                    tmp = unparsed_bag_rules[j].strip('s ,')
                    tmp = tmp.split('contain')
                    # removes empty strings after the split
                    tmp = [i for i in tmp if i]
                    tmp = tmp[0].strip()

                    # get the numbers out of the string
                    num = [int(word) for word in tmp.split() if word.isdigit()]
                    tmp = tmp.strip(str(num[0]))
                    tmp = tmp.strip()
                    bags_contained.append((tmp, num[0]))
                bag_rules[key_bag] = bags_contained

    return bag_rules

def recursive_contains_bag(bag_rules, cur_bag, bag_to_contain):
    for sub_bag in bag_rules[cur_bag]:
        sub_bag = sub_bag[0]
        if sub_bag == bag_to_contain or \
        recursive_contains_bag(bag_rules, sub_bag, bag_to_contain):
            return True
    return False

def count_bags(bag_rules, bag_to_contain):
    num_bags_can_contain = 0
    for bag in bag_rules:
        if recursive_contains_bag(bag_rules, bag, bag_to_contain):
            num_bags_can_contain += 1

    return num_bags_can_contain

def recursive_bags_within(bag_rules, bag_holding):
    if bag_rules[bag_holding[0]] == []:
        return bag_holding[1]
    else:
        # have to recurisivly go back and find all bags within this one
        bags_within = bags_in(bag_rules, bag_holding[0])
        # recursive equation for each bag
        return (bag_holding[1] + (bag_holding[1] * bags_within) )


def bags_in(bag_rules, bag_holding):
    num_bags_within = 0
    for bag_in in bag_rules[bag_holding]:
        num_bags_within += recursive_bags_within(bag_rules, bag_in)
    return num_bags_within



def main():
    bag_rules = read_bag_num_input()
    print(bag_rules)
    print(count_bags(bag_rules, 'shiny gold'))

    print(bags_in(bag_rules, 'shiny gold'))

main()
