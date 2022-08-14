import csv

if __name__ == '__main__':
    with open('titanic.csv', 'r', encoding='utf-8') as file:
        rows = list(csv.DictReader(file, delimiter=';'))
        men = [row['name'] for row in rows if row['survived'] == '1' and float(row['age']) < 18 and row['sex'] == 'male']
        women = [row['name'] for row in rows if row['survived'] == '1' and float(row['age']) < 18 and row['sex'] == 'female']
        print(*men, sep='\n')
        print(*women, sep='\n')
