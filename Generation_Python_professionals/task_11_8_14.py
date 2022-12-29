import sys
import re


if __name__ == '__main__':
    python_code = ''.join([string for string in sys.stdin])
    python_code = re.sub(r'\"{3}.*\"{3}\s*', '', python_code, flags=re.S)
    python_code = re.sub(r'#.*\s*', '\n', python_code)

    print(python_code)