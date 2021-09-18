# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 16:09:59 2021

@author: hrshl
"""

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
#import selenium.webdriver.common.alert.Alert as Alert
from selenium import webdriver
import tkinter as tk
from tkinter import messagebox
import random
import string
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException




PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://demo.e-pocketexchange.com/epportal/login")
driver.maximize_window()

#Start with login
driver.find_element_by_id("mob").send_keys(9876543210)
password = "Ashna@1991"
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_class_name("btn-primary").click()
time.sleep(5)

#driver.find_element_by_id("exampleModal").click()

driver.switch_to.window(driver.window_handles[-1])
driver.find_element_by_xpath('//*[@id="exampleModal"]/div/div/div[2]/button[1]').click()
#driver.find_element_by_class_name('nav-link').click()







