# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 09:46:17 2021

@author: Divya and Harshal
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
#import select
import random

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://demo.e-pocketexchange.com/welcome/")
print(driver.title)
driver.maximize_window()
  
  #Start with main page
driver.find_element_by_class_name("btn-get-started").click()
driver.find_element_by_partial_link_text("Sign Up").click()
driver.find_element_by_class_name("business").click()
time.sleep(1)
  
#Business account regitration page
driver.find_element_by_name('city').send_keys("cityname")
driver.find_element_by_name('address').click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_id("us3-address").send_keys("test")
driver.find_element_by_id("sendAddr").click()
driver.switch_to.window(driver.window_handles[0])
driver.find_element_by_name('state').send_keys("state")
driver.find_element_by_name('postal').send_keys(78549)
driver.find_element_by_name('company_reg_number').send_keys(45894)
driver.find_element_by_name('company_legal_name').send_keys("legalname")
driver.find_element_by_name('company_trading_name').send_keys("tradingname")
driver.find_element_by_name('industry').click()
##select(driver.find_element_by_xpath("/html/body/app-root/div/app-bregister/div/div[3]/form[1]/div/div[6]/div[1]/div/select").click())
driver.find_element_by_name('weburl').send_keys("www.hfu.com")
driver.find_element_by_class_name("btn-primary").click()
driver.find_element_by_name('first_name').send_keys("f_n")
driver.find_element_by_name('last_name').send_keys("l_n")
driver.find_element_by_name('email').send_keys("fhu@yopmail.com")
driver.find_element_by_name('dob1').click()
driver.find_element_by_xpath('//*[@id="mat-datepicker-0"]/div/mat-month-view/table/tbody/tr[3]/td[5]/div[1]').click()
driver.find_element_by_name('mobile_no').send_keys(408006)
driver.find_element_by_name('phone').send_keys("0408006888")    
driver.find_element_by_name('password').send_keys("Hi!12345")
driver.find_element_by_name('conf_pass').send_keys("Hi!12345")
driver.find_element_by_class_name("btn-primary").click()
driver.find_element_by_name('monthly_transaction').click()
drop = Select(driver.find_element_by_name('average_sale_amount')).select_by_index(3)
#time.sleep(8)
driver.find_element_by_class_name("btn-primary").click()
driver.find_element_by_class_name('btn-border').click()
#Time to check the result
time.sleep(30)
#ToDo: Enter user input before closing the 
#driver.quit()
