if __name__ == '__main__':
    l1 = input()
    l2 = input()
    l3 = input()
    en_str = 'AaBCcEeHKMOoPpTXxy'
    ru_str = 'АаВСсЕеНКМОоРрТХху'
    if all((l in en_str for l in [l1, l2, l3])):
        print('en')
    elif all((l in ru_str for l in [l1, l2, l3])):
        print('ru')
    else:
        print('mix')
