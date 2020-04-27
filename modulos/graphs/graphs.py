import matplotlib.pyplot as plt
import numpy as np


def plot_violin(data):
    np.random.seed(10)
    collectn_1 = np.random.normal(100, 10, 200)
    collectn_2 = np.random.normal(80, 30, 200)

    ## combine these different collections into a list
    data_to_plot = [collectn_1, collectn_2]

    # Create a figure instance
    fig = plt.figure()

    # Create an axes instance
    ax = fig.add_axes([0, 0, 1, 1])

    # Create the boxplot
    bp = ax.violinplot(data_to_plot, label="Legenda")
    ax.boxplot(data_to_plot)
    ax.legend()
    plt.show()
    # plt.savefig("nome", format="pdf")

array = ["36", "32", "31"]

plot_violin(array)
