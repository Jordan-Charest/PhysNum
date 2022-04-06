#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TP reconstruction TDM (CT)
# Prof: Philippe Després
# programme: Dmitri Matenine (dmitri.matenine.1@ulaval.ca)


# fichier contenant la description de la géométrie
# d'acquisition
# et de reconstruction

import numpy as np

### VARIABLES ###

### paramètres d'acquisition ###

## largeur d'un élément de détecteur (cm)
pixsize = 0.165

## taille du détecteur (nombre d'échantillons)
nbpix = 336

### paramètres de reconstruction ###

## taille de la grille d'image (carrée)
nbvox = 96 # options: 96, 192

## taille du voxel (carré) (cm)
voxsize = 0.4 # option: 0.4, 0.2

## fichiers d'entrée
dataDir = "./data/"
anglesFile = "angles.txt"
sinogramFile = "sinogram-patient.txt"

## Valeurs d'atténuation par interpolation linéaire
# 
# Arguments:
# rayon1, rayon2 : valeurs d'atténuation des deux rayons adjacents
# dist_centre_vox : distance perpendiculaire entre le rayon1
# et le centre du voxel [cm]
# 
# Retourne la valeur d'atténuation du voxel

def interpol_lin(rayon1, rayon2, dist_centre_vox):
    pente_interpol = (rayon2 - rayon1) / pixsize
    return rayon1 + dist_centre_vox * pente_interpol