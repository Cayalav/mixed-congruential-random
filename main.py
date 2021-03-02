#https://www.geeksforgeeks.org/linear-congruence-method-for-generating-pseudo-random-numbers/

#https://en.wikipedia.org/wiki/Linear_congruential_generator#:~:text=A%20linear%20congruential%20generator%20(LCG,known%20pseudorandom%20number%20generator%20algorithms.

def linearCongruentialMethod(Xo, m, a, c, randomNums, noOfRandomNums): 
    randomNums[0] = Xo 
    for i in range(1, noOfRandomNums): 
        randomNums[i] = ((randomNums[i - 1] * a) +c) % m 

if __name__ == '__main__': 
    Xo = 5 
    m = 7 
    a = 3 
    c = 0
    noOfRandomNums = 10
    randomNums = [0] * (noOfRandomNums) 
    linearCongruentialMethod(Xo, m, a, c,randomNums,noOfRandomNums) 
    for i in randomNums: 
        print(i, end = " ") 

#def lcg(modulus, a, c, seed):
#  while True:
#      seed = (a * seed + c) % modulus
#      yield seed
#lcg(7,3,2,5)    