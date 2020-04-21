#Greatest Common Divisor
# Euclid's Algorithm.
def gcd(a, b):
    num = [a, b]
    num.sort()
    while num[0] * num[1] > 0:
        num[1] -= num[0]
        num.sort()
        if num[0] == num[1]:
            return num[0]
    print('The 2 numbers dont have gcd')

#print(gcd(66528,52920))
#========================================================#
#Extended GCD
def get_divisors(a):
    d = [i  for i in range(1,a+1) if a%i == 0]
    return d
#def get_v_u(p,q):

