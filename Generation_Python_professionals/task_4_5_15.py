from zipfile import ZipFile

if __name__ == '__main__':
    with ZipFile('workbook.zip') as zip_file:
        info = zip_file.infolist()
    result = min([file for file in info if file.file_size > 0],
                 key=lambda x: x.compress_size / x.file_size * 100)
    print(result.filename.split('/')[-1])