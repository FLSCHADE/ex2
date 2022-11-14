#!/usr/bin/python3
# -*- coding: utf-8 -*-


import cv2 as cv
import openCVTools as cvt
import numpy as np
import matplotlib.pyplot as plt


# load image
imgOriginal = cvt.safeLoad('images/hummingbird_from_pixabay.png')
cvt.showImage("Original image", imgOriginal, False)


# TODO Aufgabe 1
'''
Konvertieren Sie das Bild in ein 1-Kanal Schwarzweiß(Grauton)-Bild.
Passen Sie die Funktionen `imageStats(..)` und `showImage(..)` so an, dass sie sowohl für Grau- als auch Farbbilder korrekt funktionieren.
'''
imgGray = cv.cvtColor(imgOriginal, cv.COLOR_BGR2GRAY)
cvt.showImage("Grayscale image", imgGray, False)


'''
Konvertieren Sie das originale Bild von seinem Stndarddatentyp (`uint8` pro Farbkanal) in `float` und zeigen Sie es an.
Voraussichtlich wird das Bild nahezu weiß sein. Versuchen Sie herauszufinden woran das liegt und passen Sie das Bild entsprechend an.
'''

# img = imgOriginal.astype(np.float64)  --> Produziert Fehler aufgrund des falschen Wertebereichs:
# "Clipping input data to the valid range for imshow with RGB data ([0..1] for floats or [0..255] for integers)."
img = imgOriginal.astype(np.float64)/255.0
print("Floating point image:")
cvt.showImage("Floating point image", img, False)


# TODO Aufgabe 2
'''
Zeichnen Sie ein rotes Rechteck (110 x 220 Pixel) genau in die Mitte des Bildes.
Versuchen Sie dazu den Slicing Operator aus Python zu nutzen.
'''
#
size = img.shape
mid_x = round(size[1]/2.0)
mid_y = round(size[0]/2.0)
#First Try
# for x in img[mid_x-55:mid_x+55]:
#     for y in x[mid_y-110:mid_y+110]:
#         y= np.array([1.0, 0.0, 0.0], 'float64')

#Second Try
# for x in range(mid_x-55,mid_x+55):
#     for y in range(mid_y-110, mid_y+110):
#         img[y][x] = np.array([0.0, 0.0, 1.0], 'float64')

#2nd 1st Try
for y in img[mid_y-110:mid_y+110]:
    for x in y[mid_x-55:mid_x+55]:
        x[0] = 0.0
        x[1] = 0.0
        x[2] = 1.0

cvt.showImage("Red box", img, False, add_callbacks = True)

# TODO Aufgabe 3
'''
Hängen Sie eine Callback-Funktion `mouse_move(event)` an das Bild im Fenster "Red box", die bei jeder Mausbewegung aufgerufen wird. Sie soll die Bild(!)-Koordinaten des Mauszeigers (x, y) und evtl. gedrückte Tasten ausgeben.
Sie benötigen dazu u.U. die Referenz auf das Zeichenfeld des Fensters (`plt.figure(title)`) aus der Funktion `showImage(..)`.
'''
#
# specific information: https://matplotlib.org/stable/users/explain/event_handling.html
# -->   realization through additional argument in the showImage() function and new defined callback functions in openCVTools.py
#

'''
Optional: Entfernen Sie die Callback-Funktion, sobald auf das Bild geklickt wird.
'''
#
# reaction on left mouse button click:
# -->   realization through recursive callback function "mouse_click(event, fig, disc_move, disc_key, disc_click)" in openCVTools.py
#       and the lambda event call on the figure's MouseEvent "button_press_event"
#


# TODO Aufgabe 4
'''
Schreiben Sie eine Funktion `showImageList(...)`, die Bilder auch als Liste annimmt und diese horizontal nebeneinander anzeigt.
'''
img2 = cvt.safeLoad('images/hummingbird_from_pixabay2.png')
img3 = cvt.safeLoad('images/hummingbird_from_pixabay3.png')

# cvt.showImageList("Image list1", (imgOriginal, img, img2, img3), False)
# cvt.showImageList("Image list2", (imgOriginal, img, img2, img3, img), False, arrangement_type = "column",add_callbacks = True)
cvt.showImageList("Image list3", (imgOriginal, img, img2, img3, imgOriginal), False, arrangement_type = "grid", axes_off = True, spacing = [0.1, 0.4], bg_color_RGB = [100,50,50])


# TODO Aufgabe 5
'''
Erweitern Sie die Funktionen `showImage(...)` und `showImageList(...)` um einen weiteren Parameter `normalize` vom Typ Boolean. Wenn dieser auf `False` gesetzt ist, dann soll die Funktion wie bisher funktionieren, wenn dieser auf `True` gesetzt wird, dann soll jedes Eingabebild kopiert und der Kontrast der kopierten Bilder vor der Anzeige mittels Contrast Stretching verbessert werden, damit der gesamte Wertebereich ausgenutzt wird.
'''
img3[:,:,:] = img3[:,:,:] / 4 # darken the image to show contrast stretching

#
cvt.showImage("contrast stretching", img3, True)
# cvt.showImage("contrast stretching", imgOriginal, True)
cvt.showImage("contrast stretching", imgOriginal, True, contrast_buffers = 5)
# cvt.showImage("contrast stretching", imgOriginal, True, contrast_buffers = 10)
# cvt.showImage("contrast stretching", imgOriginal, True, contrast_buffers = 20)
# cvt.showImage("contrast stretching", imgOriginal, True, contrast_buffers = 40)

cvt.showImageList("contrast stretched image list1", ((imgOriginal[:,:,:]/2).astype(np.uint8), (imgOriginal[:,:,:]/4).astype(np.uint8),(imgOriginal[:,:,:]/8).astype(np.uint8),(imgOriginal[:,:,:]/16).astype(np.uint8)), True, contrast_buffers=10)
#
z = 0