import pprint

if __name__ == '__main__':
    colors = ['White', 'Blue', 'Yellow', 'Purple', 'Black', 'Green']
    sizes = ['S', 'M', 'L', 'XL', 'XLL']
    result = [(color, size) for color in colors for size in sizes]
    print(result)


