from zipfile import ZipFile


if __name__ == '__main__':
    with ZipFile('workbook.zip') as zip_file:
        info = zip_file.infolist()
        resul = [file for file in info if file.file_size > 0]
    print(len(resul))