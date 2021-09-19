# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 11:22:37 2019

@author: sebastian
"""


import numpy as np
while True:
    temp=int(input('imput colour temp: '))
    temp=temp/100
    #red
    if temp <=66:
        red=255
    else:
        red=temp-60
        red = 329.698727446 * (red ** -0.1332047592)
        if red <0:
            red=0
        elif red>255:
            red=255
    print(red/255)
    #green
    if temp <=66:
        green = temp
        green = 99.4708025861 * np.log(green) - 161.1195681661
        if green < 0:
            green = 0
        elif green > 255:
            green = 255
    else:
        green = temp - 60
        green = 288.1221695283 * (green ** -0.0755148492)
        if green < 0:
            green = 0
        if green > 255:
            green = 255
    print(green/255)
    #blkue
    if temp >=66:
        blue=255
    else:
        if temp <=19:
            blue=0
        else:
            blue=temp-10
            blue = 138.5177312231 * np.log(blue) - 305.0447927307
            if blue <0:
                blue=0
            elif blue>255:
                blue=255
    print(blue/255)







