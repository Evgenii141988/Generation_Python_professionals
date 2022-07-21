def hide_card(card_number: str):
    result = '*' * 12
    card_number = card_number.replace(' ', '')
    return result + card_number[12:]


if __name__ == '__main__':
    card = '905 678123 45612 56'
    print(hide_card(card))