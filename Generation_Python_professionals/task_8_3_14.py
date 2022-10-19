def is_palindrome(string: str) -> bool:
    if string != '' and string[0] != string[-1]:
        return False
    if len(string) <= 2:
        return True
    else:
        return is_palindrome(string[1:-1])


if __name__ == '__main__':
    print(is_palindrome('stepik'))
    print(is_palindrome('level'))
    print(is_palindrome('122333221'))
    print(is_palindrome(''))
