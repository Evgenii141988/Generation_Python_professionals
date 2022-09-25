from collections import Counter

if __name__ == '__main__':
    data = Counter(
        'aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')
    data.min_values = lambda: [elem for elem in data.items() if elem[1] == min(data.items(), key=lambda x: x[1])[1]]
    data.max_values = lambda: [elem for elem in data.items() if elem[1] == max(data.items(), key=lambda x: x[1])[1]]
    print(data.min_values())
    print(data.max_values())