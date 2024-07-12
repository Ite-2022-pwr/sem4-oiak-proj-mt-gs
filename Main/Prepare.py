x, y = 0, 1 # inicjalizacja zmiennych globalnych

# rozszerzony algorytm euklidesa dla najwiekszego wspolnego dzielnika
def gcdExtended(a, b):
    global x, y # deklaracja zmiennych
    
    # przypadek bazowy - gdy a osiagnie 0, zwracamy b oraz ustawiamy x=0, y=1
    if (a == 0):
        x = 0
        y = 1
        return b
 
    # rekurencyjne wywolanie funkcji dla a = b % a
    gcd = gcdExtended(b % a, a)

    # zapisanie wynikow rekurenyjnego wywolania
    x1 = x
    y1 = y
 
    # aktualizacja x i y przy użyciu wynikow rekurencyjnego wywoania
    x = y1 - (b // a) * x1
    y = x1
 
    # zwrocenie wartosci nwd
    return gcd
 

 # obliczenie odwrotnosci modularnej
def modInverse(R, N): 
    g = gcdExtended(R, N) # wywolanie rozszerzonego algorytmu euklidesa dla R i N
    
    # sprawdzenie czy odwrotnosc istnieje
    if (g != 1):
        #print("Inverse doesn't exist")
        return 0

    else:
 
        # obliczenie odwrotnosci modularnej z uwzglednieniem wartosci ujemnych x
        res = (x % N + N) % N
        return res
    

# przygotowanie algorytmu montgomery'ego
def PrepareMontgomery(n):
    n_bin = bin(n)[2:] # konwersja na postac binarna i pominiecie prefiksu '0b'
    k = len(n_bin) # obliczenie liczby bitow w n
    r = 2 ** k # obliczenie r jako 2^k

    r_inv = modInverse(r, n) # obliczenie odwrotnosci modulo
    np = -(1 - r * r_inv) // n # obliczenie wartosci np
    return k, r, np