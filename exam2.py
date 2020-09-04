def main():
    letter = 0
    number = 0
    s = str(input())
    for i in range(0, len(s)):
        if s[i].isnumeric():
            number += 1
    letter = len(s) - number
    print (f"So chu so la: {number}")
    print (f"So chu cai la: {letter}")


if __name__ == "__main__":
    main()