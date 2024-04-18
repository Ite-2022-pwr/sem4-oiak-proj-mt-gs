import Prepare
import BinaryHelper

# funkcja realizujaca algorytm SOS
def sos(ap_bin,bp_bin,n_bin,np,s, w=1):
    # inicjalizacja t oraz u
    t = [0]*(2*s+1)
    u = t.copy()

    # krok 1: obliczenie t = a*b
    for i in range(s):
        carry =  0
        for j in range (s):
            carry,sum = BinaryHelper.addc(int(t[-1-(i+j)]) , int(ap_bin[-1-j])*int(bp_bin[-1-i]) ,carry)
            t[-1-(i+j)] = sum
        t[-1-(i+s)]=carry
  
    # krok 2: obliczenie u = (t + mn)/r
    # krok 2.1: t = t + mn    
    for i in range(s):
        carry = 0
        m = (int(t[-1-i])*int(np[-1])) % (2 ** w)
        for j in range(s):
            carry,sum = BinaryHelper.addc(int(t[-1-(i+j)]),int(m)*int(n_bin[-1-j]),carry)
            t[-1-(i+j)] = sum

        t = BinaryHelper.propagate_carry(t, i+s, carry)
        

    # krok 2.2: u = u/r (pomijamy nizsze s bitow)
    for j in range(s+1):
        u[-1-j] = t[-1-(j+s)]
        
    # krok 3: odejmowanie w celu redukcji u
    borrow = 0
    for i in range (s):
        borrow, diff = BinaryHelper.subc(u[-1-i],int(n_bin[-1-i]),borrow)
        t[-1-i] = diff
    borrow, diff = BinaryHelper.subc(u[-1-s],0,borrow)
    t[-1-s] = diff
    
    # zwrocenie wyniku algorytmu SOS
    if borrow == 0:
        return t
    else:
        return u
    

# obliczenie a^e mod n
def MonExp(a,e,n,w=1):
    k, r, np = Prepare.PrepareMontgomery(n)
    s = k // w
    np = bin(np)[2:]
    ap = (a * r) % n
    ap = bin(ap)[2:].zfill(s)
    up = (1 * r) % n
    up = bin(up)[2:].zfill(s)
    n = bin(n)[2:]
    for i in range(k-1, -1, -1):
        up = sos(up, up, n,np,s,w)
        if (e >> i) & 1:
            up = sos(up, ap, n,np,s,w)
    tab_1 = [0]*s
    tab_1[-1] = 1
    u = sos(up, tab_1, n,np,s,w)
    return u
