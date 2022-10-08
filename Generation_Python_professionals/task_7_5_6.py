def is_good_password(string: str) -> bool:
    return all([len(string) >= 9, any([lit.isupper() for lit in string]), any([lit.islower() for lit in string]),
                any([lit.isdigit() for lit in string])])


if __name__ == '__main__':
    print(is_good_password('41157082'))
    print(is_good_password('мойпарольсамыйлучший'))
    print(is_good_password('МойПарольСамыйЛучший111'))
    print(is_good_password('4abcdABC'))
