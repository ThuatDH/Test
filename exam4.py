import math
def findNguyento (n):
    # so nguyen n < 2 khong phai la so nguyen to
    if (n < 2):
        return False
 
    # check so nguyen to khi n >= 2
    squareRoot = int(math.sqrt(n))
    for i in range(2, squareRoot + 1):
        if (n % i == 0):
            return False
    return True


def main():
    for j in range(10000, 100000):
        if findNguyento(j):
            print (j, end=", ")



if __name__ == "__main__":
    main()