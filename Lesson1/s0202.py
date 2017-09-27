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
            if data != None:
                states.append(data)
            data = []
            data.append(newest)
            est = newest
finally:
    f.close()

# write the results in a csv file 2000 a 2003
f = open("2009pivot.csv",'wt')
try:
    writer = csv.writer(f)
    writer.writerow(('city','year','weekofyear','week_start_date','ndvi_ne','ndvi_nw','ndvi_se','ndvi_sw','precipitation_amt_mm','reanalysis_air_temp_k','reanalysis_avg_temp_k','reanalysis_dew_point_temp_k','reanalysis_max_air_temp_k','reanalysis_min_air_temp_k','reanalysis_precip_amt_kg_per_m2','reanalysis_relative_humidity_percent','reanalysis_sat_precip_amt_mm','reanalysis_specific_humidity_g_per_kg','reanalysis_tdtr_k','station_avg_temp_c','station_diur_temp_rng_c','station_max_temp_c','station_min_temp_c','station_precip_mm'))
    for i in range(1,len(states)):
        writer.writerow((states[i]))
finally:
    f.close()
    
