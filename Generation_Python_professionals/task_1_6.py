import pprint

if __name__ == '__main__':
    name = input()
    print('IGNORE HIM!' if len(set(name)) % 2 != 0 else 'CHAT WITH HER!')
