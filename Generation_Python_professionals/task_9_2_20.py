import sys

if __name__ == '__main__':
    math_expressions = [eval(elm.strip()) for elm in sys.stdin.readlines()]
    print(max(math_expressions))


