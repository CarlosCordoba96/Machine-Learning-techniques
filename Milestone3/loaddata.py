# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 12:05:59 2016

@author: FranciscoP.Romero
"""
import codecs
def load_data():
#We retake the code of a previour version because we have some problems with our code
#Defines the method that takes our data set and saves it into a variable to work with it
    try:
        f = codecs.open("Data/dengue_features_train.csv", "r", "utf-8")
        cases = []
        count = 0
        for line in f:
            if count > 0:             
                row = line.split(",")
                if row[0] == "iq":
                    if int(row[1])>=2000 and int(row[1])<=2003:
                        if row != []:
                            row = row[4:]#We delete the 4 first columns because we consider outliers
                            cases.append(map(float, row))
            count += 1
        f.close()
    except:
        print("Error while loading the data")
        sys.exit()

 
   
    return cases
