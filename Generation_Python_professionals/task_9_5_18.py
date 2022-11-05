def sourcetemplate(url: str):
    def inner(**kwargs):
        nonlocal url
        for i, key in enumerate(sorted(kwargs)):
            sym = '?' if i == 0 else '&'
            url += f'{sym}{key}={kwargs[key]}'

        return url

    return inner


if __name__ == '__main__':
    url = 'https://stepik.org/lesson/651459/step/14'
    load = sourcetemplate(url)
    print(load(thread='solutions', unit=648165))
