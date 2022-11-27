from collections import namedtuple


if __name__ == '__main__':

    Person = namedtuple('Person', ['name', 'nationality', 'sex', 'birth', 'death'])

    persons = [Person('E. M. Ashe', 'American', 'male', 1867, 1941),
               Person('Goran Aslin', 'Swedish', 'male', 1980, 0),
               Person('Erik Gunnar Asplund', 'Swedish', 'male', 1885, 1940),
               Person('Genevieve Asse', 'French', 'female', 1949, 0),
               Person('Irene Adler', 'Swedish', 'female', 2005, 0),
               Person('Sergio Asti', 'Italian', 'male', 1926, 0),
               Person('Olof Backman', 'Swedish', 'male', 1999, 0),
               Person('Alyson Hannigan', 'Swedish', 'female', 1940, 1987),
               Person('Dana Atchley', 'American', 'female', 1941, 2000),
               Person('Monika Andersson', 'Swedish', 'female', 1957, 0),
               Person('Shura_Stone', 'Russian', 'male', 2000, 0),
               Person('Jon Bale', 'Swedish', 'male', 1950, 0)]

    swedish_persons = (person for person in persons if person.nationality == 'Swedish')
    male_persons = (person for person in swedish_persons if person.sex == 'male')
    live_persons = (person for person in male_persons if person.death == 0)
    print(max(live_persons, key=lambda x: x.birth).name)
