class Random:

    def __init__(self,a,c,m,y1=923494329729):
            self.a = a
            self.c = c
            self.m=m
            self.y=y1

    def rand(self):
        tmp=(self.a*self.y+self.c)%self.m
        self.y=tmp
        return self.y


    def uni01(self):
        my_rand=self.rand()
        norm_rand=float(my_rand)/float(self.m)
        return norm_rand


    def uni(self,imax):
       return (imax*self.uni01())

    def rand_interval(self,a,b):
        return (self.uni01()*(b-a)+a)

def main():

    my_rand=Random(5641,6563,5237,7823)
    """
    for i in range(20):
        print(my_rand.rand())

    for i in range(20):
        print(my_rand.uni01())


    for i in range(100):
        print(my_rand.uni(100))

    for i in range(100):
        print(my_rand.rand_interval(-30,100))
    """
    f = open('random_numbers.dat', 'w')
    for i in range (1000):
        for j in range (3):
            f.write(str(my_rand.uni01())+str(" "))
        f.write("\n")
    f.close()

__name__ == '__main__' and main()