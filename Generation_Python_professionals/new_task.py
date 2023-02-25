from itertools import cycle

if __name__ == '__main__':
    days = ((day, name)for day, name in zip(range(1, 78), cycle(['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])))
    for elm in days:
        print(elm)