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

def contains_bag(bag_rules, cur_bag, bag_to_contain):
    for sub_bag in bag_rules[cur_bag]:
        if sub_bag == bag_to_contain or \
        contains_bag(bag_rules, sub_bag, bag_to_contain):
            return True
    return False

def recursive_count_bags(bag_rules, bag_to_contain):
    num_bags_can_contain = 0
    for bag in bag_rules:
        if contains_bag(bag_rules, bag, bag_to_contain):
            num_bags_can_contain += 1

    return num_bags_can_contain

# def how_many_contain_bag(bag_rules, bag_to_contain):
#     bags_to_search_for = set([bag_to_contain])
#     bags_searched = set([])
#     num_bags_can_contain = 0
#     while len(bags_to_search_for) != 0:
#         print(bags_to_search_for)
#         new_bags = set([])
#         for bag in bag_rules:
#             if any(item in bags_to_search_for for item in bag_rules[bag]):
#                 if bag not in bags_searched:
#                     num_bags_can_contain += 1
#                     new_bags.add(bag)
#         bags_searched = bags_to_search_for
#         bags_to_search_for = new_bags - bags_searched
#     return num_bags_can_contain


def main():
    bag_rules = read_input()
    print(bag_rules)
    print(recursive_count_bags(bag_rules, 'shiny gold'))

main()
