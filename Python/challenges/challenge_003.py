# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import math

def main(num):
    factors = []
    # True condition ok here as all numbers should have prime factors
    # so return should always exit the loop
    while True:
        n = spf(num)
        # n is a factor of num
        if n < num:
            factors.append(n)
            num = num // n
        else:
            factors.append(n)
            return num, factors


# smallest prime factor
def spf(num):
    # find smallest prime for a given number and return it
    # 2 is the lowest prime and getting the sqrt of num gives us an upper bound to look for factors
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return i
    # num is prime
    return num

if __name__ == '__main__':
    ans = main(600851475143)
    print(str(ans))
