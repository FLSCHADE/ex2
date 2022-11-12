import cv2 as cv
import sys
import numpy as np
import matplotlib.pyplot as plt


def safeLoad(pathToFile):
    '''
    OpenCV does no validation checks due to performance reasons.
    Therefore, this function checks if the image could be loaded
    '''
    img = cv.imread(pathToFile)
    if img is None:
        sys.exit("Image could not be loaded.")
    return img


# TODO Aufgabe 1
'''
Passen Sie die Funktion `imageStats(..)` so an, dass sie sowohl Grau- als auch Farbbilder korrekt anzeigt.
Erweitern Sie die Funktion zusätzlich so dass der Datentyp mit ausgegeben wird.
'''
def imageStats(img):
    '''
    Returns a few image statistics
    '''
    s = img.shape
    return f'Width: {s[1]}, Height: {s[0]}, Channels: {s[2]}'



# TODO Aufgabe 1
'''
Passen Sie die Funktion `showImage(..)` so an, dass sie sowohl Grau- als auch Farbbilder korrekt anzeigt.
'''
def showImage(title, originalImg):
    print(imageStats(originalImg))

    img = originalImg.copy()
    img = img[:,:,::-1]
    plt.figure(title)
    plt.imshow(img)
    plt.show()


