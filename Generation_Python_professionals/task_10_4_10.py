class PowerOf:
    def __init__(self, number):
        self.number = number
        self.pow = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.number ** self.pow
        self.pow += 1
        return result


if __name__ == '__main__':
    power_of_two = PowerOf(3)

    print(next(power_of_two))
    print(next(power_of_two))
    print(next(power_of_two))
    print(next(power_of_two))
    print(next(power_of_two))
    print(next(power_of_two))