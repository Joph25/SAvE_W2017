PRECISION = 0.0001
import copy

class Potential:
    potential=[]


    def get_pot(self, filename):
        tmp_potential=[]
        with open(filename) as f:
            lines = f.readlines()
        for i in range(0, len(lines)):
            tmp_potential.append(lines[i].split())
        self.potential=tmp_potential
        for i in range(len(tmp_potential)):
            for j in range(len(tmp_potential[i])):
                if (tmp_potential[i][j][0] == '*'):
                    wert = float(tmp_potential[i][j].replace("*", ""))
                    self.potential[i][j]=[wert,True]
                else:
                    wert=float(tmp_potential[i][j])
                    self.potential[i][j]=[wert,False]



    def print_potential(self):
        for i in range(len(self.potential)):
            #for j in range(len(self.potential[i])):
            print (self.potential[i])

    def calc_potential_step(self):
        for i in range(len(self.potential)):
            for j in range(len(self.potential[i])):
                if (self.potential[i][j][1]==False):
                    self.potential[i][j][0]=(self.potential[i-1][j][0]+self.potential[i+1][j][0]+self.potential[i][j-1][0]+self.potential[i][j+1][0])/4

    def calc_potential(self):
        recalc=True
        while(recalc==True):
            prev_potential=copy.deepcopy(self.potential)        #saving potential bevore calculation for comparison
            self.calc_potential_step()
            recalc=False
            for i in range(len(self.potential)):
                for j in range(len(self.potential[i])):
                    residue=self.potential[i][j][0]-prev_potential[i][j][0]
                    if abs(residue)>PRECISION:
                        recalc=True
                        continue

    def print_to_file(self,filename):
        f = open(filename, 'w')
        for i in range(len(self.potential)):
            for j in range(len(self.potential[i])):
                f.write(str(self.potential[i][j][0]))
                f.write(" ")
            f.write("\n")
        f.close()

    def print_for_gnuplot(self,filename):
        f = open(filename, 'w')
        for i in range(len(self.potential)):
            for j in range(len(self.potential[i])):
                f.write(str(i)+" "+str(j)+" "+str(self.potential[i][j][0]))
                f.write("\n")
        f.close()

    def calc_potential_step_tmp(self):
        tmp_potential=copy.deepcopy(self.potential)
        for i in range(len(self.potential)):
            for j in range(len(self.potential[i])):
                if (self.potential[i][j][1]==False):
                    tmp_potential[i][j][0]=(self.potential[i-1][j][0]+self.potential[i+1][j][0]+self.potential[i][j-1][0]+self.potential[i][j+1][0])/4
        return tmp_potential


    def calc_potential_SOR(self,omega):
        recalc = True
        counter=0
        while (recalc == True):
            self.print_to_file("pot_out.dat")
            counter+=1
            tmp_potential = copy.deepcopy(self.potential)
            potential_preomega=self.calc_potential_step_tmp()
            recalc = False
            for i in range(len(self.potential)):
                for j in range(len(self.potential[i])):
                    residue=(potential_preomega[i][j][0] - tmp_potential[i][j][0])
                    if (abs(residue) > PRECISION):
                        recalc = True
                    if(self.potential[i][j][1]==False):
                        self.potential[i][j][0]=tmp_potential[i][j][0]+omega*residue
        return counter
# ---------------------------------------------------------------------------------------------------------
def main():
    dach=Potential()
    #for i in range(16,30):
    #omega=float(i)/10
    omega=1.9
    dach.get_pot("pl_ko60x60.dat")
    counter=dach.calc_potential_SOR(omega)
    print ("With omega "+str(omega)+" the calculation took "+str(counter)+" steps")
    dach.print_to_file("pot_out.dat")
    dach.print_for_gnuplot("gnu_pot_out.dat")


# ---------------------------------------------------------------------------------------------------------
__name__ == '__main__' and main()
