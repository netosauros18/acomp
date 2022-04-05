import numpy as np
from time import process_time_ns as ns


def max(v):
    m = v[0]  #(1)
    for i in range(1, len(v)):  #(2)
        if v[i] > m:  #(3)
            m = v[i]  #(4)
    return m  #(5)

def bubble_sort(sequence):
    n = len(sequence)
    for i in range(n-1):
        for j in range(n-i-1):
            if(sequence[j] > sequence[j+1]):
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]


v = np.random.randint(1, 10, 10)
s = sorted(v)
r = sorted(v,reverse = True)
print (v)
n1 = ns()
bubble_sort(v)
n2 = ns()

print(v)
print(n2-n1)
