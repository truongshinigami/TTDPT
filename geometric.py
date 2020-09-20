# 1.a
#prob
import math

def prob(n,p):
        return math.pow(1-p, n - 1)*p      
n = 1
p = 0.5
Pb = prob(n,p)
print("Pr { X = %.2f} = %.2f" % (n, Pb))

#infoMeasure
def infoMeasure(n, p) :
    P_x = prob(n,p)
    print ("l(x) = %.2f" % -math.log(P_x))
infoMeasure(5,0.5)

#Sum Probability
def sumProb(n, p) :
    sum = 0
    for i in range(1,n+1):
        sum = sum + prob(i,p)
    print ("sum of probability = %.2f" % sum)
sumProb(5,0.5)

def  approxEntropy(n,p) :
    sum = 0 
    for i in range(1, n+1):
        sum = sum + (-math.log(prob(i,p))*prob(i,p))
    print ("Entropy = %.2f" % sum)
approxEntropy(5,0.5)