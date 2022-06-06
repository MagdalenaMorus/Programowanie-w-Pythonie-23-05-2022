import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


dim = 3
num_of_charges = 10
k = 8.9875e10

def charge():
    position = np.random.uniform(0, 10, size=3)
    value = np.random.normal()
    return position, value


def matrix():
    arr = []
    for i in range(num_of_charges):
        pos, val = charge()
        row = np.append(pos, val)
        arr.append(row)
    # print(arr)
    return arr


# def plot(data):
#     fig = plt.figure()
#     ax = fig.add_subplot(projection='3d')
#     for row in data:
#         if row[3] > 0:
#             ax.scatter(row[0], row[1], row[2], color='red')
#         if row[3] <= 0:
#             ax.scatter(row[0], row[1], row[2], color='blue')
#
#     ax.set_xlabel('X Label')
#     ax.set_ylabel('Y Label')
#     ax.set_zlabel('Z Label')
#
#     plt.show()
#     print(row)


def potential(a, b, h, data):
    for row in data:
        x1 = row[0] - a
        y1 = row[1] - b
        z1 = row[2] - h
        q1 = row[3]
        V1 = (k * q1) / np.sqrt(x1 ** 2, y1 ** 2, z1 ** 2)
    return V1

def potential_position():
    xlist = np.linspace(0, 10, 100)
    ylist = np.linspace(0, 10, 100)
    for i in range(xlist):
        for j in range(ylist):
            a = xlist[i]
            b = ylist[j]
    return a, b

#nie działa na razie to na dole
# def isoline(data):
#     xlist = np.linspace(0, 10, 100)
#     ylist = np.linspace(0, 10, 100)
#     X, Y = np.meshgrid(xlist, ylist)
    # Z = kq/r
    # Z = []
    # for row in data:
    #     q = row[3]
    #     r = np.sqrt(row[0] ** 2 + row[1] ** 2)
    #     V = (k*q)/r
    #     Z.append(V)
    # fig, ax = plt.subplots(1, 1)
    # cp = ax.contourf(X, Y, Z)
    # fig.colorbar(cp)
    # ax.set_title('Electric Potential')
    # print(Z)
    # print(X)
    # print(Y)
    # plt.show()


# plot(matrix())
