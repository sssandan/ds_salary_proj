#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 02:29:37 2020

@author: ryan
"""

import glassdoor_scraper as gs
import pandas as pd

path = "/Users/ryan/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist', 30, False, path, 5)

