def spell(*args) -> dict:
    litters = {}
    if args:
        words = [s.lower() for s in args]
        for word in words:
            key = word[0]
            value = len(word)
            litters[key] = value if litters.get(key, 0) < value else litters.get(key)
        return litters
    return litters


if __name__ == '__main__':
    words = ['россия', 'Австрия', 'австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']

    print(spell(*words))
    print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))