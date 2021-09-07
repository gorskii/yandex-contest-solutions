def min_substitutions_to_make_palindrome(s):
    """Return minimal number of substitutions to turn given string
    into a palindrome.
    """
    count = 0
    i, j = 0, len(s)-1
    while i < j:
        if s[i] != s[j]:
            count += 1
        i += 1
        j -= 1
    return count


if __name__ == '__main__':
    s = input()
    print(min_substitutions_to_make_palindrome(s))
