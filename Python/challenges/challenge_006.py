# Sum square difference

# The sum of the squares of the first ten natural numbers is 385 -> 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is 3025 -> (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
def main():
    sum = 0
    squares = 0
    for i in range(1, 101):
        sum += i
        squares += i ** 2

    return (sum ** 2) - squares

if __name__ == '__main__':
    ans = main()
    print(str(ans))
