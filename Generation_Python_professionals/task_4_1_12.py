import sys

if __name__ == '__main__':
    heights = [int(height.strip()) for height in sys.stdin]
    if heights:
        print(f'Рост самого низкого ученика: {min(heights)}')
        print(f'Рост самого высокого ученика: {max(heights)}')
        print(f'Средний рост: {sum(heights) / len(heights) }')
    else:
        print('нет учеников')