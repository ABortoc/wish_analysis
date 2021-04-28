import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# https://stackoverflow.com/a/48372659 by Trenton McKinney


def graph_create(data):
    # Bring some raw data.
    data_sorted = {i: k for i, k in sorted(
        data.items(), key=lambda item: item[1])}
    frequencies = data_sorted.values()
    freq_series = pd.Series(frequencies)

    x_labels = data_sorted.keys()

    # Plot the figure.
    plt.figure(figsize=(12, 8))
    ax = freq_series.plot(kind='bar')
    ax.set_title('Pity Frequency Breakdown')
    ax.set_xlabel('Pity Number')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(x_labels, rotation=45)

    # Call the function above. All the magic happens there.
    add_value_labels(ax)

    plt.show()


def add_value_labels(ax, spacing=5):
    """Add labels to the end of each bar in a bar chart.

    Arguments:
        ax (matplotlib.axes.Axes): The matplotlib object containing the axes
            of the plot to annotate.
        spacing (int): The distance between the labels and the bars.
    """

    # For each bar: Place a label
    for rect in ax.patches:
        # Get X and Y placement of label from rect.
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2

        # Number of points between bar and label. Change to your liking.
        space = spacing
        # Vertical alignment for positive values
        va = 'bottom'

        # If value of bar is negative: Place label below bar
        if y_value < 0:
            # Invert space to place label below
            space *= -1
            # Vertically align label at top
            va = 'top'

        # Use Y value as label and format number with one decimal place
        label = "{:.1f}".format(y_value)

        # Create annotation
        ax.annotate(
            label,                      # Use `label` as label
            (x_value, y_value),         # Place label at end of the bar
            xytext=(0, space),          # Vertically shift label by `space`
            textcoords="offset points",  # Interpret `xytext` as offset in points
            ha='center',                # Horizontally center label
            va=va)                      # Vertically align label differently for
        # positive and negative values.
