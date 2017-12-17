import random
import math
from inspect import signature

PRECISION = 1000000         #Anzahl der zufälligen samples bei der integral berechnung für funktion f (higher number == better precision == more computing time)


def rand_interval(a, b):
    return (random.random()*(b - a) + a)

class Integral:
    def __init__(self, precision=PRECISION):
        self.precision=precision

    def compute_1dim(self,f, a, b):
        sum=0
        for i in range(self.precision):
            my_rand = rand_interval(a, b)
            sum+=f(my_rand)
        return (b-a) * (1 / self.precision) * sum

    def compute_multdim(self,f, a, b):
        sig = signature(f)
        params = sig.parameters
        num_para=len(params)
        sum=0

        for i in range(self.precision):
            my_rand = []
            for j in range(num_para):
                my_rand.append(rand_interval(a, b))
            sum+=f(*my_rand)
        return math.pow((b-a),num_para) * (1 / self.precision) * sum


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
    #print(my_integral.compute_multdim(h, 0, 1))

    f=open("integral_plotting.dat","w")
    for precision in range (1,100000,100):
        my_integral=Integral(precision)
        f.write(str(precision)+" "+str(2-my_integral.compute_1dim(math.sin,0,math.pi)))
        f.write("\n")
    f.close()


__name__ == '__main__' and main()