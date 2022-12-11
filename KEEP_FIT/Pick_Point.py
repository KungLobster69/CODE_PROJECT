import numpy as np
import mediapipe as mp
import pickle
import matplotlib.pyplot as plt

Data_description = pickle.load(open('D:\KUNG_LOBSTER69\Quest\Data_description', 'rb'))
Time_series = pickle.load(open('D:\KUNG_LOBSTER69\Quest\Time_series', 'rb'))

# for Human in Data_description:
#     frame_sec = Human[1]
#     frame_all = Human[2]
#     time_all_sec = frame_all/frame_sec
#     time_all_minutes = (frame_all/frame_sec)/60
for Point in Time_series:
    left_knee_DATA = Point[0]
    right_knee_DATA = Point[1]
    left_ankle_DATA = Point[2]
    right_ankle_DATA = Point[3]
    left_foot_DATA = Point[4]
    right_foot_DATA = Point[5]
    left_hell_DATA = Point[6]
    right_hell_DATA = Point[7]

    
m = left_knee_DATA.shape
X = np.zeros((len(left_knee_DATA),8))
Y = np.zeros((len(left_knee_DATA),8))
Z = np.zeros((len(left_knee_DATA),8))

for i in range(len(left_knee_DATA)):
    X[i,] = left_knee_DATA[i,0],right_knee_DATA[i,0],left_ankle_DATA[i,0],right_ankle_DATA[i,0],left_foot_DATA[i,0],right_foot_DATA[i,0],left_hell_DATA[i,0],right_hell_DATA[i,0]
    
    Y[i,] = left_knee_DATA[i,1],right_knee_DATA[i,1],left_ankle_DATA[i,1],right_ankle_DATA[i,1],left_foot_DATA[i,1],right_foot_DATA[i,1],left_hell_DATA[i,1],right_hell_DATA[i,1]
    
    Z[i,] = left_knee_DATA[i,2],right_knee_DATA[i,2],left_ankle_DATA[i,2],right_ankle_DATA[i,2],left_foot_DATA[i,2],right_foot_DATA[i,2],left_hell_DATA[i,2],right_hell_DATA[i,2]
