def txt_to_dict():
    with open('planets.txt', 'r', encoding='utf-8') as planets_file:
        lines = (dict(tuple(elm.split(' = ')) for elm in line.split('\n')) for line in planets_file.read().split('\n\n'))
        return lines


if __name__ == '__main__':
    planets = txt_to_dict()

    print(next(planets))
    print(next(planets))
    print(next(planets))
