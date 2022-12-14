import numpy as np
import mediapipe as mp
import pickle
import matplotlib.pyplot as plt
import statistics

def find_peaks(signal):

  peaks = []
  peaks_row = []
  for i in range(1, len(signal) - 1):
    if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
      peaks = np.append(peaks,signal[i])
      peaks_row = np.append(peaks_row, i)
    elif signal[i] < signal[i-1] and signal[i] < signal[i+1]:
      peaks = np.append(peaks,signal[i])
      peaks_row = np.append(peaks_row, i)

  return peaks,peaks_row

def save_data(data):
    with open("DATA_axis", "wb") as f:
        pickle.dump(data, f)

Data_description = pickle.load(open('E:\PROJECT\KEEP_FIT\Quest\Data_description', 'rb'))
Time_series = pickle.load(open('E:\PROJECT\KEEP_FIT\Quest\Time_series', 'rb'))

x_peak_human = []
y_peak_human = []
z_peak_human = []

for Human in range(np.size(Time_series,0)):
    Human_DATA = Time_series[Human]
    x_peak_values = []
    y_peak_values = []
    z_peak_values = []
    for Point in range(np.size(Human_DATA,0)):
        Point_DATA = Human_DATA[Point]
        X = Point_DATA[:,0]
        Y = Point_DATA[:,1]
        Z = Point_DATA[:,2]
        
        x_peak_values.append((find_peaks(X)))
        y_peak_values.append((find_peaks(Y)))
        z_peak_values.append((find_peaks(Z)))
        
    x_peak_human.append((x_peak_values))
    y_peak_human.append((y_peak_values))
    z_peak_human.append((z_peak_values))
    
    # save_data([x_peak_human,y_peak_human,z_peak_human])
