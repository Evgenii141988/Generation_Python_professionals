
def create_actor(data: dict = {'name': 'Райан', 'surname': 'Рейнольдс', 'age': 46}, **kwargs) -> dict:
    return data | kwargs


if __name__ == '__main__':
    print(create_actor())
    print(create_actor(height=190, movies=['Дедпул', 'Главный герой']))
    print(create_actor(name='Jack', age=20))
