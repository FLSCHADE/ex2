#!/usr/bin/python3
# -*- coding: utf-8 -*-


import cv2 as cv
import openCVTools as cvt
import numpy as np
import matplotlib.pyplot as plt

def REPLACE_THIS(input): return input


# load image
imgOriginal = cvt.safeLoad('/images/hummingbird_from_pixabay.png')
cvt.showImage("Original image", imgOriginal)


# TODO Aufgabe 1
'''
Konvertieren Sie das Bild in ein 1-Kanal Schwarzweiß(Grauton)-Bild.
Passen Sie die Funktionen `imageStats(..)` und `showImage(..)` so an, dass sie sowohl für Grau- als auch Farbbilder korrekt funktionieren.
'''
imgGray = REPLACE_THIS(imgOriginal)
cvt.showImage("Grayscale image", imgGray)


'''
Konvertieren Sie das originale Bild von seinem Stndarddatentyp (`uint8` pro Farbkanal) in `float` und zeigen Sie es an.
Voraussichtlich wird das Bild nahezu weiß sein. Versuchen Sie herauszufinden woran das liegt und passen Sie das Bild entsprechend an.
'''
img = REPLACE_THIS(imgOriginal)
print("Floating point image:")
cvt.showImage("Floating point image", img)


# TODO Aufgabe 2
'''
Zeichnen Sie ein rotes Rechteck (110 x 220 Pixel) genau in die Mitte des Bildes.
Versuchen Sie dazu den Slicing Operator aus Python zu nutzen.
'''
#
# ???
#

cvt.showImage("Red box", img)


# TODO Aufgabe 3
'''
Hängen Sie eine Callback-Funktion `mouse_move(event)` an das Bild im Fenster "Red box", die bei jeder Mausbewegung aufgerufen wird. Sie soll die Bild(!)-Koordinaten des Mauszeigers (x, y) und evtl. gedrückte Tasten ausgeben.
Sie benötigen dazu u.U. die Referenz auf das Zeichenfeld des Fensters (`plt.figure(title)`) aus der Funktion `showImage(..)`.
'''
#
# ???
#

'''
Optional: Entfernen Sie die Callback-Funktion, sobald auf das Bild geklickt wird.
'''
#
# ???
#


# TODO Aufgabe 4
'''
Schreiben Sie eine Funktion `showImageList(...)`, die Bilder auch als Liste annimmt und diese horizontal nebeneinander anzeigt.
'''
img2 = cvt.safeLoad('images/hummingbird_from_pixabay2.png')
img3 = cvt.safeLoad('images/hummingbird_from_pixabay3.png')

# cvt.showImageList("Image list", (imgOriginal, img, img2, img3))


# TODO Aufgabe 5
'''
Erweitern Sie die Funktionen `showImage(...)` und `showImageList(...)` um einen weiteren Parameter `normalize` vom Typ Boolean. Wenn dieser auf `False` gesetzt ist, dann soll die Funktion wie bisher funktionieren, wenn dieser auf `True` gesetzt wird, dann soll jedes Eingabebild kopiert und der Kontrast der kopierten Bilder vor der Anzeige mittels Contrast Stretching verbessert werden, damit der gesamte Wertebereich ausgenutzt wird.
'''
img3[:,:,:] = img3[:,:,:] / 4 # darken the image to show contrast stretching

#
# ???
#
