def is_palindrome(s):

    def helper(left, right):

        if left >= right:
            return True

        if not s[left].isalnum():
            return helper(left + 1, right)

        if not s[right].isalnum():
            return helper(left, right - 1)

        if s[left].lower() != s[right].lower():
            return False

        return helper(left + 1, right - 1)

    return helper(0, len(s) - 1)


def main():
    print(is_palindrome("racecar"))   # True
    print(is_palindrome("A man, a plan, a canal: Panama"))   # True
    print(is_palindrome("hello"))   # False
    print(is_palindrome(""))


if __name__ == "__main__":
    main()
