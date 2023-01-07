import sys

    if __name__ == '__main__':
        numbers = [-214, 777, 181, 9, 32, -139, 43, 89, 77, 448, -20, -917, 54, 5, 432, 43, 32, 422, -895, 7, 198, 284, 472,
                   3, -986, -964, -989, 29]
        elements = (3, 5, 7, 9)
        for elm in elements:
            numbers.remove(elm)
        print(numbers)
        numbers.sort(reverse=True)