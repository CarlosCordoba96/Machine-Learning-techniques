# -*- coding: utf-8 -*-
"""

"""

import csv


f = open("2009.csv", 'rt')
states = []
est = ""
try:
    reader = csv.reader(f)
    data = None
    for row in reader:
    	newest = row[1]
    	if est == newest:
          # process the indentation spaces
    		if row[3].rfind("  ") == 2:
    			data.append(row[4])
    	else:
    		if data != None and len(data) > 1:
    			states.append(data)
    		data = []
    		data.append(newest)
    		est = newest
   		         
finally:
    f.close()

states.append(data)    
    
print states
# write the results in a csv file
f = open("2009pivot.csv",'wt')
try:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(('State','Agriculture','Mining','Utilities','Construction',
                     'Manufacturing','Wholesale trade','Retail','Transportation',
                     'Information','Finance', 'Buss. Services','Education','Arts','Oth Serv.','Fed. civ','Fed. military','State'))
    writer.writerows(states)
finally:
    f.close()
    
