import Prepare
import BinaryHelper

# funkcja realizujaca algortym CIOS
def CIOS(ap_bin, bp_bin, n, w=1):
    # przygotowanie zmiennych z konwersja na system binarny
    k, _, np = Prepare.PrepareMontgomery(n)
    np = bin(np)[2:]
    n_bin = bin(n)[2:]

    # obliczenie dlugosci parametrow a i b
    s = k // w
    #print(ap_bin, bp_bin)

    # inicjalizacja t oraz u
    t = [0] * (2*s+1)
    u = t.copy()

    # algorytm, w ktorym krok mnozenia i redukcji jest zintegrowany
    for i in range(s):
        carry = 0
        for j in range(s):
            #print(t[-1-j],ap_bin[-1-j],bp_bin[-1-i],carry)
            carry,sum = BinaryHelper.addc(int(t[-1-j]) , int(ap_bin[-1-j])*int(bp_bin[-1-i]) ,carry)
            #print(t[-1-j],ap_bin[-1-j],bp_bin[-1-i],carry,sum)
            t[-1-j] = sum
        
        carry, sum = BinaryHelper.addc(int(t[-1-s]),carry)
        t[-1-s] = sum
        t[-1-(s+1)] = carry
        carry = 0

        #print(t)

        m = (int(t[-1])*int(np[-1])) % (2 ** w)

        for j in range(s):
            #print(t[-1-j],m,n_bin[-1-j],carry)
            carry, sum = BinaryHelper.addc(int(t[-1-j]), int(m)*int(n_bin[-1-j]), carry)
            t[-1-j] = sum

        #print(t)
        
        carry, sum = BinaryHelper.addc(int(t[-1-s]), carry)
        t[-1-s] = sum
        t[-1-(s+1)] = t[-1-(s+1)] + carry

        #print(t)

        for j in range(s+1):
            t[-1-j] = t[-1-(j+1)]
            u[-1-j] = t[-1-(j+1)]
        #print(t)
        #print(u)

    borrow = 0
    for i in range (s):
        borrow, diff = BinaryHelper.subc(u[-1-i],int(n_bin[-1-i]),borrow)
        t[-1-i] = diff
    borrow, diff = BinaryHelper.subc(u[-1-s],0,borrow)
    t[-1-s] = diff

    # zwrocenie wyniku algorytmu CIOS
    if borrow == 0:
        return t
    else:
        return u


# obliczenie a^e mod n
def MonExpCIOS(a,e,n,w=1): 
    k, r, np = Prepare.PrepareMontgomery(n)
    s = k // w
    ap = (a * r) % n
    ap = bin(ap)[2:].zfill(s)
    up = (1 * r) % n
    up = bin(up)[2:].zfill(s)
    for i in range(k-1, -1, -1):
        up = CIOS(up, up, n)
        if (e >> i) & 1: 
            up = CIOS(up, ap, n,)
    tab_1 = [0]*s
    tab_1[-1] = 1
    u = CIOS(up, tab_1, n)
    return u