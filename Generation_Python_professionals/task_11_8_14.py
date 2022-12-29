import sys
import re

if __name__ == '__main__':
    python_code = ''.join([string for string in sys.stdin])
    python_code = re.sub(r'[\n ]*\"{3}.*?\"{3}', '', python_code, flags=re.S)
    python_code = re.sub(r'\n?[ ]*#.*', '', python_code)

    print(python_code)
