import HelperFunctions
from datetime import datetime
from datetime import date
import datetime
import random
import string

#General paremeters
cityname = "TestCity"
address = "Testaddress"
state = "TestState"
zipcode = "38479873"
regnum = "8454"
legalname = "fezgdz"
tradingname = "efje"
f_n = "abc"
l_n = "agn"
password = "Hi!12345"
email_length = 4
countryindex = 1
URL_length = 5
prod_or_uat = "UAT"
'''
##----------------------Test cases---------------------
#-------------------city------------
HelperFunctions.BeginTestBusiness("City Name")

# Test case number 1
cityname = ""
url = HelperFunctions.Generateurl(URL_length)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateMobileNumber(countryindex)
m_number = HelperFunctions.GenerateMobileNumber(countryindex)
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("1. Blank is not allowed", result)


#Test case number 2
cityname = " "
url = HelperFunctions.Generateurl(URL_length)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateMobileNumber(countryindex)
m_number = HelperFunctions.GenerateMobileNumber(countryindex)
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("2. Only Space as character is not allowed", result)


#Test case number 3
cityname = "123"
url = HelperFunctions.Generateurl(URL_length)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateMobileNumber(countryindex)
m_number = HelperFunctions.GenerateMobileNumber(countryindex)
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("3. Numerics are not allowed", result)


#Test case number 4
city = "$$"
url = HelperFunctions.Generateurl(URL_length)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateMobileNumber(countryindex)
m_number = HelperFunctions.GenerateMobileNumber(countryindex)
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("4. special characters are not allowed", result)
##-------------------------------end test case for city-----------------------




##------------------------------begin Test cases for Street Address----------------------
HelperFunctions.BeginTestBusiness("Street Address")

# Test case number 1
address = ""
cityname = "TestCity"
url = HelperFunctions.Generateurl(URL_length)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateMobileNumber(countryindex)
m_number = HelperFunctions.GenerateMobileNumber(countryindex)
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("1. Blank is not allowed", result)


#Test case number 2
address = " "
url = HelperFunctions.Generateurl(URL_length)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateMobileNumber(countryindex)
m_number = HelperFunctions.GenerateMobileNumber(countryindex)
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("2. Only Space as character is not allowed", result)


#Test case number 3
address = "&!§%"
url = HelperFunctions.Generateurl(URL_length)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateMobileNumber(countryindex)
m_number = HelperFunctions.GenerateMobileNumber(countryindex)
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("3. special characters are not allowed", result)
#--------------------------end testcases for street address-------------------------




#---------------------begin testcases for state---------------------------
address = "testaddress"
HelperFunctions.BeginTestBusiness("State")
# Test case number 1
state = " "
url = HelperFunctions.Generateurl(5)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateBusinesscontactNumber(5)
m_number = HelperFunctions.GenerateMobileNumber(1)
prod_or_uat = "UAT"
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("1. Only Space as character is not allowed", result)



#Test case number 2
state = ""
url = HelperFunctions.Generateurl(5)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateBusinesscontactNumber(5)
m_number = HelperFunctions.GenerateMobileNumber(1)
prod_or_uat = "UAT"
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("2. Blank is not allowed", result)

#Test case number 3
state = "123"
url = HelperFunctions.Generateurl(5)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateBusinesscontactNumber(5)
m_number = HelperFunctions.GenerateMobileNumber(1)
prod_or_uat = "UAT"
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("3. Numerics are not allowed", result)

#Test case number 4
state ="&§$"
url = HelperFunctions.Generateurl(5)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateBusinesscontactNumber(5)
m_number = HelperFunctions.GenerateMobileNumber(1)
prod_or_uat = "UAT"
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("4. special characters are not allowed", result)

#-----------------end testcases for state---------------------


#---------------------begin testcases for zipcode---------------------------
state = "TestState"
HelperFunctions.BeginTestBusiness("zipcode")
# Test case number 1
zipcode = " "
url = HelperFunctions.Generateurl(5)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateBusinesscontactNumber(5)
m_number = HelperFunctions.GenerateMobileNumber(1)
prod_or_uat = "UAT"
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("1. Only Space as character is not allowed", result)



#Test case number 2
zipcode = ""
url = HelperFunctions.Generateurl(5)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateBusinesscontactNumber(5)
m_number = HelperFunctions.GenerateMobileNumber(1)
prod_or_uat = "UAT"
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("2. Blank is not allowed", result)

#Test case number 3
zipcode = "abc"
url = HelperFunctions.Generateurl(5)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateBusinesscontactNumber(5)
m_number = HelperFunctions.GenerateMobileNumber(1)
prod_or_uat = "UAT"
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("3. Alphabets are not allowed", result)

#Test case number 4
zipcode="&§$"
url = HelperFunctions.Generateurl(5)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateBusinesscontactNumber(5)
m_number = HelperFunctions.GenerateMobileNumber(1)
prod_or_uat = "UAT"
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("4. special characters are not allowed", result)

#-------------------------end testcases for zipcode----------------------


#---------------------begin testcases for CompanyRegistrationNumber---------------------------
zipcode = "12345"
HelperFunctions.BeginTestBusiness("CompanyRegistrationNumber")
# Test case number 1
regnum = " "
url = HelperFunctions.Generateurl(5)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateBusinesscontactNumber(5)
m_number = HelperFunctions.GenerateMobileNumber(1)
prod_or_uat = "UAT"
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("1. Only Space as character is not allowed", result)



#Test case number 2
regnum = ""
url = HelperFunctions.Generateurl(5)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateBusinesscontactNumber(5)
m_number = HelperFunctions.GenerateMobileNumber(1)
prod_or_uat = "UAT"
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("2. Blank is not allowed", result)

#Test case number 3
regnum = "abc"
url = HelperFunctions.Generateurl(5)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateBusinesscontactNumber(5)
m_number = HelperFunctions.GenerateMobileNumber(1)
prod_or_uat = "UAT"
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("3. Alphabets are not allowed", result)

#Test case number 4
regnum ="&%§"
url = HelperFunctions.Generateurl(5)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateBusinesscontactNumber(5)
m_number = HelperFunctions.GenerateMobileNumber(1)
prod_or_uat = "UAT"
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("4. special characters are not allowed", result)

#-----------------------------end testcases or companyRegistrationNumber----------


#---------------------begin testcases for LegalCompanyName---------------------------
regnum = "12345"
HelperFunctions.BeginTestBusiness("Legel Name Of Company")
# Test case number 1
legalname = " "
url = HelperFunctions.Generateurl(5)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateBusinesscontactNumber(5)
m_number = HelperFunctions.GenerateMobileNumber(1)
prod_or_uat = "UAT"
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("1. Only Space as character is not allowed", result)


#Test case number 2
legalname = ""
url = HelperFunctions.Generateurl(5)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateBusinesscontactNumber(5)
m_number = HelperFunctions.GenerateMobileNumber(1)
prod_or_uat = "UAT"
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("2. Blank is not allowed", result)



#-----------------------------end testcases or Legelnameofcompany----------


#---------------------begin testcases for CompanyTradingName---------------------------
legalname = "TestLegalName"
HelperFunctions.BeginTestBusiness("Company Trading Name")

#Test case number 1
tradingname = ""
url = HelperFunctions.Generateurl(5)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateBusinesscontactNumber(5)
m_number = HelperFunctions.GenerateMobileNumber(1)
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("1. Blank is allowed", not result)
#-----------------------------end testcases for ComoanyTradingName----------



#---------------------begin testcases for URL---------------------------

HelperFunctions.BeginTestBusiness("Company Trading Name")
tradingname = "TestTradingName"
#Test case number 1
url = ""
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateBusinesscontactNumber(5)
m_number = HelperFunctions.GenerateMobileNumber(1)
prod_or_uat = "UAT"
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("7. Blank is not allowed", not result)

#Test case number 2.
#-------------------Valid URL-------------
#-----------------Checked Manually----------------

#-----------------------------end testcases for URL----------
#-------------------End testcases for first Page----------------------------------



#---------------------Test cases for Second page------------------------
##------------------------------begin Test cases for First Name----------------------
HelperFunctions.BeginTestBusiness("First Name")

# Test case number 1
f_n = ""
url = HelperFunctions.Generateurl(URL_length)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateMobileNumber(countryindex)
m_number = HelperFunctions.GenerateMobileNumber(countryindex)
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("1. Blank is not allowed", result)


#Test case number 2
f_n = " "
url = HelperFunctions.Generateurl(URL_length)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateMobileNumber(countryindex)
m_number = HelperFunctions.GenerateMobileNumber(countryindex)
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("2. Only Space as character is not allowed", result)


#Test case number 3
f_n = "123"
url = HelperFunctions.Generateurl(URL_length)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateMobileNumber(countryindex)
m_number = HelperFunctions.GenerateMobileNumber(countryindex)
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("3. Numerics are not allowed", result)


#Test case number 4
f_n = "&!§%"
url = HelperFunctions.Generateurl(URL_length)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateMobileNumber(countryindex)
m_number = HelperFunctions.GenerateMobileNumber(countryindex)
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("4. special characters are not allowed", result)

'''
#Test case number 5(checked manually,343 it is not taking)
f_n = "343hhh"
url = HelperFunctions.Generateurl(URL_length)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateMobileNumber(countryindex)
m_number = HelperFunctions.GenerateMobileNumber(countryindex)
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("5. Alphanumeric are not allowed", result)

#--------------------------end testcases for First Name-------------------------
'''

##------------------------------begin Test cases for Last Name----------------------
f_n = "TestFirst"
HelperFunctions.BeginTestBusiness("Last Name")
# Test case number 1
l_n = ""
url = HelperFunctions.Generateurl(URL_length)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateMobileNumber(countryindex)
m_number = HelperFunctions.GenerateMobileNumber(countryindex)
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("1. Blank is not allowed", result)


#Test case number 2
l_n = " "
url = HelperFunctions.Generateurl(URL_length)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateMobileNumber(countryindex)
m_number = HelperFunctions.GenerateMobileNumber(countryindex)
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("2. Only Space as character is not allowed", result)


#Test case number 3
l_n = "123"
url = HelperFunctions.Generateurl(URL_length)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateMobileNumber(countryindex)
m_number = HelperFunctions.GenerateMobileNumber(countryindex)
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("3. Numerics are not allowed", result)


#Test case number 4
l_n = "&!§%"
url = HelperFunctions.Generateurl(URL_length)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateMobileNumber(countryindex)
m_number = HelperFunctions.GenerateMobileNumber(countryindex)
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("4. special characters are not allowed", result)
'''

#Test case number 5
l_n = "343hhh"
url = HelperFunctions.Generateurl(URL_length)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateMobileNumber(countryindex)
m_number = HelperFunctions.GenerateMobileNumber(countryindex)
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("5. Alphanumeric are not allowed", result)

#--------------------------end testcases for Last Name-------------------------

#---------------------begin testcases for Email---------------------------

HelperFunctions.BeginTestBusiness("E-mail")
l_n = "TestLast"
#Test case number 1
email= ""
url = HelperFunctions.Generateurl(URL_length)
bcn = HelperFunctions.GenerateBusinesscontactNumber(5)
m_number = HelperFunctions.GenerateMobileNumber(1)
prod_or_uat = "UAT"
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("1. Blank is not allowed", result)
#-----------------------End testcases for E-mail--------------------


#BEGIN Test cases for "Date of Birth"
#----------------------
# This Test case should be done manually
#--------------------- End cases for "Date of Birth"--------------------


##------------------------------begin Test cases for Mobile Number----------------------
HelperFunctions.BeginTestBusiness("Mobile Number")

# Test case number 1
m_number = ""
url = HelperFunctions.Generateurl(URL_length)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateMobileNumber(countryindex)
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("1. Blank is not allowed", result)


#Test case number 2
m_number = "".join(random.choice(string.digits) for i in range(10))
url = HelperFunctions.Generateurl(URL_length)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateMobileNumber(countryindex)
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("2. Only valid numbers are accepted", result)

#---------------------------End testcases for mobile number----------------



##------------------------------begin Test cases for Business Contact Number----------------------
HelperFunctions.BeginTestBusiness("Business Contact Number")

# Test case number 1
bcn = ""
url = HelperFunctions.Generateurl(URL_length)
email= HelperFunctions.GenerateEmail_ID(email_length)
m_number = HelperFunctions.GenerateMobileNumber(countryindex)
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("1. Blank is not allowed", result)


#Test case number 2(not valid case,as business contact number can be anything)
bcn = "".join(random.choice(string.digits) for i in range(10))
url = HelperFunctions.Generateurl(URL_length)
email= HelperFunctions.GenerateEmail_ID(email_length)
m_number = HelperFunctions.GenerateMobileNumber(countryindex)
result = HelperFunctions.BusinessAccountRegistration(prod_or_uat, countryindex, cityname, address, state, 
                                                     zipcode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password)
HelperFunctions.SaveBusinessAccount(cityname, address, state, zipcode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictBusiness("2. only valid numbers are allowed", result)
#---------------------------End testcases for Business Contact Number----------------


#---------------------
#BEGIN Test cases for "Password"
#----------------------
# This Test case should be done manually
#---------------------
#BEGIN Test cases for "Password"
#----------------------
#