from cmath import sqrt
import random
from xml.sax.xmlreader import XMLReader 
import matplotlib.pyplot as plt
import statistics
M = []  #list to add male heights
L = []  #list to count how many ints include the actual mean 
n=5
summean=0
sums = 0
loc = ('Desktop/class_data_heights.xlsx')   #locate the xl file
wb = XMLReader.open_workbook(loc)   #reads the xl file
sheet = wb.sheet_by_index(1)
for i in range(sheet.ncols):    #θελω να λεω 'αν το στοιχειο της ι γραμμης 1ης στηλης ειναι 0 τοτε βαλε το ι-γραμμη 2η-στηλη στο Μ
    if (i,0)==0: M.append(i,1)
    i+=1
Ml = statistics.fmean(M)    #compute the mean value
print(Ml)  #print the mean value

for j in range(100):    #need to pick 5 males and blah blah blah 100 times
    r5 = random.sample(list, n)     #pick 5 rondom males
    for i in r5:
      sum+=i
      i+=1
    meann = sum/n   #compute the sample mean Xn bar
    for i in M:     #compute the Σ for the s of the conf. int. formula
        a=(i - meann)^2
        sums+=a
        i+=1
    s = sqrt(sums/(n-1))    #compute s for the confidence interval formula
    A = (meann-s)/sqrt(n)   #confidence interval = [A,B]
    B = (meann+s)/sqrt(n)
    plt.plot(A,B)
    plt.show()
    if meann>=A and meann<=B:
        L.append(1)
    print(len(L))
    j+=1

#in the A,B formula i also need the T^-1(0.95) that is on the table i dont have and dont know how to insert

