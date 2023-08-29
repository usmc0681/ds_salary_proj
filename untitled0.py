# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 10:11:34 2023

@author: usmc0
"""

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

path = "C:/Users/usmc0/Documents/ds_salary_proj/chromedriver"

driver = webdriver.Chrome(options = options)
## open selenium URL in chrome browser
driver.get('https://www.glassdoor.com/Job/jobs.htm?sc.keyword="data scientist"&locT=C&locId=1147401&locKeyword=San%20Francisco,%20CA&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0')

# username = driver.find_element(By.NAME, 'username')
 

