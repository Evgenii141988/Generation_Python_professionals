from datetime import date


def date_formatter(country_code: str):
    def inner(my_date: date):
        date_format = {'ru': '%d.%m.%Y',
                       'us': '%m-%d-%Y',
                       'ca': '%Y-%m-%d',
                       'br': '%d/%m/%Y',
                       'fr': '%d.%m.%Y',
                       'pt': '%d-%m-%Y'}
        return my_date.strftime(date_format[country_code])

    return inner


if __name__ == '__main__':
    date_ru = date_formatter('ru')
    today = date(2022, 1, 25)
    print(date_ru(today))

    date_ru = date_formatter('us')
    today = date(2025, 1, 5)
    print(date_ru(today))
