# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 21:23:25 2023

@author: usmc0
"""

import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/usmc0/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist', 900, False, path, 15)