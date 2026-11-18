def generate_parentheses(n):
    result = []
    current = []

    def backtrack(open_count, close_count):
        if len(current) == (n * 2):
            result.append("".join(current.copy()))
            return
        if open_count < n:
            current.append("(")
            backtrack(open_count + 1, close_count)
            current.pop()
        if close_count < open_count:
            current.append(")")
            backtrack(open_count, close_count + 1)
            current.pop()
    backtrack(0, 0)
    return result


print(generate_parentheses(1))
print(generate_parentheses(2))
print(generate_parentheses(3))
print(generate_parentheses(4))
