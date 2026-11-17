def two_conbinations(letters):
    result = []
    current = []

    def backtrack():
        if len(current) == 2:
            result.append("".join(current.copy()))
            return

        for i in letters:
            current.append(i)
            backtrack()
            current.pop()
        return result
    return backtrack()


print(two_conbinations(['a', 'b', 'c', 'd']))
