import math

def main():
    n = 600851475143
    maxPrime = -1
    while n % 2 == 0:
        maxPrime = 2
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n = n / i
        if n == 1:
            break;
    if n > 2:
        maxPrime = n
    print(int(maxPrime))

if __name__ == '__main__':
    main()
