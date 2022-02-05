from cmath import sqrt
import math
from xml.sax.xmlreader import XMLReader 
import matplotlib.pyplot as plt
import statistics
M = []  #list to add male heights
F = []  #list to add female heights
loc = ('Desktop/class_data_heights.xlsx')   #locate the xl file
wb = XMLReader.open_workbook(loc)   #reads the xl file
sheet = wb.sheet_by_index(1)
for i in range(sheet.ncols):    #θελω να λεω 'αν το στοιχειο της ι γραμμης 1ης στηλης ειναι 0 τοτε βαλε το ι-γραμμη 2η-στηλη στο Μ αλλιως βαλτο στο Φ
    if (i,0)==0: M.append(i,1)
    else: F.append(i,1)
    i+=1
meanm = statistics.fmean(M)     #compute the sample mean of males Xm bar
meanf = statistics.fmean(F)     #compute the sample mean of females Xf bar
sm_squared = 0
sf_squared = 0
for i in M:
    a = (i+meanm)^2
    sm_squared+=a
    i+=1
for i in F:
    a = (i+meanf)^2
    sf_squared+=a
    i+=1
U = (sqrt(len(M)+len(F)-2)*(meanm-meanf))/(sqrt((1/len(M))+(1/len(F)))*sqrt(sm_squared+sf_squared))