if __name__ == '__main__':
    n = int(input())
    staff = {}
    for _ in range(n):
        email = input()
        name_with_num, mail = email.split('@')
        number = ''
        name = ''
        for s in name_with_num:
            if s.isdigit():
                number += s
            else:
                name += s
        staff[name] = staff.get(name, []) + [number]
    # print(staff)
    m = int(input())
    for _ in range(m):
        name_staff = input()
        gen = (i for i in range(1, 10000))
        if name_staff not in staff:
            print(f'{name_staff}@beegeek.bzz')
            staff[name_staff] = staff.get(name_staff, []) + ['']
        else:
            if '' in staff[name_staff]:
                for i in gen:
                    if str(i) not in staff[name_staff]:
                        print(f'{name_staff}{i}@beegeek.bzz')
                        staff[name_staff] = staff.get(name_staff, []) + [str(i)]
                        break
            else:
                print(f'{name_staff}@beegeek.bzz')
                staff[name_staff] = staff.get(name_staff, []) + ['']
    # print(staff)
