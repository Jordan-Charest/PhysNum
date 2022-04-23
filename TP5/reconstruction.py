#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TP reconstruction TDM (CT)
# Prof: Philippe Després
# programme: Dmitri Matenine (dmitri.matenine.1@ulaval.ca)


# libs
import numpy as np
import time
import math

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


## reconstruire une image TDM en mode retroprojection filtrée en déterminant 
## les valeurs d'atténation par interpolation linéaire
def backproject_interpol():
    
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
                if distance_rayon > 0:
                    indice_rayon1 = int(geo.nbpix / 2 + math.floor(distance_rayon))
                    indice_rayon2 = int(geo.nbpix / 2 + math.ceil(distance_rayon))
                else:
                    indice_rayon1 = int(geo.nbpix / 2 + math.ceil(distance_rayon))
                    indice_rayon2 = int(geo.nbpix / 2 + math.floor(distance_rayon))
                r1 = sinogram[a][indice_rayon1]
                r2 = sinogram[a][indice_rayon2]
                d = abs(distance_rayon) % 1 * geo.pixsize
                attenuation = geo.interpol_lin(r1, r2, d)

                image[i, j] += attenuation
    
    util.saveImage(image, "fbp")
