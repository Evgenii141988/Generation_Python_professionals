import sys

if __name__ == '__main__':
    print(*[line.strip()[::-1] for line in sys.stdin], sep='\n')