# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 15:42:57 2017

@author: jeanmarie
"""

import math
import cmath
import numpy as npy

import scipy
from scipy import special
from scipy import signal
from scipy import ndimage

epsiherm=0.0001



###################################
def interferogramme( tabvignette, tabvignette2, *therest) :
    u"""
    Calcul de l'interférogramme entre deux images de même taille
    Par defaut la dimension de la fenetre est 3x3
    Renvoie une image complexe
    
    Mettre les deux pointeurs image en premier et second argument
    
    Argument 3 (facultatif) : la fenêtre sera carrée de dimension <argument 3>
    
    Arguments 3 et 4 (facultatifs) : la fenêtre sera rectangulaire de dimension <argument 3> x <argument 4>
    """
    dimx=5
    dimy=5
    
    if(len(therest)==1):        
        dimx=therest[0]
        dimy=dimx
        
    if(len(therest)==2):       
        dimx=therest[0]
        dimy=therest[1]
    
    nlig=npy.size(tabvignette,0)
    ncol=npy.size(tabvignette,1)
    print('Hi')   
    print(tabvignette.shape)
    print(tabvignette2.shape)

    if nlig != npy.size(tabvignette2,0)  :
        print(u'les deux images doivent avoir la même taille (%d  et %d)'%(nlig, npy.size(tabvignette2,0)))
        return 0
    
    if ncol != npy.size(tabvignette2,1)  :
        print(u'les deux images doivent avoir la même taille')
        return 0
    
    def moving_average_cmplx(interf):
        real_part = npy.real(interf).astype('float')
        imag_part = npy.imag(interf).astype('float')
        mvg_average_real = ndimage.uniform_filter(real_part, size=(dimx,dimy))
        mvg_average_imag = ndimage.uniform_filter(imag_part, size=(dimx,dimy))
        return mvg_average_real + 1j * (mvg_average_imag)

    
    interf= npy.multiply(tabvignette, npy.conj(tabvignette2))
    num = moving_average_cmplx(interf)

    master_pwr = moving_average_cmplx(npy.multiply(tabvignette, npy.conj(tabvignette)))
    slave_pwr = moving_average_cmplx(npy.multiply(tabvignette2, npy.conj(tabvignette2)))
    den = npy.sqrt(npy.multiply(master_pwr, slave_pwr))

    interfiltr = npy.divide(num, den)

    
    # part to be completed to compute a multi-look interfergram by averaging on a local window 
    # here interfiltr will contain only the mono-look interferogram !
    
    #interfiltr= npy.copy(interf)

    #
    
    return interfiltr
 
 
    
    
    
    
    
