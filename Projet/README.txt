## PROJET FINAL DE PHYSIQUE NUMÉRIQUE - PROPAGATION D'UN PAQUET D'ONDE ET MÉTHODE PSEUDO-SPECTRALE ##
## JORDAN CHAREST ET BENJAMIN CLAVEAU ##

Tous les fichiers .py nécessaires pour générer les simulations, les animations et les figures se trouvant dans le rapport final se trouvent dans ce dossier.

Contenu du dossier "Projet":

> anciennes_anims:
    Anciennes animations générées en .mp4. Pas à jour, des améliorations ou des modifications ont été apportées après.

> anciennes_figures:
    Anciennes figures générées en .mp4. Pas à jour, des améliorations ou des modifications ont été apportées après.

> animations:
    Animations à jour pour chaque potentiel

> figures:
    Figures à jour pour chaque potentiel

> Code:
    > alpha.py:
        Simulation de la particule alpha dans un noyau d'uranium 238. Script fonctionnel mais la méthode pseudo-spectrale ne permet pas de bien représenter la réalité
        avec la puissance de calcul dont nous disposons

    > etalement.py:
        Simulation de l'étalement d'un paquet d'onde

    > functions.py:
        Fonctions nécessaires au fonctionnement des simulations. Contient les fonctions iteration_temporelle, evolution_temporelle, energie et generate_animation

    > parabolique.py:
        Simulation de la propagation d'un paquet d'onde dans un potentiel parabolique

    > propag_libre.py:
        Simulation de la propagation libre d'un paquet d'onde

    > puits_infini.py:
        Simulation de la propagation d'un paquet d'onde dans un puits infini. Pas inclus dans le rapport car trop semblable au saut de potentiel.

    > puits-barr_pot.py:
        Simulation de la propagation d'un paquet d'onde dans un puits ou une barrière de potentiel.

    > saut_pot.py:
        Simulation de la propagation d'un paquet d'onde dans un saut (marche) de potentiel.