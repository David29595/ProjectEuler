# Special Pythagorean triplet

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#       -> a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import math

def main(product):
    for a in range(1, product + 1):
        for b in range(1, product + 1):
            c = product - a - b

            if a ** 2 + b ** 2 == c ** 2:
                print(a, b, c)
                return (a * b *c)


if __name__ == '__main__':
    ans = main(1000)
    print(str(ans))
