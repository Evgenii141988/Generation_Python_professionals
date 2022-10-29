def hash_as_key(objects: list) -> dict:
    hash_dict = {}
    for obj in objects:
        if hash(obj) in hash_dict:
            if type(hash_dict[hash(obj)]) == list:
                hash_dict[hash(obj)].append(obj)
                continue
            hash_dict[hash(obj)] = [hash_dict[hash(obj)]] + [obj]
        else:
            hash_dict[hash(obj)] = obj
    return hash_dict


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 5]

    print(hash_as_key(data))
    data = [-1, -2, -3, -4, -5]

    print(hash_as_key(data))
    data = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]

    print(hash_as_key(data))
