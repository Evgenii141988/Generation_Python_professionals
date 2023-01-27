import pprint

if __name__ == '__main__':
    words = ['feel', 'graduate', 'movie', 'fashionable', 'bacon',
             'drop', 'produce', 'acquisition', 'cheap', 'strength',
             'master', 'perception', 'noise', 'strange', 'am']
    words_with_position = [(elm, i) for i, elm in enumerate(words, 1)]
    print(words_with_position)
