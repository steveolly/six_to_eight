def digit_sum(n):
    if n == 0:
        return 0

    rem = n % 10
    n = n // 10

    return rem + digit_sum(n)


def main():
    print(digit_sum(0))
    print(digit_sum(7))
    print(digit_sum(1234))
    print(digit_sum(99999))


if __name__ == "__main__":
    main()
