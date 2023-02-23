from string import ascii_lowercase
import json

if __name__ == '__main__':
    alphabet = {lit: i for i, lit in enumerate(ascii_lowercase, 1)}
    json_data = json.dumps(alphabet, indent=3)
    print(json_data)