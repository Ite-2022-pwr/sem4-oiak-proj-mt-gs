import Prepare
import BinaryHelper

# funkcja realizujaca algortym CIOS
def CIOS(ap_bin, bp_bin, n_bin, np,s, w=1):
    # inicjalizacja t oraz u
    t = [0] * (2*s+1)
    u = t.copy()

    # algorytm, w ktorym krok mnozenia i redukcji jest zintegrowany
    for i in range(s):
        carry = 0
        for j in range(s):
            carry,sum = BinaryHelper.addc(int(t[-1-j]) , int(ap_bin[-1-j])*int(bp_bin[-1-i]) ,carry)
            t[-1-j] = sum
        
        carry, sum = BinaryHelper.addc(int(t[-1-s]),carry)
        t[-1-s] = sum
        t[-1-(s+1)] = carry
        carry = 0

        m = (int(t[-1])*int(np[-1])) % (2 ** w)

        for j in range(s):
            carry, sum = BinaryHelper.addc(int(t[-1-j]), int(m)*int(n_bin[-1-j]), carry)
            t[-1-j] = sum

        carry, sum = BinaryHelper.addc(int(t[-1-s]), carry)
        t[-1-s] = sum
        t[-1-(s+1)] = t[-1-(s+1)] + carry

        for j in range(s+1):
            t[-1-j] = t[-1-(j+1)]
            u[-1-j] = t[-1-(j+1)]

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
    np = bin(np)[2:]
    ap = (a * r) % n
    ap = bin(ap)[2:].zfill(s)
    up = (1 * r) % n
    up = bin(up)[2:].zfill(s)
    n = bin(n)[2:]
    for i in range(k-1, -1, -1):
        up = CIOS(up, up, n,np,s,w)
        if (e >> i) & 1: 
            up = CIOS(up, ap, n,np,s,w)
    tab_1 = [0]*s
    tab_1[-1] = 1
    u = CIOS(up, tab_1, n,np,s,w)
    return u
