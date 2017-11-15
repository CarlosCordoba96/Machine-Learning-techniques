# -*- coding: utf-8 -*-

"""
Created on Mon Nov 13 17:38:59 2016
@author: Julián
"""
import codecs
import sys
def load_data():

### 1. Load the data asigned
    try:
        f = codecs.open("out.csv", "r", "utf-8")
        cases = []
        count = 0
        for line in f:
            if count > 0:
                # Insert a 0 in unfilled fields
                while ",," in line:
                    line = line.replace(',,', ',0,')
                line = line.replace(',\n', ',0')                
                row = line.split(",")
                if row[0] == "iq":
                    if row != []:
                        row = row[4:]#We delete the 4 first columns because we don't need to study them
                        cases.append(map(float, row))
            count += 1
        f.close()
    except:
        print("Error while loading the data")
        sys.exit()

 
   
    return cases