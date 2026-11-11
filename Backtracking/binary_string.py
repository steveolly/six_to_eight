def binary_strings(n):
    current = []
    result = []

    def backtrack():
        if len(current) == n:
            result.append("".join(current))
            return

        for digit in ["0", "1"]:
            current.append(digit)
            backtrack()
            current.pop()
    backtrack()
    return result


def main():
    print(binary_strings(0))
    print(binary_strings(1))
    print(binary_strings(2))
    # print(len(binary_strings(4)))


if __name__ == "__main__":
    main()
