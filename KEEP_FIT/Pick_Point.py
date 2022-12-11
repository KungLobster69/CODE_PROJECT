import numpy as np
import mediapipe as mp
import pickle
import matplotlib.pyplot as plt

Data_description = pickle.load(open('E:\PROJECT\KEEP_FIT\Quest\Data_description', 'rb'))
Time_series = pickle.load(open('E:\PROJECT\KEEP_FIT\Quest\Time_series', 'rb'))

for Human in Data_description:
    frame_sec = Human[1]
    frame_all = Human[2]
    time_all_sec = frame_all/frame_sec
    time_all_minutes = (frame_all/frame_sec)/60
    
for Point in Time_series:
    left_knee_DATA = Point[0]
    right_knee_DATA = Point[1]
    left_ankle_DATA = Point[2]
    right_ankle_DATA = Point[3]
    left_foot_DATA = Point[4]
    right_foot_DATA = Point[5]
    left_hell_DATA = Point[6]
    right_hell_DATA = Point[7]
    
    size = np.size(left_knee_DATA,0)
    
    X = np.zeros((size,8))
    Y = np.zeros((size,8))
    Z = np.zeros((size,8))
    
    X[:,0] = left_knee_DATA[:,0]
    X[:,1] = right_knee_DATA[:,0]
    X[:,2] = left_ankle_DATA[:,0]
    X[:,3] = right_ankle_DATA[:,0]
    X[:,4] = left_foot_DATA[:,0]
    X[:,5] = right_foot_DATA[:,0]
    X[:,6] = left_hell_DATA[:,0]
    X[:,7] = right_hell_DATA[:,0]
    
    Y[:,0] = left_knee_DATA[:,1]
    Y[:,1] = right_knee_DATA[:,1]
    Y[:,2] = left_ankle_DATA[:,1]
    Y[:,3] = right_ankle_DATA[:,1]
    Y[:,4] = left_foot_DATA[:,1]
    Y[:,5] = right_foot_DATA[:,1]
    Y[:,6] = left_hell_DATA[:,1]
    Y[:,7] = right_hell_DATA[:,1]
    
    Z[:,0] = left_knee_DATA[:,2]
    Z[:,1] = right_knee_DATA[:,2]
    Z[:,2] = left_ankle_DATA[:,2]
    Z[:,3] = right_ankle_DATA[:,2]
    Z[:,4] = left_foot_DATA[:,2]
    Z[:,5] = right_foot_DATA[:,2]
    Z[:,6] = left_hell_DATA[:,2]
    Z[:,7] = right_hell_DATA[:,2]
    
