def subsets(nums):

    result = []
    current = []

    def backtrack(index):
        if index == len(nums):
            result.append(current.copy())
            return

        current.append(nums[index])
        backtrack(index + 1)
        current.pop()
        backtrack(index + 1)

        return result
    return backtrack(0)


print(subsets([1, 2, 3]))
