def find_keys(**kwargs):
    return sorted((key for key, value in kwargs.items() if isinstance(value, (list, tuple))), key=str.lower)


if __name__ == '__main__':
    words = input().split()
    print(all(['a' in word.lower() for word in words]))