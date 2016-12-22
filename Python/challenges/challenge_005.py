# Smallest multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def main():
    ans = 1 # lowest GCD value -> cannot divide by 0
    for i in range(1, 21):
        ans = ans * i // get_gcd(i, ans)
    return ans


# Euclidian Algorithm
def get_gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a


if __name__ == '__main__':
    ans = main()
    print(str(ans))
