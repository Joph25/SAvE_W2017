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





my_rand=Random(5641,6563,5237,7823)

for i in range(20):
    print(my_rand.rand())

for i in range(20):
    print(my_rand.uni01())
    

for i in range(100):
    print(my_rand.uni(100))