import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


dim = 3
num_of_charges = 5

def charge():
    position = np.random.uniform(0, 10, size=3)
    value = np.random.normal()
    return position, value


if __name__=='__main__':
    for i in range(num_of_charges):
        pos, val = charge()
        arr=np.array(pos)
    print(arr)
    #
    # fig = plt.figure()
    # ax = fig.add_subplot(projection='3d')
    # ax.scatter(pos[0], pos[1], pos[2])
    #
    # ax.set_xlabel('X Label')
    # ax.set_ylabel('Y Label')
    # ax.set_zlabel('Z Label')
    #
    # plt.show()
    #
