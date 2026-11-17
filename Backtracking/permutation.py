def permutations(nums):
    current = []
    result = []
    used = [False] * len(nums)

    def backtrack():
        if len(current) == len(nums):
            result.append(current.copy())
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            current.append(nums[i])
            used[i] = True

            backtrack()

            current.pop()
            used[i] = False

        return result
    return backtrack()


print(permutations([1, 1, 3]))
