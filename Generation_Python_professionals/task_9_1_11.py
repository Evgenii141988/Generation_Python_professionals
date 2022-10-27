if __name__ == '__main__':
    names = ['Moana', 'Cars', 'Zootopia', 'Ratatouille', 'Coco', 'Inside Out', 'Finding Nemo', 'Frozen']
    budgets = [150000000, 120000000, 150000000, 150000000, 180000000, 175000000, 94000000, 150000000]
    box_offices = [643331111, 462216280, 1023784195, 620702951, 807082196, 857611174, 940335536, 1280802282]
    for cartoon in sorted(zip(names, budgets, box_offices), key=lambda x: x[0]):
        name, budget, box_office = cartoon
        print(f'{name}: {box_office - budget}$')