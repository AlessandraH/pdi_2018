import imageio
import cv2

kargs = {'duration': 0.5}

picture1 = 'pictures/kirby1.jpg'
picture1_frame = 'kirby1'
picture2 = 'pictures/kirby2.jpg'
picture2_frame = 'kirby2'

img1 = cv2.imread(picture1, 1)
img2 = cv2.imread(picture2, 1)

n = img1.shape[0]
divisores = [i for i in range(2, n // 2 + 1) if n % i == 0]
divisores.append(n)
div_inv = [i for i in range(n // 2 + 1, 2, -1) if n % i == 0]
div_inv.insert(0, n)

gif = []
for i in divisores:
    gif.append(imageio.imread('pictures/amostr/kirby1_' + str(i) + '.jpg'))

for i in div_inv:
    gif.append(imageio.imread('pictures/amostr/kirby2_' + str(i) + '.jpg'))

for i in divisores:
    gif.append(imageio.imread('pictures/amostr/kirby2_' + str(i) + '.jpg'))

for i in div_inv:
    gif.append(imageio.imread('pictures/amostr/kirby1_' + str(i) + '.jpg'))

imageio.mimsave('pictures/gif/gif.gif', gif, **kargs)
