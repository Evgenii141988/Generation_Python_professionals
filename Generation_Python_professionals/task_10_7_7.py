if __name__ == '__main__':
    with open('data.csv', 'r', encoding='utf-8') as file_data:
        lines = (line.strip() for line in file_data)
        keys = next(lines).split(',')
        datas = (dict(zip(keys, line.split(','))) for line in lines)
        sum_round_a_invest = sum(int(data['raisedAmt']) for data in datas if data['round'] == 'a')
        print(sum_round_a_invest)