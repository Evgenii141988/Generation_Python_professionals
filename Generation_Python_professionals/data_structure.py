def detect_lucky(number: int) -> bool:
    return sum(map(int, str(number)[:3])) == sum(map(int, str(number)[3:]))

if __name__ == '__main__':
    print(detect_lucky(985778))
