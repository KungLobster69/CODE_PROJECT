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
    
    X = np.zeros((len(left_knee_DATA),8))
    Y = np.zeros((len(left_knee_DATA),8))
    Z = np.zeros((len(left_knee_DATA),8))
    
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
    
    #Find Pick Point X
    for i in range(np.size(X,1)):
        x_point = X[:,i]
        x_peak = []
        sample_x_peak = []
        row_x_peak = []
        for j in range(np.size(x_point,0)):
            if j > 0 and j < np.size(x_point,0)-1:
                After_sample_x_point = x_point[j-1]
                sample_x_point = x_point[j]
                Next_sample_x_point = x_point[j+1]
                
                # PEAK บน
                if After_sample_x_point < sample_x_point and sample_x_point > Next_sample_x_point:
                    sample_x_peak = np.append(sample_x_peak,sample_x_point)
                    row_x_peak = np.append(row_x_peak,j)
                    
                # PEAK ล่าง
                elif After_sample_x_point > sample_x_point and sample_x_point < Next_sample_x_point:
                    sample_x_peak = np.append(sample_x_peak,sample_x_point)
                    row_x_peak = np.append(row_x_peak,j)
                    
        x_peak = np.array([sample_x_peak,row_x_peak]).T
        
    #Find Pick Point Y
    for i in range(np.size(Y,1)):
        y_point = Y[:,i]
        y_peak = []
        sample_y_peak = []
        row_y_peak = []
        for j in range(np.size(y_point,0)):
            if j > 0 and j < np.size(y_point,0)-1:
                After_sample_y_point = y_point[j-1]
                sample_y_point = y_point[j]
                Next_sample_y_point = y_point[j+1]
                
                # PEAK บน
                if After_sample_y_point < sample_y_point and sample_y_point > Next_sample_y_point:
                    sample_y_peak = np.append(sample_y_peak,sample_y_point)
                    row_y_peak = np.append(row_y_peak,j)
                    
                # PEAK ล่าง
                if After_sample_y_point > sample_y_point and sample_y_point < Next_sample_y_point:
                    sample_y_peak = np.append(sample_y_peak,sample_y_point)
                    row_y_peak = np.append(row_y_peak,j)
                    
        y_peak = np.array([sample_y_peak,row_y_peak]).T

    #Find Pick Point Z
    for i in range(np.size(Z,1)):
        z_point = X[:,i]
        z_peak = []
        sample_z_peak = []
        row_z_peak = []
        for j in range(np.size(z_point,0)):
            if j > 0 and j < np.size(z_point,0)-1:
                After_sample_z_point = z_point[j-1]
                sample_z_point = z_point[j]
                Next_sample_z_point = z_point[j+1]
                
                # PEAK บน
                if After_sample_z_point < sample_z_point and sample_z_point > Next_sample_z_point:
                    sample_z_peak = np.append(sample_z_peak,sample_z_point)
                    row_z_peak = np.append(row_z_peak,j)
                    
                # PEAK ล่าง
                if After_sample_z_point > sample_z_point and sample_z_point < Next_sample_z_point:
                    sample_z_peak = np.append(sample_z_peak,sample_z_point)
                    row_z_peak = np.append(row_z_peak,j)
                    
        z_peak = np.array([sample_z_peak,row_z_peak]).T