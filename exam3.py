def fibonacci (n):
    fib = []
    if n == 2:
        fib.append(0)
        fib.append(1)
        fib.append(1)
    if n > 2:
        fib.append(0)
        fib.append(1)
        fib.append(1)
        for i in range (2, n-1):
            fib.append(fib[i]+ fib[i-1])
    return fib


def main():
    num = int(input())
    print(fibonacci(num))


if __name__ == "__main__":
    main()