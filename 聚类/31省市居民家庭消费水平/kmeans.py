# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 10:43:28 2017

@author: zt
"""

import numpy as np
from sklearn.cluster import KMeans
 
 
def loadData(filePath):
    fr = open(filePath,'r+')
    lines = fr.readlines()
    retData = []
    retCityName = []
    for line in lines:
        items = line.strip().split(",")
        retCityName.append(items[0])
        retData.append([float(i) for i in items[1:]])
    return retData,retCityName
 
     
if __name__ == '__main__':
    data,cityName = loadData('city.txt')
    clusters = 4
    km = KMeans(n_clusters=clusters)
    label = km.fit_predict(data)
    expenses = np.sum(km.cluster_centers_,axis=1)
    CityCluster = [[] for i in range(clusters)]  
 
    for i in range(len(cityName)):
        CityCluster[label[i]].append(cityName[i])
    CityClusterExpensesDescending = sorted(list(zip(expenses, CityCluster)), key=lambda x: x[0], reverse=True)
    for expens, city in CityClusterExpensesDescending:
        print("Expenses:%.2f" % expens)
        print(city)