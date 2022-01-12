import cv2 as cv
import numpy as np
import mahotas as mh

# abrir una imagen
img = cv.imread("./img/prueba2.png")
cv.imshow('Original', img)

# Pre-procesamiento
# conversion a escala de grises
img_gris = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gris', img_gris)

# eliminar ruido
img_median_filtered = cv.medianBlur(img_gris, 5)
cv.imshow('Median Filtered', img_median_filtered)

# deteccion de bordes
img_sobel_X = cv.Sobel(img_median_filtered, cv.CV_64F, 1, 0)
img_sobel_Y = cv.Sobel(img_median_filtered, cv.CV_64F, 0, 1)

img_sobel__filteredX = np.uint8(np.absolute(img_sobel_X))
img_sobel__filteredY = np.uint8(np.absolute(img_sobel_Y))

img_sobel__filtered = cv.bitwise_or(img_sobel__filteredX, img_sobel__filteredY)
cv.imshow('Sobel Filtered', img_sobel__filtered)

ret, img_threshold = cv.threshold(img_sobel__filtered, 0, 250, cv.THRESH_OTSU)
cv.imshow('Thresholding', img_threshold)

# condicion de cerrar
cv.waitKey(0)

# eliminar las ventanas
cv.destroyAllWindows()