def gcd_Euclidean(a, b):
    num = [a, b]
    num.sort()
    while num[0] * num[1] > 0:
        num[1] -= num[0]
        num.sort()
        if num[0] == num[1]:
            return num[0]
    print('The 2 numbers dont have gcd')

print(gcd_Euclidean(66528,52920))
