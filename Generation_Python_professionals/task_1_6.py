import sys
if __name__ == '__main__':
    text = input()
    print(f"|{text:&^20}|")
    print(f"|{text:&>20}|")
    print(f"|{text:&<20}|")


