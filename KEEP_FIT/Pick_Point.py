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
        