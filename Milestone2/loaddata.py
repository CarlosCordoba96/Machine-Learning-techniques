# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 12:05:59 2016

@author: FranciscoP.Romero
"""
import codecs
def load_data_usa(path):
        
    try:
        f = codecs.open("Data/iq_2000_2003_pivot.csv", "r", "utf-8")
        cases = []
        count = 0
        for line in f:
            if count > 0: 
                # Insert a 0 in unfilled fields
                while ",," in line:
                    line = line.replace(',,', ',0,')
                line = line.replace(',\n', ',0')
                
                row = line.split(",")
                if row != []:
                            
                    cases.append(map(float, row))
            count += 1
        f.close()
    except:
        print("Error while loading the data")
 
   
    return cases