import cv2


def find_midst(a):
    return [[i, j] for i in range(img.shape[0]) for j in range(img.shape[1]) if
            img[i, j] > a and (img[i - 1, j] == a or img[i + 1, j] == a or img[i, j - 1] == a or img[i, j + 1] == a)]


# picture = 'pictures/circle.jpg'
# picture_frame = 'circle'
picture = 'pictures/rectangle.png'
picture_frame = 'rectangle'

img = cv2.imread(picture, 0)
(thresh, img) = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

margin = [[i, j] for i in range(img.shape[0]) for j in range(img.shape[1]) if
          img[i, j] != 0 and (img[i - 1, j] == 0 or img[i + 1, j] == 0 or img[i, j - 1] == 0 or img[i, j + 1] == 0)]

while margin:
    img[margin[0][0], margin[0][1]] = 3
    margin.remove([margin[0][0], margin[0][1]])

n = 3
midst = find_midst(n)
while midst:
    n += 3
    while midst:
        img[midst[0][0], midst[0][1]] = n
        midst.remove([midst[0][0], midst[0][1]])
    midst = find_midst(n)

# cv2.imwrite('pictures/circletd.jpg', img)
cv2.imwrite('pictures/rectangletd.jpg', img)
cv2.imshow(picture_frame, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
