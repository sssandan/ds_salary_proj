#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 21:16:28 2020

@author: ryan
"""

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

# salary parsing (take out the glassdoor estimate)
# company name text only
# replace cities, state as state instead
# age of company 
# parsing of job description (python, etc)

    
    
df = df[df['Salary Estimate'] != '-1']

# taking out the "glassdoor estimate" from the salary estimate column
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
salary = salary.apply(lambda x: x.replace('K', '').replace('$', ''))