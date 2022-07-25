
class File:
    EXTENSION = set()

    def __init__(self, name: str, extension: str, size: int, units: str):
        self.name = name
        self.extension = extension
        if units == 'B':
            self.size = size
        elif units == 'KB':
            self.size = size * 1024
        elif units == 'MB':
            self.size = size * 1024 * 1024
        elif units == 'GB':
            self.size = size * 1024 * 1024 * 1024
        self.units = 'B'
        self.EXTENSION.add(extension)


def get_size(size: int) -> tuple:
    if 0 <= size < 1024:
        return size, 'B'
    elif 1024 <= size < 1024 * 1024:
        return round(size / 1024), 'KB'
    elif 1024 * 1024 <= size < 1024 * 1024 * 1024:
        return round(size / (1024 * 1024)), 'MB'
    else:
        return round(size / (1024 * 1024 * 1024)), 'GB'


if __name__ == '__main__':
    with open('files.txt', 'r', encoding='utf-8') as file:
        files_gen = ([string.split('.') if i == 0 else string for i, string in enumerate(file.strip('\n').split())] for
                     file in file.readlines())
        files_obj = [File(file[0][0], file[0][1], int(file[1]), file[2]) for file in files_gen]
        extensions = list(files_obj[0].EXTENSION)
        extensions.sort()
        for ex in extensions:
            files_obj_ex = [file for file in files_obj if file.extension == ex]
            files_obj_ex.sort(key=lambda x: x.name)
            size_sum = sum((file.size for file in files_obj_ex))
            for file in files_obj_ex:
                print(f'{file.name}.{file.extension}')
            size, extension = get_size(size_sum)
            print('-' * 10)
            print(f'Summary: {size} {extension}')
            # print(f'Summary: {size_sum}')
            print()
