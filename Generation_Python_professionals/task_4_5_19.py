from zipfile import ZipFile
import os.path

if __name__ == '__main__':
    file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
                  'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
                  'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']
    with ZipFile('files.zip', 'a') as zip_file:
        for file in file_names:
            if os.path.getsize(file) <= 100:
                zip_file.write(file)

