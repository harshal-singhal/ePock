# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 12:29:03 2021

@author: Divya and Harshal
"""
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from email.parser import HeaderParser
import HelperFunctions
import imaplib,time
import string

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://yopmail.com/en/")
print(driver.title)
driver.maximize_window()
driver.find_element_by_id('accept').click()
#driver.find_element_by_xpath('//*[@id="accept"]')
##email = HelperFunctions.GenerateEmail_ID(4)
email = "div112"
print(email)
driver.find_element_by_class_name('ycptinput').send_keys(email)
driver.find_element_by_xpath('//*[@id="refreshbut"]/button/i').click()
'''

T=time.time()
M=imaplib.IMAP4_SSL("imap.yopmail.com")
M.select() 
typ, data = M.search(None, 'UNSEEN SINCE T')
for num in string.split(data[0]):
       typ, data=M.fetch(num,'(RFC822)')
       msg=email.message_from_string

'''
driver.switch_to_frame("ifmail")
ep = driver.find_element_by_link_text('link')
driver.implicitly_wait(500)
ep.click()


