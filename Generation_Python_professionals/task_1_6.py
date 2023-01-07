import sys

if __name__ == '__main__':
    numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
    indexs = (-1, 0, 12, 7)
    sum_elements = sum(numbers.pop(i) for i in indexs)
    print(numbers)
    print(sum_elements)