#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TP reconstruction TDM (CT)
# Prof: Philippe Després
# programme: Dmitri Matenine (dmitri.matenine.1@ulaval.ca)


# libs
import numpy as np
import time

# local files
import geometry as geo
import util as util
import CTfiltre as CTfiltre

## créer l'ensemble de données d'entrée à partir des fichiers
def readInput():
    # lire les angles
    [nbprj, angles] = util.readAngles(geo.dataDir+geo.anglesFile)

    print("nbprj:",nbprj)
    print("angles min and max (rad):")
    print("["+str(np.min(angles))+", "+str(np.max(angles))+"]")

    # lire le sinogramme
    [nbprj2, nbpix2, sinogram] = util.readSinogram(geo.dataDir+geo.sinogramFile)

    if nbprj != nbprj2:
        print("angles file and sinogram file conflict, aborting!")
        exit(0)

    if geo.nbpix != nbpix2:
        print("geo description and sinogram file conflict, aborting!")
        exit(0)

    return [nbprj, angles, sinogram]


## reconstruire une image TDM en mode retroprojection
def laminogram():
    
    [nbprj, angles, sinogram] = readInput()

    # initialiser une image reconstruite
    image = np.zeros((geo.nbvox, geo.nbvox))

    # "etaler" les projections sur l'image
    # ceci sera fait de façon "voxel-driven"
    # pour chaque voxel, trouver la contribution du signal reçu
    for j in range(geo.nbvox): # colonnes de l'image
        print("working on image column: "+str(j+1)+"/"+str(geo.nbvox))
        for i in range(geo.nbvox): # lignes de l'image
            for a in range(len(angles)):
                x = (j - geo.nbvox / 2) * geo.voxsize
                y = (i - geo.nbvox / 2) * geo.voxsize
                r = np.sqrt(x**2 + y**2)
                if y < 0:
                    theta_vox = np.arctan(x / y)
                elif y == 0 and x <= 0:
                    theta_vox = np.pi / 2
                elif y == 0 and x > 0:
                    theta_vox = 3 * np.pi / 2
                else:
                    theta_vox = np.arctan(x / y) + np.pi
                theta = theta_vox - angles[a]
                distance_rayon = r * np.sin(theta) / geo.pixsize
                indice_rayon = int(geo.nbpix / 2 + np.round(distance_rayon))

                image[i, j] += sinogram[a][indice_rayon]
                
    util.saveImage(image, "lam")


## reconstruire une image TDM en mode retroprojection filtrée
def backproject():
    
    [nbprj, angles, sinogram] = readInput()
    
    # initialiser une image reconstruite
    image = np.zeros((geo.nbvox, geo.nbvox))
    
    ### option filtrer ###
    CTfiltre.filterSinogram(sinogram)
    ######
    
    # "etaler" les projections sur l'image
    # ceci sera fait de façon "voxel-driven"
    # pour chaque voxel, trouver la contribution du signal reçu
    for j in range(geo.nbvox): # colonnes de l'image
        print("working on image column: "+str(j+1)+"/"+str(geo.nbvox))
        for i in range(geo.nbvox): # lignes de l'image
            for a in range(len(angles)):
                x = (j - geo.nbvox / 2) * geo.voxsize
                y = (i - geo.nbvox / 2) * geo.voxsize
                r = np.sqrt(x**2 + y**2)
                if y < 0:
                    theta_vox = np.arctan(x / y)
                elif y == 0 and x <= 0:
                    theta_vox = np.pi / 2
                elif y == 0 and x > 0:
                    theta_vox = 3 * np.pi / 2
                else:
                    theta_vox = np.arctan(x / y) + np.pi
                theta = theta_vox - angles[a]
                distance_rayon = r * np.sin(theta) / geo.pixsize
                indice_rayon = int(geo.nbpix / 2 + np.round(distance_rayon))

                image[i, j] += sinogram[a][indice_rayon]
    
    util.saveImage(image, "fbp")
