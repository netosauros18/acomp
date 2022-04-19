import numpy as np
from time import process_time_ns as ns

def bb_s(sequence):
#    a = 0
    n = len(sequence)
#    a += 1
    for i in range(n-1):
#      a += 1
      for j in range(n-i-1):
#        a += 1
        if(sequence[j] > sequence[j+1]):
#          a += 1
          sequence[j], sequence[j+1] = sequence[j+1], sequence[j]
#          a += 1
#    print(a)

def main(*args):
  v = np.random.randint(1, 10000, 10000)
  s = sorted(v)
  r = sorted(v,reverse = True)

 # print(v,s,r)
  
  n1 = ns()
  bb_s(v)
  n2 = ns()
  print(n2-n1)
#  print(v)

  n1 = ns()
  bb_s(s)
  n2 = ns()
  print(n2-n1)
#  print(s)
  
  n1 = ns()
  bb_s(r)
  n2 = ns()
  print(n2-n1)
#  print(r)  

if __name__ == '__main__':
  main()