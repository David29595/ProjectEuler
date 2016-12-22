# Largest Palindrome Product

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def main():
    i = 100
    j = 100
    ans = 0
    while (i <= 999):
        while (j <= 999):
            product = i * j
            if (product > ans and Palindrome(str(product))):
                ans = product
            j += 1
        j = 100
        i += 1
    return greatest

def Palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    ans = main()
    print(str(ans))
