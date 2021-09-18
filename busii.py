import HelperFunctions
from datetime import datetime
from datetime import date
import datetime

#General paremeters
cityname = "TestCity"
state = "TestState"
ziocode = "38479873"
regnum = "8454"
legalname = "fezgdz"
tradingname = "efje"
f_n = "abc"
l_n = "agn"
password = "Hi!12345"
password1 = "Hi!12345"
email_length = 4


##----------------------Test cases---------------------
##---------city-----------

# Test case number 1
countryindex = 15
url = HelperFunctions.Generateurl(5)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateBusinesscontactNumber(5)
m_number = HelperFunctions.GenerateMobileNumber_NIGIRIEA(7)
result = HelperFunctions.BusinessAccountRegistration(countryindex, cityname, state, 
                                                     ziocode, regnum, legalname, 
                                                     tradingname, url, f_n, l_n, email, 
                                                     bcn, m_number, password, password1)
HelperFunctions.SaveBusinessAccount(cityname, state, ziocode, regnum, legalname, 
                                    tradingname, url, f_n, l_n, email, bcn, 
                                    m_number, password)
HelperFunctions.SetVerdictforbusiness("Account Created ?: ", result)
HelperFunctions.SetVerdict("1. Space is not allowed", result)
HelperFunctions.Activate_account(email)
HelperFunctions.Account_login(bcn, password)


'''#Test case number 2
cityname = ""
url = HelperFunctions.Generateurl(5)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateBusinesscontactNumber(5)
m_number = HelperFunctions.GenerateMobileNumber(7)
result = HelperFunctions.BusinessAccountRegistration(cityname, state, ziocode, regnum, legalname, tradingname, url, f_n, l_n, email, bcn, m_number, password, password1)
HelperFunctions.SetVerdictforbusiness("Account Created ?: ", result)
HelperFunctions.SetVerdict("1. Space is not allowed", result)

#Test case number 3
cityname = "123"
url = HelperFunctions.Generateurl(5)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateBusinesscontactNumber(5)
m_number = HelperFunctions.GenerateMobileNumber(7)
result = HelperFunctions.BusinessAccountRegistration(cityname, state, ziocode, regnum, legalname, tradingname, url, f_n, l_n, email, bcn, m_number, password, password1)
HelperFunctions.SetVerdictforbusiness("Account Created ?: ", result)
HelperFunctions.SetVerdict("1. Space is not allowed", result)

#Test case number 4
cityname = "§§"
url = HelperFunctions.Generateurl(5)
email= HelperFunctions.GenerateEmail_ID(email_length)
bcn = HelperFunctions.GenerateBusinesscontactNumber(5)
m_number = HelperFunctions.GenerateMobileNumber(7)
result = HelperFunctions.BusinessAccountRegistration(cityname, state, ziocode, regnum, legalname, tradingname, url, f_n, l_n, email, bcn, m_number, password, password1)
HelperFunctions.SetVerdictforbusiness("Account Created ?: ", result)
HelperFunctions.SetVerdict("1. Space is not allowed", result)
'''