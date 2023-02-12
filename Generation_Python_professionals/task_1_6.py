def flatten_dict(d: dict) -> dict:
    result = {}

    def rec(d: dict, s: str = ''):
        for key, value in d.items():
            if type(value) == int:
                result[key if not s else f'{s}_{key}'] = value

            else:
                s = key if not s else f'{s}_{key}'
                rec(value, s)
                s = ''
    rec(d)
    return result


if __name__ == '__main__':
    assert flatten_dict({'Q': {'w': {'E': {'r': {'T': {'y': 123}}}}}}) == {'Q_w_E_r_T_y': 123}
    assert flatten_dict({'Germany_berlin': 7,
                         'Europe_italy_Rome': 3,
                         'USA_washington': 1,
                         'USA_New York': 4}) == {'Germany_berlin': 7, 'Europe_italy_Rome': 3, 'USA_washington': 1,
                                                 'USA_New York': 4}
    assert flatten_dict({'a': 100, 'b': 200}) == {'a': 100, 'b': 200}
    assert flatten_dict(
        {'Geeks': {'for': {'for': 1, 'geeks': 4}}, 'for': {'geeks': {'Geeks': 3}}, 'geeks': {'Geeks': {'for': 7}}}) == {
               'Geeks_for_geeks': 4, 'for_geeks_Geeks': 3, 'geeks_Geeks_for': 7, 'Geeks_for_for': 1}
    assert flatten_dict({"a": 1,
                         "b": {
                             "c": 2,
                             "d": 3,
                             "e": {
                                 "f": 4,
                                 '6': 100,
                                 '5': {"g": 6},
                                 "l": 1,
                             }
                         }}) == {'a': 1, 'b_c': 2, 'b_d': 3, 'b_e_f': 4, 'b_e_6': 100, 'b_e_5_g': 6, 'b_e_l': 1}
