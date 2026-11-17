def letter_case(s):
    result = []

    def build(i, current):
        if i == len(s):
            result.append("".join(current))
            return [""]

        if s[i].isalpha():
            current.append(s[i].lower())
            build(i+1, current)
            current.pop()
            current.append(s[i].upper())
            build(i+1, current)
            current.pop()
        else:
            current.append(s[i])
            build(i+1, current)
            current.pop()

        return result
    return build(0, [])


print(letter_case(""))
print(letter_case("12"))
print(letter_case("3z4"))
print(letter_case("a1b2"))
print(letter_case("a1b"))
print(letter_case("3a"))
