import sys

class WireGraph:
    def __init__(self):
        self.size = 10000
        self.graph = [[0]* self.size for i in range(self.size) ]

        self.no_wire = 0
        self.one_wire = 1
        self.cross = "X"
        self.center = "C"

        self.center_loc = 5000

        self.graph[self.center_loc][self.center_loc] = self.center

        self.wire1 = []
        self.wire2 = []

        # print(self.graph)

    def input_wires(self, fileName):
        i = 1
        with open(fileName) as file:
            for line in file:
                split = (line.split(','))
                for dir in split:
                    dir = dir.strip()
                    if i == 1:
                        self.wire1.append(dir)
                    elif i == 2:
                        self.wire2.append(dir)
                i += 1

        # print(self.wire1)
        # print(self.wire2)

    def set_wires(self):
        cur_loc_horz = self.center_loc
        cur_loc_vert = self.center_loc
        for dir in self.wire1:
            if (self.wire1[dir][0] == "R"):
                len = int(self.wire1[dir].replace('R', ''))

            elif (self.wire1[dir][0] == "L"):
                len = - int(self.wire1[dir].replace('L', ''))

            elif (self.wire1[dir][0] == "U"):
                len = int(self.wire1[dir].replace('U', ''))

            elif (self.wire1[dir][0] == "D"):
                len = - int(self.wire1[dir].replace('D', ''))

    def update_graph(self, len, dir, cur_loc_horz, cur_loc_vert):
        if (dir == 'R' or dir == 'L'):
            new_loc_horz = cur_loc_horz + len
            for i in range(abs(len)):
                if dir == 'R':
                    cur_loc_horz += 1
                    if self.graph[cur_loc_horz][cur_loc_vert] == self.no_wire:
                        self.graph[cur_loc_horz][cur_loc_vert] = self.one_wire
                    elif self.graph[cur_loc_horz][cur_loc_vert] == self.one_wire:
                        self.graph[cur_loc_horz][cur_loc_vert] = self.cross




if __name__ == "__main__":
    wires = WireGraph()
    wires.input_wires(sys.argv[1])
