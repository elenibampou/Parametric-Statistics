from xml.sax.xmlreader import XMLReader 
from fractions import Fraction as fr
import matplotlib.pyplot as plt
import statistics
from statistics import variance

from numpy import maximum
loc = ('Desktop/class_data_heights.xlsx')   #locate the xl file
L = []  #list to add the heights
M = []  #list to add male heights
F = []  #list to add female heights
n = 82  #how many students mesured their height
wb = XMLReader.open_workbook(loc)   #reads the xl file
sheet = wb.sheet_by_index(1)
for i in range(sheet.nrows):    #adds the heights to the list
    L.append(i,1)
    i+=1
print(statistics.fmean(L))  #compute and print the mean value
print(variance(L))  #compute and print the sample variance

for i in range(sheet.ncols):    #θελω να λεω 'αν το στοιχειο της ι γραμμης 1ης στηλης ειναι 0 τοτε βαλε το ι-γραμμη 2η-στηλη στο Μ αλλιως βαλτο στο Φ
    if (i,0)==0: M.append(i,1)
    else: F.append(i,1)
    i+=1
x = [range(len(M)+1)]
ym = [range(len(L)+1)]
yf = [range(len(F)+1)]
plt.plot(ym,yf)
plt.show()