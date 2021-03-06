# -*- coding: utf-8 -*-
"""(US)Total Suicide No. by age group.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ll1ob4lNMCaTodZRN9R9gmr_SaC1_4Ng
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab

from google.colab import files
uploaded = files.upload()

import io
df = pd.read_csv(io.BytesIO(uploaded['master.csv']))
# Dataset is now stored in a Pandas Dataframe

#selecting just the entries of US
us = df.loc[df['country'] == 'United States']

#melting male and female entries that have the same year, averaging their suicide_no
us2 = us.pivot_table(index=['age'],
                             columns='year',
                             values='suicides_no', aggfunc=np.average)

#dividing up by age groups
youngest = us2.loc['5-14 years'].values.tolist()
teen = us2.loc['15-24 years'].values.tolist()
adult = us2.loc['25-34 years'].values.tolist()
middle = us2.loc['35-54 years'].values.tolist()
older = us2.loc['55-74 years'].values.tolist()
senior = us2.loc['75+ years'].values.tolist()


year = [1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]

#plotting each age group suicide rates for each year. X = year, Y = suicide rates(by age group)
plt.plot(year, youngest, color='yellow', label='5-14')
plt.plot(year, teen, color='orange',label='15-24')
plt.plot(year, adult, color='green', label='25-34')
plt.plot(year, middle, color='blue',label = '35-54')
plt.plot(year, older, color='black',label='55-74')
plt.plot(year, senior, color='grey',label='75+')

plt.xlabel('Year')
plt.ylabel('No. Suicides')
plt.title('Avg No. of suicides in the US for different age groups from 1985-2016')
pylab.legend(loc='upper left')
plt.show()