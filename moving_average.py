import numpy as np
import matplotlib.pyplot as plt


def moving_average_real (numbers_array, window_length):
    #moving Average of a sampele of a sample of uniform numbers
    #dataA_average = np.average(dataA)
    window_averages = []
    spikes = []
    item_number = len(numbers_array)
    for i in range(item_number): #this loop is to define windows
        if i + window_length < item_number:
            window = numbers_array[i: i + window_length]
        else:
            window = numbers_array[i:]
        window_avr = np.average(window)
        window_averages.append(window_avr)
        window_spike = []
        for sample_idx in range(len(window)): #this loop gives the local spikes acording to
            if window[sample_idx] > window_avr:
                window_spike.append((window[sample_idx], f"index in window = {sample_idx}", f"index = {i + sample_idx}"))
        spikes.append(window_spike)
    return window_averages, spikes


def moving_average (starting_point, ending_point, item_number, window_length):
    #moving Average of a sampele of a sample of uniform numbers
    dataA = np.random.randint(starting_point, ending_point, (item_number,))
    #dataA_average = np.average(dataA)
    window_averages = []
    spikes = []
    for i in range(item_number): #this loop is to define windows
        if i + window_length < item_number:
            window = dataA[i: i + window_length]
        else:
            window = dataA[i:]
        window_avr = np.average(window)
        window_averages.append(window_avr)
        window_spike = []
        for sample_idx in range(len(window)): #this loop gives the local spikes acording to
            if window[sample_idx] > window_avr:
                window_spike.append((window[sample_idx], f"index in window = {sample_idx}", f"index = {i + sample_idx}"))
        spikes.append(window_spike)
    return dataA, window_averages, spikes


def plots(item_number, dataA, window_averages):
    plt.bar(range(item_number), dataA, label="Data: A")
    plt.legend(loc="lower right")
    plt.plot(range(item_number), window_averages, color="red", label="Local Median")
    plt.show()


starting_point = 1
ending_point = 100
item_number = 2000
window_length = 100

dataA, window_averages, spikes = moving_average(starting_point, ending_point, item_number, window_length)
print(window_averages)
print(spikes)
plots(item_number, dataA, window_averages)
