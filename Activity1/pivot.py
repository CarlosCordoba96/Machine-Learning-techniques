# -*- coding: utf-8 -*-
"""

"""

import csv


f = open("Data\dengue_features_train.csv", 'rt')
states = []
est = ""

try:
    g = open("2009pivot.csv", 'wt')
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
    for row in reader:
        newest = row[0]
        year = row[1]
        if 'iq' == newest:
            if int(year) >= 2000 and int(year) <= 2003:
                print row
                #for i in range(1,len(row)):
                #data.append(row)
                writer.writerow(row)
finally:
    f.close()
