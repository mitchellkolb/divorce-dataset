
#Mitchell Kolb
#Project 315
#Divorce Dataset Analysis Code


import csv
import os
import pandas as pd
import numpy as np
from statistics import mean
from sklearn.cluster import AgglomerativeClustering
#from sklearn.datasets.samples_generator import make_blobs
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt





os.system('cls')
print("\n\n\nHello\n\n\n")


    #Doing initial run throughs of each row and column to get an idea of maxs, mins, averages
    #----------------------------------------------------------------------------------------

#setup
results = open("results.txt","w")
divorce = pd.read_csv('divorce.csv')
columnName = "Atr"
colNumber = 1
column = (columnName + str(colNumber))

#Figuring out what the "Class" atribute is
className = "Class"
results.write('The Last column Class has 1"s or 0"s, this is how many 1"s\n')
results.write('%s\n\n' %divorce[className].sum())
group1start = 1
group1end = (1 + divorce[className].sum())
group2start = (2 + divorce[className].sum()) #this hold the row value where the two types of peoples results changed
group2end = (divorce.shape[0])
results.write('Group 1 is rows: ')
results.write(str(group1start))
results.write(' - ')
results.write(str(group1end))
results.write('\nGroup 2 is rows: ')
results.write(str(group2start))
results.write(' - ')
results.write(str(group2end))

        #One line write version
        #results.write('\nGroup 2 is rows: {}'.format(group2start))

#Adding up the score of each question
results.write('\n\nThe total scores for each question by every user\n')
incrementLet = "Question "
incrementNum = 1
incrementEnd = ":  "
incrementLabel = (incrementLet + str(incrementNum) + incrementEnd)
for x in range(1,55): #1,55
    colNumber = x
    column = (columnName + str(colNumber))
    #print(divorce[column].sum())
    results.write(incrementLabel)
    results.write('%s\n' %divorce[column].sum())
    incrementNum+=1
    incrementLabel = (incrementLet + str(incrementNum) + incrementEnd)

#Showing the stats for entries
# print(divorce.describe(include='all'))
# print("\n")
# print(divorce.Atr1.describe())
# print("\n")
# print(divorce.Atr1.max())
# print("\n")
# print(divorce.loc[1:85, 'Atr1'].max())
test1 = []

#----------------------------------------------------------------------------------------
#Declare lists
maxList = []
minList = []
meanList = []
colNumber = 1
column = (columnName + str(colNumber))
results.write("\n\n-----------------Atr Scores------------------------")
results.write('\nThe max,min,mean of the questions in group 1\n')
#cycles through group 1 and finds max, min, mean for each Atr
for x in range(1,55):
    colNumber = x
    column = (columnName + str(colNumber))
    results.write('%s, ' %divorce.loc[group1start:group1end, column].max())
    maxList.append(divorce.loc[group1start:group1end, column].max())
    results.write('%s, ' %divorce.loc[group1start:group1end, column].min())
    minList.append(divorce.loc[group1start:group1end, column].min())
    results.write('%s, \n' %round((divorce.loc[group1start:group1end, column].mean()), 2))
    meanList.append(divorce.loc[group1start:group1end, column].mean())
    if x == 1 or x == 4:
        test1.append(round((divorce.loc[group1start:group1end, column].mean()), 2))
#Adds the averages to the result file
results.write("\nThe averages of the max,min,mean\n")
results.write('%s, ' %mean(maxList))
results.write('%s, ' %mean(minList))
results.write('%s, ' %round((mean(meanList)),2))

test3 = ((test1[0] + test1[1])/2)
#print(test3)

#clear lists for group 2 info
maxList.clear()
minList.clear()
meanList.clear()
results.write("\n\n\n")
results.write('\n\nThe max,min,mean of the questions in group 2\n')
colNumber = 1
column = (columnName + str(colNumber))
#cycles through group 2 and finds max, min, mean for each Atr
for x in range(1,55):
    colNumber = x
    column = (columnName + str(colNumber))
    results.write('%s, ' %divorce.loc[group2start:group2end, column].max())
    maxList.append(divorce.loc[group2start:group2end, column].max())
    results.write('%s, ' %divorce.loc[group2start:group2end, column].min())
    minList.append(divorce.loc[group2start:group2end, column].min())
    results.write('%s, \n' %round((divorce.loc[group2start:group2end, column].mean()), 2))
    meanList.append(divorce.loc[group2start:group2end, column].mean())
#Adds the averages to the result file
results.write("\nThe averages of the max,min,mean\n")
results.write('%s, ' %mean(maxList))
results.write('%s, ' %mean(minList))
results.write('%s, ' %round((mean(meanList)),2))


#----------------------------------------------------------------------------------------
#Doing the max,min,mean of all the questions for each user singly
#clear lists for group 1 info
maxList.clear()
minList.clear()
meanList.clear()
results.write("\n\n\n-----------------User Answers------------------------")
results.write('\nThe max,min,mean of the questions in group 1\n')
#cycles through group 1 and finds max, min, mean for each User
for x in range(0,group2start):
    rowNumber = x
    results.write('%s, ' %divorce.iloc[x,0:54].max())
    maxList.append(divorce.iloc[x,0:54].max())
    results.write('%s, ' %divorce.iloc[x,0:54].min())
    minList.append(divorce.iloc[x,0:54].min())
    results.write('%s, \n' %round((divorce.iloc[x,0:54].mean()), 2))
    meanList.append(divorce.iloc[x,0:54].mean())
#Adds the averages to the result file
results.write("\nThe averages of the max,min,mean\n")
results.write('%s, ' %mean(maxList))
results.write('%s, ' %mean(minList))
results.write('%s, ' %round((mean(meanList)),2))

maxList.clear()
minList.clear()
meanList.clear()
results.write('\n\n\nThe max,min,mean of the questions in group 2\n')
#cycles through group 1 and finds max, min, mean for each User
for x in range(group2start,group2end):
    rowNumber = x
    results.write('%s, ' %divorce.iloc[x,0:54].max())
    maxList.append(divorce.iloc[x,0:54].max())
    results.write('%s, ' %divorce.iloc[x,0:54].min())
    minList.append(divorce.iloc[x,0:54].min())
    results.write('%s, \n' %round((divorce.iloc[x,0:54].mean()), 2))
    meanList.append(divorce.iloc[x,0:54].mean())
#Adds the averages to the result file
results.write("\nThe averages of the max,min,mean\n")
results.write('%s, ' %mean(maxList))
results.write('%s, ' %mean(minList))
results.write('%s, ' %round((mean(meanList)),2))
#adding up each users score, how much they agreed or disagreed with the q's

#print(divorce.iloc[0:1,0:54].to_numpy())
#print(divorce.iloc[0,0:54].max())







    #Doing the clustering method
    #----------------------------------------------------------------------------------------

np.random.seed(1)
#plt.style.use('seaborn')

atr1 = divorce['Atr1']
atr4 = divorce["Atr4"]
ratio = test3
color = divorce["Atr5"]

plt.scatter(atr1, atr4, c=color, s=150, cmap='summer', edgecolor='black', linewidth=3, alpha=0.75)
cbar = plt.colorbar()
#cbar.set_label('Average Ratio of the ATR')
plt.title('ATR Plot')
plt.xlabel('Atr1')
plt.ylabel('Atr4')
plt.tight_layout()
plt.show()


plt.scatter(atr1, atr4, c=color, s=150, cmap='summer', edgecolor='black', linewidth=3, alpha=0.75)
cbar = plt.colorbar()
#cbar.set_label('Average Ratio of the ATR')
plt.xscale('log')
plt.yscale('log')
plt.title('ATR Plot')
plt.xlabel('Atr1')
plt.ylabel('Atr4')
plt.tight_layout()
plt.show()



    #----------------------------------------------------------------------------------------
bool = False
answer = input("\nDo you want to see demo clustering: y/n\n")
if answer == "y":
    bool = True

if bool == True:
    #demo custer using 
    x, _ = make_blobs(n_samples=300, centers=5, cluster_std=.8)
    plt.scatter(x[:,0], x[:,1])
    plt.show()

    aggloclust=AgglomerativeClustering(n_clusters=5).fit(x)
    print(aggloclust)
    labels = aggloclust.labels_

    plt.scatter(x[:,0], x[:,1], c=labels)
    plt.show()

    f = plt.figure()
    f.add_subplot(2, 2, 1)
    for i in range(2, 6):
        aggloclust=AgglomerativeClustering(n_clusters=i).fit(x)
        f.add_subplot(2, 2, i-1)
        plt.scatter(x[:,0], x[:,1], s=5, 
            c=aggloclust.labels_, label="n_cluster-"+str(i))
        plt.legend()
    plt.show()


    #----------------------------------------------------------------------------------------

results.close()