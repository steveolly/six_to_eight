# Backtracking for subset

# def backtrack(index, current, numbers):
#     if index == len(numbers):
#         print(current)
#         return

#     current.append(numbers[index])
#     backtrack(index+1, current, numbers)
#     current.pop()

#     backtrack(index+1, current, numbers)


# numbers = [1, 2, 3]
# backtrack(0, [], numbers)


def subset(numbers):
    result = []

    def backtrack(start_index, current_subset):
        result.append(current_subset.copy())

        for i in range(start_index, len(numbers)):
            current_subset.append(numbers[i])

            backtrack(i+1, current_subset)

            current_subset.pop()
    backtrack(0, [])
    return result


print(subset([1, 2, 3]))
