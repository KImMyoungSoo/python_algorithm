def gcd(a,b) :
    if a > b :
        while b > 0 :
            a, b = b, a % b
        return a
    else :
        while a > 0 :
            b, a = a, b % a
        return b

a = 18
b = 48
print(gcd(a,b))