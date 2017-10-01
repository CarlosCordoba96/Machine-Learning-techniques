# -*- coding: utf-8 -*-
"""

"""

import csv
import pandas as pd 

def nullvalues():
    #Using pandas package the method fillna replace the NaN values with the mean of the columns
    table = pd.read_csv("Data\ iq_2000_2003_pivot.csv", index_col='weekofyear')
    table = table.fillna(table.mean())
    table.to_csv("Data\ iq_2000_2003_pivot.csv", sep=',')


f = open("Data\dengue_features_train.csv", 'rt')
est = ""

try:
    g = open("Data\ iq_2000_2003_pivot.csv", 'wt')
    writer = csv.writer(g)
    writer.writerow(('weekofyear',
                     'ndvi_ne', 'ndvi_nw', 'ndvi_se', 'ndvi_sw',
                     'precipitation_amt_mm', 'reanalysis_air_temp_k', 'reanalysis_avg_temp_k',
                     'reanalysis_dew_point_temp_k', 'reanalysis_max_air_temp_k', 'reanalysis_min_air_temp_k',
                     'reanalysis_precip_amt_kg_per_m2', 'reanalysis_relative_humidity_percent',
                     'reanalysis_sat_precip_amt_mm', 'reanalysis_specific_humidity_g_per_kg', 'reanalysis_tdtr_k',
                     'station_avg_temp_c', 'station_diur_temp_rng_c', 'station_max_temp_c', 'station_min_temp_c',
                     'station_precip_mm'))
    reader = csv.reader(f)
    data = None

    fallos = []
    for row in reader:

        newest = row[0]
        year = row[1]
        if 'iq' == newest:
            i_year = int(year)
            if i_year >= 2000 and i_year <= 2003:

                #Elimina ciudad, año y fecha (semana podría ser identificador, pero no es un dato único, se repite en muchas filas)
                del row[0]
                del row[0]
                del row[1]

                print row

                for i in range(len(row)-1):
                    if (row[i] == ""):
                        row[i]=0
                        fallos.append(i)
                        print "atenció"
                    row[i] = float(row[i])
                writer.writerow(row)

finally:
    f.close()
nullvalues()    #lista de columnas donde falla y hay un 0

