import numpy as np
from time import process_time_ns as ns


def max(v):
    m = v[0]  #(1)
    for i in range(1, len(v)):  #(2)
        if v[i] > m:  #(3)
            m = v[i]  #(4)
    return m  #(5)


def main(*args):
  v = np.random.randint(1, 10, 10)
  s = sorted(v)
  r = sorted(v,reverse = True)

  print(v,s,r)
  
  n1 = ns()
  max(v)
  n2 = ns()
  print(n2-n1)
#  print(v)

  n1 = ns()
  max(s)
  n2 = ns()
  print(n2-n1)
#  print(s)
  
  n1 = ns()
  max(r)
  n2 = ns()
  print(n2-n1)
#  print(r)  

if __name__ == '__main__':
  main()
