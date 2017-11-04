import math
import utm


# ---------------------------------------------------------------------------------------------------------
class Map:
    bound_coord = []
    bound_coord_utm = []
    circumference = 0
    area = 0
    cog = []  # center of gravity

    # ---------------------------------------------------------------------------------------------------------
    def read_coord(self, filename):
        with open(filename) as f:
            lines = f.readlines()
        del lines[0:2]  # deleting first two lines (not gps coordinates)
        for i in range(0, len(lines)):
            self.bound_coord.append(lines[i].split())

        # convert gps coord to utm coord
        for i in range(0, len(self.bound_coord)):
            self.bound_coord_utm.append(utm.from_latlon(float(self.bound_coord[i][0]), (float(self.bound_coord[i][1]))))
            # print(self.bound_coord_utm[i])

    # ---------------------------------------------------------------------------------------------------------

    def calc_circ(self):  # calculating circumference
        for i in range(0, (len(self.bound_coord) - 1)):
            long_from = float(self.bound_coord[i][0])
            long_to = float(self.bound_coord[i + 1][0])
            lat_from = float(self.bound_coord[i][1])
            lat_to = float(self.bound_coord[i + 1][1])
            tmp = math.acos(math.sin(lat_from) * math.sin(lat_to) + math.cos(lat_from) * math.cos(lat_to) * math.cos(
                long_from - long_to))
            self.circumference += tmp * 6370 * math.pi / 180

        # adding last element to first element
        long_from = float(self.bound_coord[-1][0])
        long_to = float(self.bound_coord[0][0])
        lat_from = float(self.bound_coord[-1][1])
        lat_to = float(self.bound_coord[0][1])
        tmp = math.acos(math.sin(lat_from) * math.sin(lat_to) + math.cos(lat_from) * math.cos(lat_to) * math.cos(
            long_from - long_to))
        self.circumference += tmp * 6370 * math.pi / 180

    # ---------------------------------------------------------------------------------------------------------
    def calc_singular_utm_area(self, coordinates):
        area = 0
        for i in range(0, len(coordinates)):  # calculating area using gaussian area algorithm
            x_from = coordinates[i][0]
            x_to = coordinates[(i + 1) % (len(coordinates))][0]
            y_from = coordinates[i][1]
            y_to = coordinates[(i + 1) % (len(coordinates))][1]
            area += (x_from + x_to) * (y_from - y_to)
        return 0.5 * abs(area)

    # ---------------------------------------------------------------------------------------------------------
    def calc_area(self):
        letters = []
        for c in range(ord('C'), ord('Y')):  # creating letter range from C to X
            letters.append(chr(c))
        for i in range(1, 60):
            for j in letters:
                coordinates = []
                for k in range(0, (len(self.bound_coord))):
                    if j in ('I', 'O'):  # I and O are not accepted fields
                        continue
                    if i != self.bound_coord_utm[k][2]:
                        continue
                    if j != self.bound_coord_utm[k][3]:
                        continue
                    coordinates.append(self.bound_coord_utm[k])
                self.area += self.calc_singular_utm_area(coordinates)

   # ---------------------------------------------------------------------------------------------------------

    def calc_singular_utm_cog(self, coordinates):
        cog = []
        for i in range(0, len(coordinates)):  # calculating area using gaussian area algorithm
            x_from = coordinates[i][0]
            x_to = coordinates[(i + 1) % (len(coordinates))][0]
            y_from = coordinates[i][1]
            y_to = coordinates[(i + 1) % (len(coordinates))][1]
            
        return 0.5 * abs(area)
    def calc_cog(self):
        letters = []
        for c in range(ord('C'), ord('Y')):  # creating letter range from C to X
            letters.append(chr(c))
        for i in range(1, 60):
            for j in letters:
                coordinates = []
                for k in range(0, (len(self.bound_coord))):
                    if j in ('I', 'O'):  # I and O are not accepted fields
                        continue
                    if i != self.bound_coord_utm[k][2]:
                        continue
                    if j != self.bound_coord_utm[k][3]:
                        continue
                    coordinates.append(self.bound_coord_utm[k])
                self.area += self.calc_singular_utm_area(coordinates)
    # ---------------------------------------------------------------------------------------------------------
    def print(self):
        print("Umfang: %.2f" %self.circumference," km")
        print("Flaeche: %.2f"% (self.area/1000000)," km^2")
        print("Schwerpunkt bei: ",self.cog)



# ---------------------------------------------------------------------------------------------------------
def main():
    austria = Map()
    austria.read_coord('Gpsies_austria.csv')

    austria.calc_circ()
    austria.calc_area()
    austria.calc_cog()
    austria.print()


# ---------------------------------------------------------------------------------------------------------
__name__ == '__main__' and main()
