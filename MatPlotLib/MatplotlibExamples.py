import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Basic graphs
def PlotLineGraph():
    x = [0, 1, 2, 3]
    y = [0, 2, 4, 6]
    #   plt.plot(x, y, color='red', label='2x', marker='.', markersize=12, markeredgecolor='blue')

    # Use shorthand notation
    # fmt = '[color][marker][line]'
    plt.plot(x, y, 'b.--', label='2x')
    plt.figure(figsize=(5, 3), dpi=300)
    plt.title('Plot Line Graph', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.xticks([0, 1, 2, 3])
    plt.yticks([0, 1, 2, 3])
    plt.legend('2X')
    plt.show()


# PlotLineGraph()

# MatPltLib With Numpy
def MatPlotLibWithNumpy():
    x2 = np.arange(0, 4.5, 0.5)
    plt.plot(x2, x2**2, label='X^2')
    plt.legend('X2')
    plt.show()


#   MatPlotLibWithNumpy()

def BarCharts():
    labels = ['A', 'B', 'C']
    values = [1, 4, 2]

    bars = plt.bar(labels, values)
    bars[0].set_hatch('/')
    bars[1].set_hatch('*')
    bars[2].set_hatch('o')
    plt.show()


#   BarCharts()
