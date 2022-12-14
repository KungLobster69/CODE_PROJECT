import numpy as np
import mediapipe as mp
import pickle
import matplotlib.pyplot as plt
import statistics

Data_description = pickle.load(open('E:\PROJECT\KEEP_FIT\Quest\Data_description', 'rb'))
Time_series = pickle.load(open('E:\PROJECT\KEEP_FIT\Quest\Time_series', 'rb'))

for Human in range(np.size(Time_series,0)):
    Human_DATA = Time_series[Human]
    for Point in range(np.size(Human_DATA,0)):
        Point_DATA = Human_DATA[Point]
        X = Point_DATA[:,0]
        Y = Point_DATA[:,1]
        Z = Point_DATA[:,2]
        
        #Find Pick Point X
        x_peak_sample_upper = []
        x_peak_sample_lower = []
        x_peak_sample = []
        x_peak_row = []
        for sample in range(np.size(X,0)):
            if sample > 0 and sample < np.size(X,0) - 1:
                Old_sample = X[sample - 1]
                Current_sample = X[sample]
                New_sample = X[sample + 1]
                
                # PEAK บน
                if Old_sample < Current_sample and Current_sample > New_sample:
                    x_peak_sample_upper = np.append(x_peak_sample_upper,Current_sample)
                    x_peak_sample = np.append(x_peak_sample,Current_sample)
                    x_peak_row = np.append(x_peak_row,sample)
                    
                # PEAK ล่าง
                if Old_sample > Current_sample and Current_sample < New_sample:
                    x_peak_sample_lower = np.append(x_peak_sample_lower,Current_sample)
                    x_peak_sample = np.append(x_peak_sample,Current_sample)
                    x_peak_row = np.append(x_peak_row,sample)
        
        mean_x_peak_upper = statistics.mean(x_peak_sample_upper)
        mean_x_peak_lower = statistics.mean(x_peak_sample_lower)
        mean_x_peak = statistics.mean(x_peak_sample)
        
        for sample in range(np.size(x_peak_sample,0)):
            if x_peak_sample[sample] > mean_x_peak and x_peak_sample[sample] < mean_x_peak_upper:
                x_peak_sample[sample] = mean_x_peak
                x_peak_row[sample] = 0
            if x_peak_sample[sample] < mean_x_peak and x_peak_sample[sample] > mean_x_peak_lower:
                x_peak_sample[sample] = mean_x_peak
                x_peak_row[sample] = 0
        # x_peak = np.array([x_peak_sample,x_peak_row]).T
        
        # #Find Pick Point y
        # y_peak_sample = []
        # y_peak_row = []
        # for sample in range(np.size(Y,0)):
        #     if sample > 0 and sample < np.size(Y,0) - 1:
        #         Old_sample = Y[sample - 1]
        #         Current_sample = Y[sample]
        #         New_sample = Y[sample + 1]
                
        #         # PEAK บน
        #         if Old_sample < Current_sample and Current_sample > New_sample:
        #             y_peak_sample = np.append(y_peak_sample,Current_sample)
        #             y_peak_row = np.append(y_peak_row,sample)
                    
        #         # PEAK ล่าง
        #         if Old_sample > Current_sample and Current_sample < New_sample:
        #             y_peak_sample = np.append(y_peak_sample,Current_sample)
        #             y_peak_row = np.append(y_peak_row,sample)
                    
        # y_peak = np.array([y_peak_sample,y_peak_row]).T
        
        # #Find Pick Point z
        # z_peak_sample = []
        # z_peak_row = []
        # for sample in range(np.size(Z,0)):
        #     if sample > 0 and sample < np.size(Z,0) - 1:
        #         Old_sample = Z[sample - 1]
        #         Current_sample = Z[sample]
        #         New_sample = Z[sample + 1]
                
        #         # PEAK บน
        #         if Old_sample < Current_sample and Current_sample > New_sample:
        #             z_peak_sample = np.append(z_peak_sample,Current_sample)
        #             z_peak_row = np.append(z_peak_row,sample)
                    
        #         # PEAK ล่าง
        #         if Old_sample > Current_sample and Current_sample < New_sample:
        #             z_peak_sample = np.append(z_peak_sample,Current_sample)
        #             z_peak_row = np.append(z_peak_row,sample)
                    
        # z_peak = np.array([z_peak_sample,z_peak_row]).T
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        