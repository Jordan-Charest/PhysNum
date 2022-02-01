# Erreur sur l'intégration par la méthode des trapèzes selon l'équation d'Euler-Maclaurin


def erreur_trapeze(f, N, a, b):
    return 1/12 * (N / (b - a))**2 * (f(a) - f(b))


# dérivée déterminée analytiquement À AJOUTER

