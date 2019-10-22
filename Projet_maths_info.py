def find_seed(f, c=0, eps=2**(-26), x0=0) :
    def g(y) :
        return f(x0,y) - c
    if g(0)*g(1) > 0 : #dans ce cas, notre hypothèse n'est pas vérifiée.
        return None
    else :
        a, b = 0, 1
        while b-a >= 2*eps :
            m=(a+b)/2
            if g(m) >= 0 :
                b = m
            else :
                a = m
        return (a+b)/2 #Comme l'intervalle est de taille au plus 2*eps, on renvoit bien le 0 à + ou - eps.


def simple_contour_scan_X(f, c=0.0, delta=0.01) :
    abscisses = []
    ordonnées = []
    X = 0
    while X <= 1 :
        t = find_seed(f, c, x0 = X)
        if t != None :
            abscisses.append(X)
            ordonnées.append(t)
        X = X + delta
    return abscisses, ordonnées

abscisses = []
ordonnées = []
def simple_contour_carre_elementaire_initiale(f, c=0, delta=0.01, x0, y0) :  #Permet juste de trouver une autre racine sur les bords du carré de centre notre racine initiale (x0, y0)
    def find_seed_y0(f, c=0, eps=2**(-26), y0=0) :  #comme find_seed mais en faisant varier x à y0 fixé
        def g(x) :
            return f(x,y0) - c
        if g(0)*g(1) > 0 :
            return None
        else :
            a, b = 0, 1
            while b-a >= 2*eps :
                m=(a+b)/2
                if g(m) >= 0 :
                    b = m
                else :
                    a = m
            return (a+b)/2
    for x in [x0 + delta/2, x0 - delta/2] :
        t = find_seed(f, c, x0 = x)
        if t != None :
            return x, t
    for y in [y0 + delta/2, y0 - delta/2] :
        t = find_seed_y0(f, c, x0 = x)
        if t != None :
            return t, y
    return None

def simple_contour_carre_elementaire(f, c=0, delta=0.01, x0, y0, numcôté) :




def f(x,y) :
    return x**2 + y**2 -0.5


