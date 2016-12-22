# Sum the even Fibonacci numbers that don't exceed 4 million

def main():
    MAX_ITERATIONS = 4000000
    ans = 0
    current_num = 1
    next_num = 2
    while current_num <= MAX_ITERATIONS:
        # sum even numbers
        if current_num % 2 == 0:
            ans += current_num

        temp = current_num # needed as current_num gets updated before next_num
        current_num = next_num
        next_num = temp +  next_num # add previous and current numbers -> Fibonacci
    return ans

if __name__ == '__main__':
    ans = main()
    print(str(ans))
