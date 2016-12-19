# sum all numbers between 1 and 1000 that are divisible by 3 and 5

def main():
    sum=0
    for i in range(1000):
        if i % 3 == 0 or i % 5 ==0:
            sum += i
    return str(sum)

if __name__ == '__main__':
    print(main())
