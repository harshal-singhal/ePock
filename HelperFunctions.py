# -*- coding: utf-8 -*
"""
Created on Wed Jul 21 17:30:01 2021
@author: Divya and Harshal
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
from email.parser import HeaderParser
import imaplib,time





#-------------Individual Registration--------------
def IndividualAccountRegistration(f_n, l_n, email, address, m_number, password, countryindex):
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    #driver.get("https://www.e-pocketexchange.com/epportal/login")
    driver.get("http://demo.e-pocketexchange.com/epportal/login")
    driver.maximize_window()
    
    #Start with main page
    driver.find_element_by_partial_link_text("Sign Up").click()
    driver.find_element_by_class_name("normal").click()
    time.sleep(1)
    
    #Individual account registration Page
    driver.find_element_by_name('first_name').send_keys(f_n)
    driver.find_element_by_name('last_name').send_keys(l_n)
    driver.find_element_by_name('email').send_keys(email)
    
    county_x_path = "/html/body/app-root/div/app-nregister/div/form/div/div[3]/div[1]/div/div/ul/li[" + str(countryindex)   + "]"
    driver.find_element_by_class_name('coutry-dropdown').click()
    time.sleep(1)
    driver.find_element_by_xpath(county_x_path).click()
    
    
    driver.find_element_by_name('address').send_keys(address)
    driver.find_element_by_name('mobile_no').send_keys(m_number)    
    driver.find_element_by_name('dob1').click()
    driver.find_element_by_xpath('//*[@id="mat-datepicker-0"]/div/mat-month-view/table/tbody/tr[1]/td[3]/div[1]').click()
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("conf_pass").send_keys(password)
    driver.find_element_by_class_name("btn-primary").click()
    time.sleep(2)
    
    try:
        driver.find_element_by_xpath("""//*[@id="exampleModal"]/div/div/div[2]/button""").click()
    except NoSuchElementException:
        print ("Account couldn't be created !!")
        time.sleep(1)
        driver.quit()
        return False  
    #It means Account is created Successfully
    print ("Account is created successfully !!!")
    time.sleep(1)
    driver.quit()
    return True

    
#---------------Business Registration--------------
def BusinessAccountRegistration(countryindex, cityname, state, ziocode, regnum, legalname, tradingname, url, f_n, l_n, email, bcn, m_number, password, password1):
  PATH = "C:\Program Files (x86)\chromedriver.exe"
  driver = webdriver.Chrome(PATH)
  #driver.get("http://demo.e-pocketexchange.com/welcome/")
  driver.get("http://demo.e-pocketexchange.com/epportal/login")
  print(driver.title)
  driver.maximize_window()
    
  #Start with main page
  #driver.find_element_by_class_name("btn-get-started").click()
  driver.find_element_by_partial_link_text("Sign Up").click()
  driver.find_element_by_class_name("business").click()
  time.sleep(1)
    
  # 1st page starts here
  #/html/body/app-root/div/app-bregister/div/div[3]/form[1]/div/div[3]/div[1]/div/div/ul/li[2]
  county_x_path = "/html/body/app-root/div/app-bregister/div/div[3]/form[1]/div/div[3]/div[1]/div/div/ul/li[" + str(countryindex)   + "]"
  driver.find_element_by_class_name('coutry-dropdown').click()
  driver.find_element_by_xpath(county_x_path).click()
  driver.find_element_by_name('city').send_keys(cityname)
  driver.find_element_by_name('address').click()
  driver.switch_to.window(driver.window_handles[1])
  driver.find_element_by_id("us3-address").send_keys("test")
  driver.find_element_by_id("sendAddr").click()
  driver.switch_to.window(driver.window_handles[0])
  driver.find_element_by_name('state').send_keys(state)
  driver.find_element_by_name('postal').send_keys(ziocode)
  driver.find_element_by_name('company_reg_number').send_keys(regnum)
  driver.find_element_by_name('company_legal_name').send_keys(legalname)
  driver.find_element_by_name('company_trading_name').send_keys(tradingname)
  driver.find_element_by_name('industry').click()
  driver.find_element_by_name('weburl').send_keys(url)
  driver.find_element_by_class_name("btn-primary").click()
  
  
  # 2nd page starts here
  try:
      driver.find_element_by_name('first_name').send_keys(f_n)
  except NoSuchElementException:
      print("invalid field found in first page: PASS for test case")
      time.sleep(2)
      driver.quit()
      return True
  driver.find_element_by_name('last_name').send_keys(l_n)
  driver.find_element_by_name('email').send_keys(email)
  driver.find_element_by_name('dob1').click()
  driver.find_element_by_xpath('//*[@id="mat-datepicker-0"]/div/mat-month-view/table/tbody/tr[1]/td[2]/div[1]').click()
  driver.find_element_by_name('mobile_no').send_keys(bcn)
  driver.find_element_by_name('phone').send_keys(m_number)    
  driver.find_element_by_name('password').send_keys(password)
  driver.find_element_by_name('conf_pass').send_keys(password)
  driver.find_element_by_class_name("btn-primary").click()
  
  
  # 3rd page starts here
  try:
      driver.find_element_by_name('monthly_transaction').click()
  except NoSuchElementException:
      print("invalid field found in second page: PASS for test case")
      time.sleep(2)
      driver.quit()
      return True
  Select(driver.find_element_by_name('average_sale_amount')).select_by_index(3)
  #time.sleep(2)
  driver.find_element_by_class_name("btn-primary").click()
 
  root = tk.Tk()
  root.withdraw()
  verdict = messagebox.askyesno("Verdict", "Account created or not ?")
  print(verdict)
  time.sleep(2)
  driver.quit()
  return verdict 
  
  
def SetVerdictforbusiness(Check_statement, verdict):
    File_Handle = open("BusinessAccount.txt", 'a')
    File_Handle.write("\n" + Check_statement + ": ")
    if verdict:
        File_Handle.write("Created")
    else:
        File_Handle.write("Not Created")
    File_Handle.write("\n\n")
    File_Handle.close() 
  
##------------------Email-id generation------------
def GenerateEmail_ID(length):
  email_length = length
  email_random = "".join(random.choice(string.ascii_lowercase) for i in range(email_length))
  email = email_random + "@yopmail.com"
  return email

#--------------------Random string --------------
def GenerateName(length):
  name = "".join(random.choice(string.ascii_lowercase) for i in range(length))
  return name

##---------------------MobileNumber generation-----------
def GenerateMobileNumber(countryIndex):
  mobile = 0
  if(countryIndex == 1):
      print("Country: Australia")
      mobile_length = 7
      mobile_random = "".join(random.choice(string.digits) for i in range(mobile_length))
      mobile = "040" + mobile_random
      return mobile
  else:
      print("Todo: Other countries. ERROR has occurred")
      return mobile

##---------------------MobileNumber generation for New zealand-----------
def GenerateMobileNumber_NZ(length):
  mobile_length = 5 #total length is 9 for new zealand
  mobile_random = "".join(random.choice(string.digits) for i in range(mobile_length))
  mobile = "0943" + mobile_random
  return mobile

##-------------------------------Mobilenumber for nigeria---------------------
def GenerateMobileNumber_NIGIRIEA(length):
  mobile_length = 7 #total length is 10 for nigiria
  mobile_random = "".join(random.choice(string.digits) for i in range(mobile_length))
  mobile = "706" + mobile_random
  return mobile
##-------------Business contact number-----------------
def GenerateBusinesscontactNumber(length):
  mobile_length = length
  mobile_random = "".join(random.choice(string.digits) for i in range(mobile_length))
  bcn = "176" + mobile_random
  return bcn

##---------------URL generation-------------
def Generateurl(length):
  url_length = length
  url_random = "".join(random.choice(string.ascii_lowercase) for i in range(url_length))
  url = "www." + url_random + ".com"
  return url

##----------------------Writting in file-------------------

def SaveIndividualAccount(f_name, l_name, email, address, mobile, password, c_Index):
    File_Handle = open("IndividualAccount.txt", 'a')
    File_Handle.write("\nIndividual Account details: \n"
                      + "First name: " + f_name     + "\n"
                      + "Last name: "  + l_name     + "\n"
                      + "Email: "      + email      + "\n"
                      + "Country: "    + str(c_Index)    + "\n"
                      + "Address: "    + address    + "\n"
                      + "Mobile: "     + mobile     + "\n"
                      + "Password: "   + password)
    File_Handle.close()
    
def SaveBusinessAccount(cityname, state, ziocode, regnum, legalname, tradingname, url, f_n, l_n, email, bcn, m_number, password):  
    #datetime.date.today().strftime("%B %d, %Y")
    #c = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    ##--------------------Date-------------
    File_Handle = open("BusinessAccount.txt", 'a')
    File_Handle.write("Details of the user:\n"
    ##----------time---------------
    "-----------------Begin----------------------"
    "Account details: \n"
    #+ "Current_time_Time:"      + c             + "\n"
    + "City name: "             + cityname      + "\n"
    + "state: "                 + state         + "\n"
    + "Zipcode: "               + ziocode       + "\n"
    + "Registrationnumber: "    + regnum        + "\n"
    + "Legal name: "            + legalname     + "\n"
    + "Trading name: "          + tradingname   + "\n"
    + "Url: "                   + url           + "\n"
    + "First_name: "            + f_n           + "\n"
    + "Last_Name: "             + l_n           + "\n"
    + "E_mail: "                + email         + "\n"
    + "Busii_Num: "             + bcn           + "\n"
    + "Mobile_Number: "         + m_number      + "\n"
    + "Password: "              + password)
    File_Handle.close()

def BeginTest(field_name):
    File_Handle = open("IndividualAccount.txt", 'a')
    File_Handle.write("\n-----------------Begin----------------------\n"
                      "Test case for: " + field_name + "\n"
                      "---------------------------------------\n")
    File_Handle.close()

def SetVerdictIndividual(Check_statement, AccountCreatedOrNot):
    File_Handle = open("IndividualAccount.txt", 'a')
    File_Handle.write("\n" + Check_statement + ": ")
    if AccountCreatedOrNot:
        File_Handle.write("FAIL")
    else:
        File_Handle.write("PASS")
    File_Handle.write("\n\n")
    File_Handle.close()
    
def SetVerdict(Check_statement, verdict):
    File_Handle = open("BusinessAccount.txt", 'a')
    File_Handle.write("\n" + Check_statement + ": ")
    if verdict:
        File_Handle.write("PASS")
    else:
        File_Handle.write("FAIL")
    File_Handle.write("\n\n")
    File_Handle.close()

def DisplayAll(f_name, l_name, email, mobile, password):
    print("Individual Account details: \n"
                      + "First name: " + f_name     + "\n"
                      + "Last name: "  + l_name     + "\n"
                      + "Email: "      + email      + "\n"
                      + "Mobile: "     + mobile     + "\n"
                      + "Password: "   + password)  

##------------------------------Account activation------------
def Activate_account(email):
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://yopmail.com/en/")
    print(driver.title)
    driver.maximize_window()
    driver.find_element_by_id('accept').click()
    #driver.find_element_by_xpath('//*[@id="accept"]')
    ##email = HelperFunctions.GenerateEmail_ID(4)
    print(email)
    driver.find_element_by_class_name('ycptinput').send_keys(email)
    driver.find_element_by_xpath('//*[@id="refreshbut"]/button/i').click()
    driver.switch_to_frame("ifmail")
    ep = driver.find_element_by_link_text('link')
    driver.implicitly_wait(500)
    ep.click()
    time.sleep(10)
    
    
#-------------------for login---------------------------
    
def Account_login(bcn, password):
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("http://demo.e-pocketexchange.com/epportal/login")
    driver.maximize_window()
    driver.find_element_by_id("mob").send_keys(bcn)
    password2 = password
    driver.find_element_by_id("password").send_keys(password2)
    driver.find_element_by_class_name("btn-primary").click()
    time.sleep(5)
    driver.find_element_by_id("exampleModal").click()
    driver.switch_to.window(driver.window_handles[-1])
    driver.find_element_by_xpath("""//*[@id="exampleModal"]/div/div/div[2]/button[1]""").click()