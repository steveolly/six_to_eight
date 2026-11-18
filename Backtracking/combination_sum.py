def combination_sum(candidates, target):
    result = []
    current = []

    def backtrack(rem, start):
        if rem == 0:
            result.append(current.copy())
            return

        for i in range(start, len(candidates)):
            num = candidates[i]
            if rem - num < 0:
                continue
            current.append(num)
            backtrack(rem-num, i)
            current.pop()

    backtrack(target, 0)

    return result


print(combination_sum([2, 3, 6, 7], 7))
print(combination_sum([2, 3, 5], 8))
print(combination_sum([6, 4, 2, 1, 5], 9))
