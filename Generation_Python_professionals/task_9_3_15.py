if __name__ == '__main__':
    fib = lambda n: 1 if n <= 2 else fib(n - 1) + fib(n - 2)
    print(fib(1))
    print(fib(2))
    print(fib(5))
    print(fib(6))
    print(fib(7))
