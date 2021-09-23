# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 09:00:56 2021

@author: hrshl
"""

import HelperFunctions
import random
import string


def InstantAccountRegistration():
    prod_OR_uat = "PROD"
    i_OR_b = "I"
    country = "Australia"
    prod_OR_uat = input("Enter environment type (prod or uat)?: ")
    i_OR_b      = input("Which type of account (I or B)?: ")
    country     = input("For which Country?: ")
    if((i_OR_b == "I") or (i_OR_b == "i")):
        #Parameters for individual account
        F_name = "Instant_first_name"
        L_name = "Instant_last_name"
        password = "Hi!12345" 
        address = "Instant address"
        email_length = 4
        
        email = HelperFunctions.GenerateEmail_ID(email_length)
        countryIndex = HelperFunctions.GetCountryIndex(country)
        mobile = HelperFunctions.GenerateMobileNumber(countryIndex)
        Done = HelperFunctions.IndividualAccountRegistration(prod_OR_uat, F_name, L_name, email, 
                                                      address, mobile, password, countryIndex)
        if(Done):
            HelperFunctions.DisplayAllIndividual(F_name, L_name, email, country, address, mobile, password)
            print ("\n======================\n"
                   "Activating the Individual account now! Hold on -- ")
            HelperFunctions.Activate_account(email)
        else:
            print("Unable to register individual account. ERROR.")
        
    elif((i_OR_b == "B") or (i_OR_b == "b")):
        #Parameters for individual account
        F_name = "Instant_first_name"
        L_name = "Instant_last_name"
        password = "Hi!12345" 
        address = "Instant address"
        email_length = 4
        cityname = "InstantCity"
        state = "InstantState"
        zipcode = "".join(random.choice(string.digits) for i in range(5))
        regnum = "".join(random.choice(string.digits) for i in range(5))
        legalname = "fezgdz"
        tradingname = "efje"
        url = HelperFunctions.Generateurl(5)
              
        email = HelperFunctions.GenerateEmail_ID(email_length)
        countryIndex = HelperFunctions.GetCountryIndex(country)
        mobile = HelperFunctions.GenerateMobileNumber(countryIndex)
        bcn = HelperFunctions.GenerateMobileNumber(countryIndex)
        Done = HelperFunctions.BusinessAccountRegistration(prod_OR_uat, countryIndex, cityname, 
                                                    address, state, zipcode, regnum, legalname, 
                                                    tradingname, url, F_name, L_name, email, 
                                                    bcn, mobile, password)
        if(Done):
            HelperFunctions.DisplayAllBusiness(cityname, state, zipcode, regnum, legalname, 
                                           tradingname, url, F_name, L_name, email, bcn, 
                                            mobile, password)
            print ("\n======================\n"
                   "Activating the Business account now! Hold on ---")
            HelperFunctions.Activate_account(email) 
        else:
            print("Unable to register business account. ERROR.")
        
InstantAccountRegistration()





