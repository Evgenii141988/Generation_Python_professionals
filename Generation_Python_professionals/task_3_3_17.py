from datetime import datetime

if __name__ == '__main__':
    with open('diary.txt', 'r', encoding='utf-8') as file:
        data_list = file.readlines()
    new_data = []
    s = ''
    for data in data_list:
        if data != '\n':
            s += data
        else:
            new_data.append(s)
            s = ''
    new_data.append(s + '\n')
    new_data_dict = {datetime.strptime(data[:17], '%d.%m.%Y; %H:%M'): data for data in new_data}
    sort_date = sorted(new_data_dict)
    for d in sort_date:
        print(new_data_dict[d])
