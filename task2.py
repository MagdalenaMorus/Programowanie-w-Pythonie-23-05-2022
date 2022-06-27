import numpy as np
import matplotlib.pyplot as plt


NUM_OF_CHARGES = 2
K = 8.9875e9


def charge():
    position = np.random.uniform(0, 10, size=3)
    value = np.random.normal()
    return position, value


def matrix(num_of_charges):
    arr = []
    for i in range(num_of_charges):
        pos, val = charge()
        row = np.append(pos, val)
        arr.append(row)
    return arr


def plot(data):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    for row in data:
        if row[3] > 0:
            ax.scatter(row[0], row[1], row[2], color='red')
        if row[3] <= 0:
            ax.scatter(row[0], row[1], row[2], color='blue')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()


def potential(a, b, h, data):
    """
    calculating potential in one point(a,b,h) from all charges
    :param a: x coordinate of the point
    :param b: y coordinate of the point
    :param h: z coordinate of the point
    :param data: matrix of charges
    :return: potential in this one point
    """
    potentials = []
    for row in data:
        delta_x = row[0] - a
        delta_y = row[1] - b
        delta_z = row[2] - h
        q = row[3]
        sumsum = delta_x ** 2 + delta_y ** 2 + delta_z ** 2
        V = (K * q) / np.sqrt(sumsum)
        potentials.append(V)
    return sum(potentials)


def isoline(h, data):
    grid_resolution = 500
    xlist = np.linspace(0, 10, grid_resolution)
    ylist = np.linspace(0, 10, grid_resolution)
    array = np.zeros((grid_resolution, grid_resolution))
    for a_ind, a in enumerate(xlist):
        for b_ind, b in enumerate(ylist):
            array[a_ind, b_ind] = potential(a, b, h, data)
    X, Y = np.meshgrid(xlist, ylist)
    fig, ax = plt.subplots(1, 1)
    cp = ax.contourf(X, Y, array, levels=20)
    fig.colorbar(cp)
    ax.set_title('Electric Potential')
    plt.show()


data = matrix(NUM_OF_CHARGES)
isoline(5, data)
plot(data)



