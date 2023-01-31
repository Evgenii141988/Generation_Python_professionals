# объявление функции
def generate_fizz_buzz_list(n: int):
    result = []
    for i in range(1, n + 1):
        match i:
            case int() if i % 3 == 0 and i % 5 == 0:
                result.append('FizzBuzz')
            case int() if i % 3 == 0:
                result.append('Fizz')
            case int() if i % 5 == 0:
                result.append('Buzz')
            case _:
                result.append(i)
    return result


if __name__ == '__main__':
    print(generate_fizz_buzz_list(3))
    print(generate_fizz_buzz_list(7))
    print(generate_fizz_buzz_list(15))
