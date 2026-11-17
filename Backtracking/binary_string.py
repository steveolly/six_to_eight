def binary_string(n):
    current = []
    result = []

    def backtrack():
        if len(current) == n:
            result.append("".join(current.copy()))
            return

        for i in ['0', '1']:
            current.append(i)
            backtrack()
            current.pop()
        return result

    return backtrack()


print(binary_string(4))
