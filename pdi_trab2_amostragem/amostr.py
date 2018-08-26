import numpy as np
import cv2


def downsampling(img, step):
    img_aux = img[::step, ::step]
    img_aux = np.repeat(img_aux, step, axis=0)
    img_aux = np.repeat(img_aux, step, axis=1)
    return img_aux


picture1 = 'pictures/kirby1.jpg'
picture1_frame = 'kirby1'
picture2 = 'pictures/kirby2.jpg'
picture2_frame = 'kirby2'

img1 = cv2.imread(picture1, 1)
img2 = cv2.imread(picture2, 1)

n = img1.shape[0]
divisores = [i for i in range(2, n // 2 + 1) if n % i == 0]
divisores.append(n)

for i in divisores:
    img11 = downsampling(img1, i)
    cv2.imwrite('pictures/amostr/kirby1_' + str(i) + '.jpg', img11)
    img21 = downsampling(img2, i)
    cv2.imwrite('pictures/amostr/kirby2_' + str(i) + '.jpg', img21)

# cv2.imshow(picture1_frame, img1)
# # cv2.imshow('pixelado', img11)
# cv2.imshow(picture2_frame, img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
