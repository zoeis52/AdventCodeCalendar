import sys

def calc_answer(noun, verb):
    return 100 * noun + verb

def run_instr(instr):
    cur = 0

    while (instr[cur] != 99):
        a_index = instr[cur + 1]
        a = instr[a_index]
        b_index = instr[cur + 2]
        b = instr[b_index]
        out_index = instr[cur + 3]

        if (instr[cur] == 1):
            instr[out_index] = a + b
        elif (instr[cur] == 2):
            instr[out_index] = a * b

        cur += 4
        # print(instr)


    return instr


def read_input():
    fileName = sys.argv[1]

    instr = []
    with open(fileName) as file:
        for line in file:
            split = (line.split(','))
            for num in split:
                num = num.strip()
                instr.append(int(num))

    return instr


def main ():
    instr = read_input()

    print(instr)

    for noun in range(100):
        for verb in range(100):
            mem = instr.copy()
            mem[1] = noun
            mem[2] = verb

            run_instr(mem)

            if (mem[0] == 19690720):
                print("solution is: ", calc_answer(noun, verb))
                print(mem)
                break

    # run_instr(instr)






main()
