from collections import Counter


def count_AGTC(dna: str) -> tuple:
    new_dna = Counter(dna)
    return tuple(new_dna[elm] if elm in new_dna else 0 for elm in 'AGTC' )

if __name__ == '__main__':
    print(count_AGTC('AGGTC'))
    print(count_AGTC('AAAATTT'))
    print(count_AGTC('AGTTTTT'))
    print(count_AGTC('CCT'))