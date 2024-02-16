# 1. Thresholding
import cv2
import matplotlib.pyplot as plt


image = cv2.imread('Image/abc.jpg', 0)
print(image)
# cv2.imshow("avcsc",image)
plt.imshow(image, cmap='gray')
plt.title('Thresholded Image')
plt.show()

# Simple Thresholding
ret, thresh_simple = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
# cv2.imshow('Simple Thresholding', thresh_simple)
plt.imshow(thresh_simple)
plt.title('Thresholded Image')
plt.show()
# Adaptive Thresholding
thresh_adaptive = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
# cv2.imshow('Adaptive Thresholding', thresh_adaptive)
plt.imshow(thresh_simple)
plt.title('Thresholded Image')
plt.show()
# Otsu's Thresholding
ret2, thresh_otsu = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# cv2.imshow('Otsu Thresholding', thresh_otsu)
plt.imshow(thresh_simple)
plt.title('Thresholded Image')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()