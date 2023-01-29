def get_body_mass_index(weight: (int | float), height: (int | float)) -> str:
    index = weight / (height / 100) ** 2
    if index < 18.5:
        print("Недостаточная масса тела")
    elif index > 25:
        print("Избыточная масса тела")
    else:
        print("Норма")


if __name__ == '__main__':
    get_body_mass_index(70, 170)
