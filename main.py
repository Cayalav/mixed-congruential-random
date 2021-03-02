 
def multiplicativeCongruentialMethod(Xo, m, a, randomNums, noOfRandomNums): 
    randomNums[0] = Xo 
    for i in range(1, noOfRandomNums): 
        randomNums[i] = (randomNums[i - 1] * a) % m 
if __name__ == '__main__': 
    Xo = 3 
    m = 15 
    a = 7 
    noOfRandomNums = 10
    randomNums = [0] * (noOfRandomNums) 
    multiplicativeCongruentialMethod(Xo, m, a, randomNums, noOfRandomNums) 
    for i in randomNums: 
        print(i, end = " ") 