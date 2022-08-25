import json
from datetime import datetime

if __name__ == '__main__':
    pattern = '%H:%M'
    my_start = datetime.strptime('10:00', pattern)
    my_end = datetime.strptime('12:00', pattern)
    with open('pools.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    monday_pools = []
    for elem in data:
        start, end = [datetime.strptime(t, pattern) for t in elem['WorkingHoursSummer']['Понедельник'].split('-')]
        if my_start >= start and my_end <= end:
            monday_pools.append(elem)
    my_pool = max(monday_pools, key=lambda x: (x['DimensionsSummer']['Length'], x['DimensionsSummer']['Width']))
    print(f"{my_pool['DimensionsSummer']['Length']}x{my_pool['DimensionsSummer']['Width']}\n{my_pool['Address']}")

