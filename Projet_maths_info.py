def find_seed(f, c=0, eps=2**(-26)) :
    def g(y) :
        return f(0,y) - c
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


