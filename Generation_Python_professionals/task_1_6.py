if __name__ == '__main__':
    one = input()
    two = input()
    experiment = 'Притягиваются' if one in ('N', 'S') and two in ('N', 'S') and one != two else 'Отталкиваются'
    print(experiment)
