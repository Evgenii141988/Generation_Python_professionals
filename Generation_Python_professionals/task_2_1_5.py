def convert(string: str) -> str:
    lowers = [s for s in string if s.islower()]
    uppers = [s for s in string if s.isupper()]
    return string.lower() if len(lowers) >= len(uppers) else string.upper()


if __name__ == '__main__':
    print(convert('BEEgeek'))
    print(convert('pyTHON'))
    print(convert('pi31415!'))