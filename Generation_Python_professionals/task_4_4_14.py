import csv
import json
from datetime import datetime


if __name__ == '__main__':
    students = []
    students_dict = {}
    pattern = "%Y-%m-%d %H:%M:%S"
    with open('exam_results.csv', 'r', encoding='utf-8') as file:
        rows = csv.DictReader(file)
        for row in rows:
            key = row['email']
            students_dict[key] = students_dict.get(key, []) + [row]
    sort_emails = sorted(students_dict)
    for email in sort_emails:
        students.append(max(students_dict[email], key=lambda x: (int(x['score']), datetime.strptime(x['date_and_time'], pattern))))
    for student in students:
        student['best_score'] = int(student.pop('score'))
    with open('best_scores.json', 'w', encoding='utf-8') as file_json:
        json.dump(students, file_json, indent='   ')