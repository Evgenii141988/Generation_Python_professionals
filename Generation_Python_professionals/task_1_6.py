def cmp_prev(val, numbers=[]):
    if len(numbers) < 1:
        numbers.append(val)
        return False
    flag = val > sum(numbers[-2:])
    numbers.append(val)
    return flag


if __name__ == '__main__':
    assert cmp_prev(0) == False
    assert cmp_prev(1) == True
    assert cmp_prev(68) == True
    assert cmp_prev(57) == False
    assert cmp_prev(346) == True
    assert cmp_prev(4) == False
    assert cmp_prev(5) == False
    assert cmp_prev(10) == True
    assert cmp_prev(15) == False
    assert cmp_prev(-7) == False
    assert cmp_prev(8) == False
    assert cmp_prev(2) == True
    assert cmp_prev(-6) == False
    assert cmp_prev(-7) == False
    assert cmp_prev(-6) == True
    assert cmp_prev(0) == True
    assert cmp_prev(-5) == True
    assert cmp_prev(65) == True
    assert cmp_prev(456) == True
    assert cmp_prev(-678) == False
    assert cmp_prev(77) == True
