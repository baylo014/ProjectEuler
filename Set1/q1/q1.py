import sys
import time
# Find the sum of all the multiples of 3 or 5 below 1000.
def main(num):
    sum = 0
    s = time.time()
    for i in range(1,num):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
    e = time.time()
    print("Total:",sum,"for",num)
    print("Time Taken:",e-s)
if __name__ == '__main__':
    if len(sys.argv) < 2:
        main(1000)
    else:
        main(int(sys.argv[1]))
