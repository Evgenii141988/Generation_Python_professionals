import json

if __name__ == '__main__':
    with open('data1.json', 'r', encoding='utf-8') as file1:
        data1 = json.load(file1)
    with open('data2.json', 'r', encoding='utf-8') as file2:
        data2 = json.load(file2)
    new_data = data1 | data2
    with open('data_merge.json', 'w', encoding='utf-8') as file:
        json.dump(new_data, file, indent='   ')