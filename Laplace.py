import copy

PRECISION = 0.0001

#TODO tu hier was

class Potential:
    potential = []
    starting_pot = []
    e_field = []

    def __init__(self):
        self.potential = []
        self.starting_pot = []

    def get_pot(self, filename):
        tmp_potential = []
        with open(filename) as f:
            lines = f.readlines()
        for i in range(0, len(lines)):
            tmp_potential.append(lines[i].split())
        self.potential = tmp_potential
        for i in range(len(tmp_potential)):
            for j in range(len(tmp_potential[i])):
                if tmp_potential[i][j][0] == '*':
                    wert = float(tmp_potential[i][j].replace("*", ""))
                    self.potential[i][j] = [wert, True]
                else:
                    wert = float(tmp_potential[i][j])
                    self.potential[i][j] = [wert, False]
        self.starting_pot = self.potential

    def print_potential(self):
        for i in range(len(self.potential)):
            # for j in range(len(self.potential[i])):
            print(self.potential[i])

    def calc_potential_step(self):
        for i in range(len(self.potential)):
            for j in range(len(self.potential[i])):
                if not self.potential[i][j][1]:
                    # calculating potential as median of surrounding points
                    self.potential[i][j][0] = (self.potential[i - 1][j][0] + self.potential[i + 1][j][0] +
                                               self.potential[i][j - 1][0] + self.potential[i][j + 1][0]) / 4

    def calc_potential(self):
        recalc = True
        counter = 0
        while recalc:
            counter += 1
            prev_potential = copy.deepcopy(self.potential)  # saving potential bevore calculation for comparison
            self.calc_potential_step()
            recalc = False
            for i in range(len(self.potential)):
                for j in range(len(self.potential[i])):
                    residue = self.potential[i][j][0] - prev_potential[i][j][0]
                    if abs(residue) > PRECISION:
                        recalc = True
                        continue
        return counter

    def print_to_file(self, filename):
        f = open(filename, 'w')
        for i in range(len(self.potential)):
            for j in range(len(self.potential[i])):
                f.write(str("%.2f" % self.potential[i][j][0]))
                f.write(" ")
            f.write("\n")
        f.close()

    def print_field_to_file(self, filename):
        f = open(filename, 'w')
        for i in range(len(self.e_field)):
            for j in range(len(self.e_field[i])):
                f.write(str('%.1f' % self.e_field[i][j][0] + ',%.1f' % self.e_field[i][j][1]))
                f.write(" ")
            f.write("\n")
        f.close()

    def print_for_gnuplot(self, filename):
        f = open(filename, 'w')
        for i in range(len(self.potential)):
            for j in range(len(self.potential[i])):
                f.write(str(i) + " " + str(j) + " " + str(self.potential[i][j][0]))
                f.write("\n")
        f.close()

    def print_field_for_gnuplot(self, filename):
        f = open(filename, 'w')
        for i in range(len(self.e_field)):
            for j in range(len(self.e_field[i])):
                f.write(str(i) + " " + str(j) + " " + str(self.e_field[i][j][0]) + " " + str(self.e_field[i][j][1]))
                f.write("\n")
        f.close()

    def calc_potential_sor(self, omega):
        recalc = True
        counter = 0
        while recalc:
            self.print_to_file("pot_out.dat")
            counter += 1
            tmp_potential = copy.deepcopy(
                self.potential)  # copy previous potential for comnparison and residue calculation
            recalc = False
            for i in range(len(self.potential)):
                for j in range(len(self.potential[i])):
                    if not self.potential[i][j][1]:
                        # calculating potential as median of surrounding points
                        residue = (((self.potential[i - 1][j][0] + self.potential[i + 1][j][0] +
                                     self.potential[i][j - 1][0] + self.potential[i][j + 1][0]) / 4) -
                                   tmp_potential[i][j][0])
                        if abs(residue) > PRECISION:
                            recalc = True
                        if abs(residue) > 10000:
                            print("residue too big @ counter " + str(counter))
                            quit()
                        if not self.potential[i][j][1]:
                            self.potential[i][j][0] = self.potential[i][j][0] + (omega * residue)
        return counter

    def calc_field(self):
        self.e_field = copy.deepcopy(self.potential)
        for i in range(len(self.potential)):
            for j in range(len(self.potential[i])):
                if not self.potential[i][j][1]:
                    self.e_field[i][j][0] = -(self.potential[i][j][0] - self.potential[i - 1][j][0])
                    self.e_field[i][j][1] = -(self.potential[i][j][0] - self.potential[i][j - 1][0])
                else:
                    self.e_field[i][j][0] = 0
                    self.e_field[i][j][1] = 0


# ---------------------------------------------------------------------------------------------------------
def main():
    dach = Potential()
    for i in range(1680,1700):
        omega=float(i)/1000
        dach.get_pot('laplace_daten/pl_ko30x30.dat')
        counter = dach.calc_potential_sor(omega)
        print("With omega " + str(omega) + " the calculation took " + str(counter) + " steps")
    dach.calc_field()
    dach.print_field_to_file("field_out.dat")
    dach.print_field_for_gnuplot('gnu_field.dat')
    dach.print_to_file("pot_out.dat")
    dach.print_for_gnuplot("gnu_pot_out.dat")


# ---------------------------------------------------------------------------------------------------------
__name__ == '__main__' and main()
