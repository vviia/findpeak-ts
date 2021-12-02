#import library
from math import dist
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import neurokit2 as nk
from scipy.signal import find_peaks
# import data1_05
# from data1_05 import ppg
import data1_10
from data1_10 import ppg

#mendefinisi x dan y array
# x= np.linspace(0,7244,7245) #data1_05
x= np.linspace(0,3487,3488) #data1_10
y= ppg
#menemukan puncak
peaks = find_peaks(y, height=525, threshold=0, distance=10)
height = peaks[1]['peak_heights']
peak_post= x[peaks[0]]

print("posisi titik puncak :", peak_post)


#menemukan nilai minimum
y2=y*-1
minima=find_peaks(y2)
min_pos=x[minima[0]]
min_height=y2[minima[0]]

#print titik puncak
peak_coordinate=peak_post
    #print(peak_coordinate)
#banyaknya puncak
    # print(len(peak_coordinate)) 
    #output 40
#data titik ke2 sampai 40
data1=peak_coordinate[1:]
#data titik ke1-39
data2=peak_coordinate[:-1]
#jarak antar puncak (pengurangan array)
distance= data1-data2
print("jarak antar puncak :", distance)   #selisih

#mencari rata-rata jarak
total = np.sum(distance)
totaldistance = total
average= totaldistance/len(distance)
#mencari RR
# delay =200 #delay 05
delay = 100 #delay 10
RR = average/delay
#mencari HR
HR = 60/RR

#print(min(peak_post))
print("jarak terdekat :", min(distance))
print("jarak terjauh :", max(distance))
print("rata-rata jarak :", average)
print("banyaknya peak :", len(distance))
print("jumlah jarak:", total)
print("HR", HR)

#plotting
fig = plt.figure()
ax= fig.subplots()
ax.plot(x,y)
ax.scatter(peak_post, height, color='r', s=15, marker='D', label='puncak PPG')
ax.scatter(min_pos, min_height*-1, color='gold', s=15, marker='X', label='minimal')
ax.legend()
ax.grid()
plt.show()