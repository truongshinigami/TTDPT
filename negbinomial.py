import math
n = 5
p = 0.5
N = 3
r = 2

def prob(n, p, N, r) :
    factr = 1
    factN = 1
    factrN = 1
    for i in range(1,r) :
        factr = factr*i
    for i in range(1,N+1) :
        factN = factN*i
    for i in range(1,N+r) :
        factrN = factrN*i
    P_x =  math.pow(1-p, N)*math.pow(p,r)
    return (factrN/(factr*factN)*P_x)
print ("P(x) = %.2f" % prob(n, p, N, r) )

def sumProb(n,p,N,r) :
    sum = 0
    for i in range(1,N+1) :
        sum = sum + prob(n,p,i,r)
    print ("Sum of probability = %.2f" % sum)
sumProb(n,p,N,r)

def  approxEntropy(n,p, N,r) :
    sum = 0 
    for i in range(1,N+1) :
        sum = sum + (prob(n, p, i,r)*math.log(prob(n, p, i,r)))
    print("Entropy = %.2f" % sum)
approxEntropy(n,p,N,r)