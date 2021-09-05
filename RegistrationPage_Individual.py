import HelperFunctions
import random
import string

#Parameters for individual account
F_name = "Test_first_name"
L_name = "Test_last_name"
password = "Hi!12345" 
address = "test address"
email_length = 4
number_length = 7

#---------------------
#BEGIN Test cases for "First Name"
#----------------------
HelperFunctions.BeginTest("First Name")

# Test case number 1
F_name = " "
email = HelperFunctions.GenerateEmail_ID(email_length)
mobile = HelperFunctions.GenerateMobileNumber(number_length)
HelperFunctions.SaveIndividualAccount(F_name, L_name, email, address, mobile, password)
result = HelperFunctions.IndividualAccountRegistration(F_name, L_name, email, address, mobile, password)
HelperFunctions.SetVerdictIndividual("1. Space is not allowed", result)

# Test case number 2
F_name = ""
email = HelperFunctions.GenerateEmail_ID(email_length)
mobile = HelperFunctions.GenerateMobileNumber(number_length)
HelperFunctions.SaveIndividualAccount(F_name, L_name, email, address, mobile, password)
result = HelperFunctions.IndividualAccountRegistration(F_name, L_name, email, address, mobile, password)
HelperFunctions.SetVerdictIndividual("2. Blank is not allowed", result)

# Test case number 3
F_name = "123"
email = HelperFunctions.GenerateEmail_ID(email_length)
mobile = HelperFunctions.GenerateMobileNumber(number_length)
HelperFunctions.SaveIndividualAccount(F_name, L_name, email, address, mobile, password)
result = HelperFunctions.IndividualAccountRegistration(F_name, L_name, email, address, mobile,password)
HelperFunctions.SetVerdictIndividual("3. Numerics are not allowed", result)

# Test case number 4
F_name = "$%"
email = HelperFunctions.GenerateEmail_ID(email_length)
mobile = HelperFunctions.GenerateMobileNumber(number_length)
HelperFunctions.SaveIndividualAccount(F_name, L_name, email, address, mobile, password)
result = HelperFunctions.IndividualAccountRegistration(F_name, L_name, email, address, mobile, password)
HelperFunctions.SetVerdictIndividual("4. Special characters are not allowed", result)
#---------------------
#END Test cases for "First Name"
#----------------------



#---------------------
#BEGIN Test cases for "Last Name"
#----------------------
F_name = "Test_first_name"
HelperFunctions.BeginTest("Last Name")

# Test case number 5
L_name = " "
email = HelperFunctions.GenerateEmail_ID(email_length)
mobile = HelperFunctions.GenerateMobileNumber(number_length)
HelperFunctions.SaveIndividualAccount(F_name, L_name, email, address, mobile, password)
HelperFunctions.IndividualAccountRegistration(F_name, L_name, email, address, mobile, password)
HelperFunctions.SetVerdictIndividual("5. Space is not allowed", result)

# Test case number 6
L_name = ""
email = HelperFunctions.GenerateEmail_ID(email_length)
mobile = HelperFunctions.GenerateMobileNumber(number_length)
HelperFunctions.SaveIndividualAccount(F_name, L_name, email, address, mobile, password)
result = HelperFunctions.IndividualAccountRegistration(F_name, L_name, email, address, mobile, password)
HelperFunctions.SetVerdictIndividual("6. Blank is not allowed", result)

# Test case number 7
L_name = "123"
email = HelperFunctions.GenerateEmail_ID(email_length)
mobile = HelperFunctions.GenerateMobileNumber(number_length)
HelperFunctions.SaveIndividualAccount(F_name, L_name, email, address, mobile, password)
result = HelperFunctions.IndividualAccountRegistration(F_name, L_name, email, address, mobile, password)
HelperFunctions.SetVerdictIndividual("7. Numerics are not allowed", result)

# Test case number 8
L_name = "$%"
email = HelperFunctions.GenerateEmail_ID(email_length)
mobile = HelperFunctions.GenerateMobileNumber(number_length)
HelperFunctions.SaveIndividualAccount(F_name, L_name, email, address, mobile, password)
result = HelperFunctions.IndividualAccountRegistration(F_name, L_name, email, address, mobile, password)
HelperFunctions.SetVerdictIndividual("8. Special characters are not allowed", result)
#---------------------
#END Test cases for "Last Name"
#----------------------


#---------------------
#BEGIN Test cases for "Email ID"
#----------------------
L_name = "Test_last_name"
HelperFunctions.BeginTest("Email ID")

# Test case number 9
email = ""
mobile = HelperFunctions.GenerateMobileNumber(number_length)
HelperFunctions.SaveIndividualAccount(F_name, L_name, email, address, mobile, password)
HelperFunctions.IndividualAccountRegistration(F_name, L_name, email, address, mobile, password)
HelperFunctions.SetVerdictIndividual("9. Blank is not allowed", result)
#----------------------
#END Test cases for "Email ID"
#----------------------



#---------------------
#BEGIN Test cases for "Date of Birth"
#----------------------
# This Test case should be done manually
#---------------------
#BEGIN Test cases for "Date of Birth"
#----------------------
#



#---------------------
#BEGIN Test cases for "Mobile number"
#----------------------

# Test case number 10
email = HelperFunctions.GenerateEmail_ID(email_length)
#Generate random number of 10 digits with no format
mobile = "".join(random.choice(string.digits) for i in range(10))
HelperFunctions.SaveIndividualAccount(F_name, L_name, email, address, mobile, password)
HelperFunctions.IndividualAccountRegistration(F_name, L_name, email, address, mobile, password)
HelperFunctions.SetVerdictIndividual("10. Only valid mobile numbers are accepted", result)

# Test case number 11
email = HelperFunctions.GenerateEmail_ID(email_length)
mobile = ""
HelperFunctions.SaveIndividualAccount(F_name, L_name, email, address, mobile, password)
HelperFunctions.IndividualAccountRegistration(F_name, L_name, email, address, mobile, password)
HelperFunctions.SetVerdictIndividual("11. Blank is not allowed", result)
#---------------------
#BEGIN Test cases for "Mobile number"
#----------------------



#---------------------
#BEGIN Test cases for "Address"
#----------------------

# Test case number 12
address = ""
email = HelperFunctions.GenerateEmail_ID(email_length)
mobile = HelperFunctions.GenerateMobileNumber(number_length)
HelperFunctions.SaveIndividualAccount(F_name, L_name, email, address, mobile, password)
HelperFunctions.IndividualAccountRegistration(F_name, L_name, email, address, mobile, password)
HelperFunctions.SetVerdictIndividual("12. Blank is not allowed", result)

# Test case number 13
address = " "
email = HelperFunctions.GenerateEmail_ID(email_length)
mobile = HelperFunctions.GenerateMobileNumber(number_length)
HelperFunctions.SaveIndividualAccount(F_name, L_name, email, address, mobile, password)
HelperFunctions.IndividualAccountRegistration(F_name, L_name, email, address, mobile, password)
HelperFunctions.SetVerdictIndividual("13. Space is not allowed", result)
#---------------------
#BEGIN Test cases for "Address"
#----------------------



#---------------------
#BEGIN Test cases for "Password"
#----------------------
# This Test case should be done manually
#---------------------
#BEGIN Test cases for "Password"
#----------------------
#

'''
#--------------------------------------------
#Account login
Button_GetStarted = driver.find_element_by_class_name("btn-get-started");
Button_GetStarted.click()

Field_MobileNumber = driver.find_element_by_id('mob')
Field_MobileNumber.send_keys("9876543210")
Field_Password= driver.find_element_by_id('password')
Field_Password.send_keys("Ashna@1991")

Button_Submit = driver.find_element_by_class_name("btn-primary");
Button_Submit.click()
#---------------------------------------------
'''
