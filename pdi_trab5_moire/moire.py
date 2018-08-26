import cv2
import numpy as np
from matplotlib import pyplot as plt

# ler imagem em tons de cinza
img = cv2.imread('pictures/up.jpg', 0)

# aplicando transformada Fourier na imagem
# e shiftando o resultado para formar a estrela
img = np.fft.fftshift(np.fft.fft2(img))

# mostrando o resultado da transformada Fourier
plt.imshow(20 * np.log(np.abs(img)), cmap='gray')
plt.show()

# alterando 3 pontos da transformada Fourier
img[60, 70] = img.max()
img[580, 70] = img.max()
img[250, 700] = img.max()

# mostrando 'nova' transformada Fourier
plt.imshow(20 * np.log(np.abs(img)), cmap='gray')
plt.show()

# mostrando imagem resultante (moire)
plt.imshow(abs(np.fft.ifft2(img)), cmap='gray')
plt.show()
