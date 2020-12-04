import sys

def read_input():
    "reads in the command line file and converts to a list of dictionaries"
    fileName = sys.argv[1]

    lines = []
    with open(fileName) as file:
        whole_file = file.read()
        for passport in whole_file.split('\n\n'):
            pass_dict = {}
            passport = passport.replace('\n', ' ')
            passport = passport.strip()
            for field_pair in passport.split(' '):
                field_pair = field_pair.split(":")
                pass_dict[field_pair[0]] = field_pair[1]
            lines.append(pass_dict)

    return lines

def determine_valid_fields(passport):
    # print(passport)
    for field in passport:
        if field == 'byr':
            value = passport[field]
            if len(value) != 4:
                print('byr too short')
                return False
            elif int(value) < 1920 or int(value) > 2002:
                print('byr incorrect range')
                return False
        elif field == 'iyr':
            value = passport[field]
            if len(value) != 4:
                print('iyr too short')
                return False
            elif int(value) < 2010 or int(value) > 2020:
                print('iyr incorrect range')
                return False
        elif field == 'eyr':
            value = passport[field]
            if len(value) != 4:
                print('eyr too short')
                return False
            elif int(value) < 2020 or int(value) > 2030:
                print('eyr incorrect range')
                return False
        elif field == 'hgt':
            value = passport[field]
            if value.find('cm') != -1:
                value = value.replace('cm', '')
                if int(value) < 150 or int(value) > 193:
                    print('hgt incorrect range')
                    return False
            elif value.find('in') != -1:
                value = value.replace('in', '')
                if int(value) < 59 or int(value) > 76:
                    print('hgt incorrect range')
                    return False
            else:
                print('hgt not cm or in')
                return False
        elif field == 'hcl':
            value = passport[field]
            if value[0] != '#':
                print('hcl no #')
                return False
            elif len(value[1:]) == 6:
                    try:
                        int(value[1:], 16)
                    except:
                        print('hcl not hex')
                        return False
            else:
                print('hcl too short')
                return False
        elif field == 'ecl':
            value = passport[field]
            ecl_set = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
            if value not in ecl_set:
                print('ecl not in set')
                return False
        elif field == 'pid':
            value = passport[field]
            if len(value) != 9:
                print('pid too short')
                return False
            else:
                try:
                    int(value)
                except:
                    print('pid not int')
                    return False
        elif field == 'cid':
            # pretty much do nothing here
            i = 0
        else:
            print('not a valid field')
            return False
    return True

def determine_valid_passport(passport, num_expected_fields):
    # Assumes that there are no unexpected fields in the passport
    if len(passport) == 8:
        if determine_valid_fields(passport):
        # print("all fields")
            return True
    # if only 7, but the missing one is cid, still vaild
    elif (len(passport) == 7) and ('cid' not in passport):
        # print("all but cid")
        if determine_valid_fields(passport):
            return True
    elif len(passport) >= 8:
        sys.exit("Error: there are unexpected fields")
    else:
        # print("not enough")
        return False

def count_valid_passports(passports, num_expected_fields):
    valid = 0
    for passport in passports:
        if determine_valid_passport(passport, num_expected_fields):
            valid += 1
    return valid

def main ():
    num_expected_fields = 8
    passports = read_input()
    print(count_valid_passports(passports, num_expected_fields))


main()
