#!/usr/bin/env python
# coding: utf-8

# In[ ]:


points = open("C:\\Users\\MTI\\Desktop\\project\\points.txt")
print(points.read())


def remove_missing_values(points):
    with open("C:\\Users\\MTI\\Desktop\\project\\points.txt") as f,open("points.txt","w") as f_out:
        for line in f:
            if not any(value == "" for value in line.strip().split(',')):
                f_out.write(line)
remove_missing_values("points.txt")


# In[ ]:


POINT = tuple[float, float, float]
def distance(p1: POINT, p2: POINT) -> float:
    return (abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2]))


# In[ ]:


from random import randint, choices
k = int(input("K = "))
centers = [(randint(-10, 10), randint(-10, 10), randint(-10, 10)) for _ in range(k)]
print(centers)


# In[ ]:


def k_means(points: list[POINT], centers: list[POINT]):
    result = [
        {
            "center": center,
            "points": [],
        }
        for center in centers
    ]
    for point in points:
        index, minimum = 0, distance(point, centers[0])

        i = 1
        
        while i < len(centers):
            d = distance(point, centers[i])
            if d < minimum:
                index, minimum = i, d

            i += 1

        result[index]["points"].append(point)

    return result
print(k_means(points,centers))


# In[ ]:


import pprint
while True:
    clusters = k_means(points, centers)
    new_centers = []
    for cluster in clusters:
        x, y, z = zip(*cluster["points"])
        new_centers.append(
            (
                sum(x) / len(x),
                sum(y) / len(y),
                sum(z) / len(z),
            )
        )

    if new_centers == centers:
        break

    centers = new_centers


pprint.pprint(clusters)

