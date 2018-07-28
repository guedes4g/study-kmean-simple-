import matplotlib
import matplotlib.pyplot as plt
import numpy as np

colors =  ['#e6194b', '#3cb44b', '#ffe119', '#0082c8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#d2f53c', '#fabebe', '#008080', '#e6beff', '#aa6e28', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000080', '#808080', '#000000']


def plot(km):
    for i in range(len(km.groups)):
        point = np.array(km.groups[i].points)
        ic = i % len(colors)
        if point.size > 0:
            plt.plot(point[:, 0], point[:, 1], marker='o', color=colors[ic], ls='')

    for i in range(len(km.groups)):
        ic = i % len(colors)
        plt.plot([km.groups[i].position[0]], [km.groups[i].position[1]],
                 marker='x', color=colors[ic], ls='')

    plt.show()
