import sys

if __name__ == '__main__':
    numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
    inserts = ((111, 5), (222, 8), (789, 0), (201, 11))
    for num, i in inserts:
        numbers.insert(i, num)
    print(numbers)