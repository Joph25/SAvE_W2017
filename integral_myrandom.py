from myrandom import Random
import math
from inspect import signature

PRECISION = 100000         #Anzahl der zufälligen samples bei der integral berechnung für funktion f (higher number == better precision == more computing time)

class Integral:
    def __init__(self):
        self.myrandom = Random(5641, 6563, 5237, 7823)

    def compute_1dim(self,f, a, b):
        sum=0
        for i in range(PRECISION):
            my_rand = self.myrandom.rand_interval(a, b)
            sum+=f(my_rand)
        return(b-a)*(1/PRECISION)*sum

    def compute_multdim(self,f, a, b):
        sig = signature(f)
        params = sig.parameters
        num_para=len(params)
        sum=0

        for i in range(PRECISION):
            my_rand = []
            for j in range(num_para):
                my_rand.append(self.myrandom.rand_interval(a, b))
            sum+=f(*my_rand)
        return math.pow((b-a),num_para)*(1/PRECISION)*sum

def f(x):
    return (x * x)

def g(x,y):
    #print(x,y)
    return(x*x*y*y)

def h(x,y,z):
    #print(x,y,z)
    return(x*x*y*y*z*z)

def main():

    my_integral = Integral()

    #print(my_integral.compute_1dim(math.sin, 0, (math.pi)/2))
    #print(my_integral.compute_1dim(f, 0, 10))
    #print(my_integral.compute_multdim(g, -10, 10))
    print(my_integral.compute_multdim(h, 0, 1))

__name__ == '__main__' and main()