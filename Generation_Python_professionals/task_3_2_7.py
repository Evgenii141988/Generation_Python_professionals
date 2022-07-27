from datetime import date


if __name__ == '__main__':
    andrew = date(1992, 8, 24)

    print(andrew.strftime('%Y-%m'))   # выводим дату в формате YYYY-MM
    print(andrew.strftime('%B (%Y)'))   # выводим дату в формате month_name (YYYY)
    print(andrew.strftime('%Y-%j'))   # выводим дату в формате YYYY-day_number