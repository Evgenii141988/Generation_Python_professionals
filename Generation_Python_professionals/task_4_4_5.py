import json


def is_correct_json(string: str) -> bool:
    try:
        data = json.loads(string)
        return True
    except json.decoder.JSONDecodeError:
        return False


if __name__ == '__main__':
    data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'

    print(is_correct_json(data))
    print(is_correct_json('number = 17'))