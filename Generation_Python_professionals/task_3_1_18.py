from datetime import date

if __name__ == '__main__':
    quarters = {'Q1': (1, 2, 3), 'Q2': (4, 5, 6), 'Q3': (7, 8, 9), 'Q4': (10, 11, 12)}
    dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11),
             date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21),
             date(1666, 6, 6), date(1968, 5, 26)]
    for date in dates:
        month = date.month
        year = date.year
        for k, v in quarters.items():
            if month in v:
                print(f'{year}-{k}')
                break
