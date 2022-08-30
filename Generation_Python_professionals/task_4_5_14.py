from zipfile import ZipFile

if __name__ == '__main__':
    with ZipFile('workbook.zip') as zip_file:
        info = zip_file.infolist()
        size_source_files = sum([file.file_size for file in info if file.file_size > 0])
        size_compressed_files = sum([file.compress_size for file in info if file.compress_size > 0])
    print(f'Объем исходных файлов: {size_source_files} байт(а)')
    print(f'Объем сжатых файлов: {size_compressed_files} байт(а)')
