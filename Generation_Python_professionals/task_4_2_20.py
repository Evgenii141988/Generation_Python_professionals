import csv


if __name__ == '__main__':
    with open('student_counts.csv', 'r', encoding='utf-8') as file:
        rows = csv.DictReader(file)
        classes = []
        numbers = []
        for row in rows:
            if not classes:
                classes = ['year'] + sorted(list(row)[1:], key=lambda x: (int(x[0]) if len(x) == 3 else int(x[:len(x) - 2]), x[-1]))
            nums = []
            for cls in classes:
                nums.append(row[cls])
            numbers.append(nums)
    with open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(classes)
        writer.writerows(numbers)