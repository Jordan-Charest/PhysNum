#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TP reconstruction TDM (CT)
# Prof: Philippe Després
# programme: Dmitri Matenine (dmitri.matenine.1@ulaval.ca)


# libs
import numpy as np

# local files
import geometry as geo

## filtrer le sinogramme
## ligne par ligne
def filterSinogram(sinogram):
    for i in range(sinogram.shape[0]):
        sinogram[i] = filterLine(sinogram[i])

## filter une ligne (projection) via FFT
def filterLine(projection):
    F = np.fft.fft(projection)
    freq = np.fft.fftfreq(geo.nbpix, d=geo.pixsize)
    F = F * np.absolute(freq)
    return np.fft.ifft(F)
