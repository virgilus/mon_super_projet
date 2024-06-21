#!/usr/bin/env python
# coding: utf-8

# # "Countries.csv"

import pandas as pd
import os

RAW_DATA_PATH = '../data/raw/'
PROCESSED_DATA_PATH = '../data/processed/'
COUNTRIES_FILENAME = 'countries.csv'

def rename_processed_data(filename, str_to_replace='.', new_string='_processed.'):
    return filename.replace(str_to_replace, new_string)

d = {'country': 'string',
     'region': 'category',
     'population': 'int32',
     'area (km²)': 'int32',
     'coastline (coast/area ratio)': 'float32',
     'net migration': 'float32',}

df = pd.read_csv(os.path.join(RAW_DATA_PATH, COUNTRIES_FILENAME),
                 sep=';',
                 skiprows=3,
                 quotechar='#',
                 decimal=',',
                 usecols=d.keys(),
                 dtype=d,
                 #nrows=10000,
                )
# ### Density computation
df['density (km²)'] = df['population'] / df['area (km²)']

# ### Export to a clean CSV
df.to_csv(os.path.join(PROCESSED_DATA_PATH, rename_processed_data(COUNTRIES_FILENAME)))

