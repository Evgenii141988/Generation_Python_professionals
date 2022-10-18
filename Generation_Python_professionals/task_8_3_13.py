def tribonacci(n):
    cache = {1: 1, 2: 1, 3: 1}

    def trib_rec(n):
        result = cache.get(n)
        if result is None:
            result = trib_rec(n - 3) + trib_rec(n - 2) + trib_rec(n - 1)
            cache[n] = result
        return result

    return trib_rec(n)


if __name__ == '__main__':
    print(tribonacci(1))
    print(tribonacci(7))
    print(tribonacci(4))