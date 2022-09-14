from collections import namedtuple
if __name__ == '__main__':
    Game = namedtuple('Game', 'name developer publisher')

    ExtendedGame = namedtuple('ExtendedGame', [*Game._fields, 'release_date', 'price'])
