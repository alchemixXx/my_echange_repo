import _wpf





SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
print(SUITE)
print(RANKS)

def full_deck():
    full_deck = []
    for a in SUITE:
        for b in RANKS:
            full_deck.append(a+b)
    return full_deck
print(len(full_deck()))
