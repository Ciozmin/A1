import math

def prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

n = int(input())

a = 2
b = 3

while not (a <= n <= b):
    x = b + 1
    while not prime(x):
        x += 1
    a = b
    b = x

if abs(a - n) <= abs(b - n):
    print(a)
else:
    print(b)

#we initialize a and b as the smallest 2 prime numbers and using x and the 'prime' function, we find the next biggest prime function
#which we use to update a and b, until n is between a and b, meaning we have the biggest prime smaller than n and the smallest prime bigger than n
#then, print the one that's closer to n