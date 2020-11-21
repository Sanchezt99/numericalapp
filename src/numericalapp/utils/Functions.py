import numpy as np


def f(x):
    return np.log(np.power(np.sin(x),2) + 1) - 0.5

def f1(x):
    return np.log(np.power(np.sin(x),2)+1)-0.5-x

def efPrime(x):
    return 2 * ( 1 / (np.power(np.sin(x), 2) + 1)) * np.sin(x) * np.cos(x)

def g(x):
    return np.log(np.power(np.sin(x),2)+1)-1/2

def h(x):
    return np.exp(x)-x-1

def hPrime(x):
    return np.exp(x) - 1

def hPrimeTwo(x):
    return np.exp(x)


def f(x):
    return np.exp(x-0.5) - 0.5 * np.power(x,2) - 0.5*x - 0.625

def fPrime(x):
    return -x + np.exp(x-0.5) - 0.5

def fPrimePrime(x):
    return np.exp(x-0.5) - 1

def e(x):
    
    return 0.5 * np.power(x,2) + 1 * x + 0