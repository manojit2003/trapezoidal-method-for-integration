import numpy as np

def f(x):
    return x**2
def trap(A,B,n):
    h=(B-A)/(n-1)
    trap_sum = (f(A)+f(B))/2
    for i in range(1,n-1):
        trap_sum += f(A+(i*h)) 
    trap_sum *= h
    return (trap_sum)

print(trap(-1,10.00,5000))

