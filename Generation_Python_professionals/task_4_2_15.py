import csv

if __name__ == '__main__':
    domains = {}
    columns = ['domain', 'count']
    with open('data.csv', 'r', encoding='utf-8') as file:
        rows = csv.DictReader(file)
        for row in rows:
            email = row['email']
            index = email.find('@')
            domain = email[index + 1:]
            domains[domain] = domains.get(domain, 0) + 1
    domains_sort = sorted(domains, key=lambda x: (domains[x], x))
    data = [[domain, domains[domain]] for domain in domains_sort]
    with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        writer.writerows(data)
