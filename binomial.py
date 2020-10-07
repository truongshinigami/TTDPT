import math 
#binomial
n = 5
p = 0.5
N = 3

def prob(n, p, N) : 
    factn = 1
    factN = 1
    factnN = 1
    for i in range(1,n+1) :
        factn = factn*i
    for i in range(1,N+1) :
        factN = factN*i
    for i in range(1,n-N+1) :
        factnN = factnN*i
    P_x =  math.pow(1-p, n - N)*math.pow(p,N)
    return (factn/(factN*factnN)*P_x)

print ("Probability = %.2f" % prob (n,p,N))
#
def sumProb(n,p,N) :
    sum = 0
    for i in range(1,N+1) :
        sum = sum + prob(n,p,i)
    print ("Sum of probability = %.2f" % sum)
sumProb(n,p,N)

def  approxEntropy(n,p, N) :
    sum = 0 
    for i in range(1,N+1) :
        sum = sum + (prob(n, p, i)*math.log(prob(n, p, i)))
    print("Entropy = %.2f" % sum)
approxEntropy(n,p,N)