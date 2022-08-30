from zipfile import ZipFile
from datetime import datetime


if __name__ == '__main__':
    my_date = datetime(2021, 11, 30, 14, 22)
    with ZipFile('workbook.zip') as zip_file:
        info = zip_file.infolist()
        files = sorted([file.filename.split('/')[-1] for file in info if file.file_size > 0 and datetime(*file.date_time) > my_date])
    print(*files, sep='\n')



