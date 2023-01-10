if __name__ == '__main__':
    if (money := int(input())) <= 10000:
        print(f'Сумма {money} не превышает лимит, проходите')
    else:
        print(f'Ого! {money}! Куда вам столько? Мы заберем {money - 10000}')