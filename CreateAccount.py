# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 19:33:14 2021
@author: Divya and Harshal
"""


from selenium.webdriver.support.ui import Select
import HelperFunctions
from selenium import webdriver
import tkinter as tk
from tkinter import messagebox
import random
import string
import time

#Parameters
f_n = HelperFunctions.GenerateName(4)
l_n = HelperFunctions.GenerateName(4)
email = HelperFunctions.GenerateEmail_ID(4)
m_number = HelperFunctions.GenerateMobileNumber(7)
address = "Test Address"
password = "Hi!12345"
#-------------------

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
#driver.get("http://demo.e-pocketexchange.com/welcome/")
driver.get("https://www.e-pocketexchange.com/welcome/")


driver.maximize_window()

#Start with main page
driver.find_element_by_class_name("btn-get-started").click()
driver.find_element_by_partial_link_text("Sign Up").click()
driver.find_element_by_class_name("normal").click()
time.sleep(1)

#Individual account registration Page
driver.find_element_by_name('first_name').send_keys(f_n)
driver.find_element_by_name('last_name').send_keys(l_n)
driver.find_element_by_name('email').send_keys(email)
driver.find_element_by_name('address').send_keys(address)
driver.find_element_by_name('mobile_no').send_keys(m_number)    
driver.find_element_by_name('dob1').click()
driver.find_element_by_xpath('//*[@id="mat-datepicker-0"]/div/mat-month-view/table/tbody/tr[1]/td[3]/div[1]').click()
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_name("conf_pass").send_keys(password)
driver.find_element_by_class_name("btn-primary").click()

time.sleep(1)
HelperFunctions.DisplayAll(f_n, l_n, email, m_number, password)
driver.quit()
    