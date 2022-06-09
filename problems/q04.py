def is_palindrome(n):
    return str(n) == str(n)[::-1]


def main():
    best = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            if is_palindrome(i * j):
                best = max(best, i * j)

    print(best)


if __name__ == "__main__":
    main()
