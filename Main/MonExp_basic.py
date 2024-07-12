import MonPro
import Prepare

# obliczenie potęgi a^e mod n
def MonExpNaive(a,e,n): 
    k, r, np = Prepare.PrepareMontgomery(n) # obliczenie  k, r, np
    ap = (a * r) % n # obliczenie ap
    up = (1 * r) % n # obliczenie up

    # wykonanie potegowania
    for i in range(k-1, -1, -1):

        # obliczenie MonPro
        up = MonPro.MonProNaive(up, up, n, r, np)

        # jesli e[i] wynosi 1 to wykonujemy operacje MonProNaive
        if (e >> i) & 1: 
            up = MonPro.MonProNaive(up, ap, n, r, np)
    # wykonianie ostatniej operacji MonProNaive w celu uzyskania wyniku, dlatego mnozymy przez 1        
    u = MonPro.MonProNaive(up, 1, n, r, np)
    return u