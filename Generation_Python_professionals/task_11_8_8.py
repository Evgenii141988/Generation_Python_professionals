import re


def normalize_jpeg(filename: str) -> str:
    return re.sub(r'\.jpe?g$', r'.jpg', filename, flags=re.I)


if __name__ == '__main__':
    print(normalize_jpeg('stepik.jPeG'))
    print(normalize_jpeg('mountains.JPG'))
    print(normalize_jpeg('windows11.jpg'))
    print(normalize_jpeg('stepik.jpeg.jpeg'))