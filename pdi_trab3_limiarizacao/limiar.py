import matplotlib.pyplot as plt
import numpy as np

picture = 'pictures/up.jpg'
threshould = 20

def bfs_area(image, i_start, j_start, visited):
    queue = [(i_start, j_start)]
    local_visited = set()
    tam = 0

    while queue:
        node = queue.pop()
        if node not in visited:
            visited.add(node)
            local_visited.add(node)
            tam += 1
            [i, j] = node
            neighbours = ((k, l) for k, l in [\
                            (i + 1, j),
                            (i - 1, j),
                            (i, j + 1),
                            (i, j - 1)
                            ] if 0 < k < image.shape[0] and
                                 0 < l < image.shape[1] and
                                 image[k, l] and (k, l) not in visited)

            for neighbour in neighbours:
                queue.append(neighbour)

    if tam <= threshould:
        for v in local_visited:
            image[v] = 0

img = plt.imread(picture)[:, :, 0]
img_in = list(map(lambda x: img >= x, range(256)))

for image in img_in:
    visited = set()
    for k, l in zip(*np.where(image)):
        if (k, l) not in visited:
            bfs_area(image, k, l, visited)

plt.imsave(fname="teste.png", arr=np.add.reduce(img_in), cmap="gray")
