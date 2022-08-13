import csv

if __name__ == '__main__':
    companies = {}
    with open('salary_data.csv', 'r', encoding='utf-8') as file:
        rows = csv.DictReader(file, delimiter=';')
        for row in rows:
            companies[row['company_name']] = companies.get(row['company_name'], [0, 0])
            companies[row['company_name']][0] += int(row['salary'])
            companies[row['company_name']][1] += 1
    companies_sort_list = sorted(companies, key=lambda x: (companies[x][0] / companies[x][1], x))
    print(*companies_sort_list, sep='\n')