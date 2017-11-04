import math


# ---------------------------------------------------------------------------------------------------------
class Map():
    bound_coord = []
    circumference=0
    area=0
    cog=0  # center of gravity

    # ---------------------------------------------------------------------------------------------------------
    def read_coord(self, filename):
        lines=[]
        with open(filename) as f:
            lines=f.readlines()
        del lines[0:2]           #deleting first two lines (not gps coordinates)
        for i in range (0,len(lines)):
            self.bound_coord.append(lines[i].split())


"""    # ---------------------------------------------------------------------------------------------------------

    def calc_circ(self):  # calculating circumference

    # ---------------------------------------------------------------------------------------------------------
    def calc_area(self):

    # ---------------------------------------------------------------------------------------------------------
    def calc_cog(self):

    # ---------------------------------------------------------------------------------------------------------
    def print(self):
"""

# ---------------------------------------------------------------------------------------------------------
def main():
    austria = Map()
    austria.read_coord('Gpsies_austria.csv')


"""    austria.calc_circ()
    austria.calc_area()
    austria.calc_cog()
    austria.print()
"""

# ---------------------------------------------------------------------------------------------------------
__name__ == '__main__' and main()
