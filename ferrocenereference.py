import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import preprocess as prep

def fcReference(inputFile, wait_for_plot):
    fileInput = inputFile
    File = prep.prep(fileInput)

    headers = ['potential','current']
    df = pd.read_csv(File, names = headers)

    x = df['potential']
    y = df['current']

    data = np.array(y)  
    """ While boxcar averaging is not really a good idea, this will not have an impact on
        the actual plotted data. This is simply for finding the maxima and minima."""
    window_size = 5
    smoothed_data = np.convolve(data, np.ones(window_size)/window_size, mode='valid')

    """ This is how we can find the maxima and minima of the smoothed data, which
        will look pretty good."""
    localMaxIndices = np.where((smoothed_data[1:-1] > smoothed_data[:-2]) & (smoothed_data[1:-1] > smoothed_data[2:]))[0] + 1
    localMinIndices = np.where((smoothed_data[1:-1] < smoothed_data[:-2]) & (smoothed_data[1:-1] < smoothed_data[2:]))[0] + 1

    """ There's too many points plotted here because of the noise, so we need to try to only
        plot enough points to get the real maxima and minima, without too much noise."""
    min_distance = 5
    filteredMaxIndices = [localMaxIndices[0]]
    filteredMinIndices = [localMinIndices[0]]

    for max_index in localMaxIndices[1:]:
        if max_index - filteredMaxIndices[-1] > min_distance:
            filteredMaxIndices.append(max_index)

    for min_index in localMinIndices[1:]:
        if min_index - filteredMinIndices[-1] > min_distance:
            filteredMinIndices.append(min_index)

    filteredMaxPotentials = x[filteredMaxIndices]
    filteredMinPotentials = x[filteredMinIndices]

    """Now, we can plot the data. yippee!"""
    plt.figure()
    plt.plot(x, y, label='Original Data')
    plt.gca().invert_xaxis()
    plt.scatter(filteredMaxPotentials, data[filteredMaxIndices], color='red', marker='o', label='Filtered Maxima')
    plt.scatter(filteredMinPotentials, data[filteredMinIndices], color='blue', marker='o', label='Filtered Minima')
    for i, potential in enumerate(filteredMaxPotentials):
        plt.annotate(f'{potential:.2f}', (potential, data[filteredMaxIndices[i]]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='red')

    for i, potential in enumerate(filteredMinPotentials):
        plt.annotate(f'{potential:.2f}', (potential, data[filteredMinIndices[i]]), textcoords="offset points", xytext=(0,-10), ha='center', fontsize=8, color='blue')
    plt.xlabel('Potential')
    plt.ylabel('Current')
    plt.title('Filtered Local Maxima and Minima')
    
    if wait_for_plot == True:
        plt.show()