# -*- coding: utf-8 -*-
"""

"""

import csv
def unique_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x




f = open("Data\dengue_features_train.csv", 'rt')
states = []
est = ""

try:
    g = open("Data\ 2009pivot.csv", 'wt')
    writer = csv.writer(g)
    writer.writerow(('city', 'year', 'weekofyear', 'week_start_date', 'ndvi_ne', 'ndvi_nw', 'ndvi_se', 'ndvi_sw',
                     'precipitation_amt_mm', 'reanalysis_air_temp_k', 'reanalysis_avg_temp_k',
                     'reanalysis_dew_point_temp_k', 'reanalysis_max_air_temp_k', 'reanalysis_min_air_temp_k',
                     'reanalysis_precip_amt_kg_per_m2', 'reanalysis_relative_humidity_percent',
                     'reanalysis_sat_precip_amt_mm', 'reanalysis_specific_humidity_g_per_kg', 'reanalysis_tdtr_k',
                     'station_avg_temp_c', 'station_diur_temp_rng_c', 'station_max_temp_c', 'station_min_temp_c',
                     'station_precip_mm'))
    reader = csv.reader(f)
    data = None

    fallos=[]
    for row in reader:

        newest = row[0]
        year = row[1]
        if 'iq' == newest:
            if int(year) >= 2000 and int(year) <= 2003:

                print row
                del row[0]
                for i in range(len(row)-1):
                    if (row[i] == ""):
                        row[i]=0
                        fallos.append(i)
                        print "atenció"
                writer.writerow(row)


    fallos=sorted(unique_list(fallos))#lista de columnas donde falla y hay un 0
finally:
    f.close()
