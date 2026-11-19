def permutations(nums):
    result = []
    current = []
    position = [False] * len(nums)

    def backtrack():
        if len(current) == len(nums):
            result.append(current.copy())
            return

        for i in range(len(nums)):
            if position[i]:
                continue

            current.append(nums[i])
            position[i] = True
            backtrack()
            current.pop()
            position[i] = False

    backtrack()

    return result


print(permutations([1, 2, 3]))
print(permutations([2, 3, 2]))
print(permutations([2, 2]))
