import json
if __name__ == '__main__':

    club1 = {"name": "FC Byern Munchen", "country": "Germany", "founded": 1900,
             "trainer": "Julian Nagelsmann", "gaolkeeper": "M. Neuer", "league_position": 1}

    club2 = {"name": "FC Barcelona", "country": "Spain", "founded": 1899,
             "trainer": "Xavier Creus", "gaolkeeper": "M. Ter Stegen", "league_position": 7}

    club3 = {"name": "FC Manchester United", "country": "England", "founded": 1878,
             "trainer": "Michael Carrick", "gaolkeeper": "D. De Gea", "league_position": 8}

    clubs = [club1, club2, club3]
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(clubs, file, indent='   ')