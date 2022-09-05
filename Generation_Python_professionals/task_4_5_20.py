from zipfile import ZipFile


def extract_this(zip_name: str, *args):
    files = args
    if len(files) == 0:
        with ZipFile(zip_name) as zip_file:
            zip_file.extractall()
    else:
        with ZipFile(zip_name) as zip_file:
            for file in files:
                zip_file.extract(file)

