# dodawanie z przeniesieniem
def addc(a,b,c=0):
    ab = a + b + c # dodanie a, b i c gdzie c to bit przeniesienia

    # jesli suma wynosi wiecej niz dwa to ustawiamy bit przeniesienia
    if ab >= 2:
        c = 1 
        ab = ab%2
    else:
        c = 0

    return c, ab

# propagowanie przeniesienia
def propagate_carry(bits, start, carry):
    # iteracja po bitach od indeksu startowego
    i = start

    # propagowanie przeniesiania
    while carry > 0 and i < len(bits):
        #dodanie przeniesienia w odpowiednim miejscu i obliczenie nowego przeniesienia
        carry, bits[-1-i] = addc(bits[-1-i], carry, 0)
        i += 1
    return bits

# wykonanie odejmowania z pozyczka
def subc(x, y, borrow):
    # odejmowanie z pozyczka
    diff = x - y - borrow

    # jezeli roznica jest ujemna, ustawiamy pozyczke na 1 i dodajemy 2 do roznicy, aby uzyskac wynik dodatni
    if diff < 0:
        borrow = 1
        diff += 2
    else:
        borrow = 0

    return borrow, diff