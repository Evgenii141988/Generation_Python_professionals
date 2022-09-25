import sys

if __name__ == '__main__':
    students = [tuple(student.strip().split()) for student in sys.stdin.readlines()]
    print(sorted(students, key=lambda x: int(x[1]))[1][0])
