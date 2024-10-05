## This file contains all the imports with the functions that are used in the main file
#imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

## --------------------------------- General Functions --------------------------------- ##

def start_driver():
    #Start the driver
    service=Service("chromedriver.exe")
    driver=webdriver.Chrome(service=service)
    return driver

def open_page(driver,url):
    #Open the page and waits untill fully loaded
    driver.get(url)

    return driver

def wait(driver,timeout=10):
    #Wait for the page to be loaded given time out
    try:
        WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.TAG_NAME,"body")))
    except:
        print("Timeout While Loading the Page")



## --------------------------------- Specific Functions For Scraping --------------------------------- ##
def property_name(driver):
    pass

def property_price(driver):
    pass

def property_location(driver):
    pass

def property_area(driver):
    pass

def property_purpose(driver):
    pass

def property_bedrooms(driver):
    pass

def property_bathrooms(driver):
    pass

def property_added_time(driver):
    pass

def property_description(driver):
    pass

def property_estate_agent_name(driver):
    pass

def property_estate_agent_number(driver):
    pass

def home_finance_monthly_payment(driver):
    pass

def bank_finance_amount(driver):
    pass

def property_id(driver):
    pass

def property_amenities(driver):
    pass

## --------------------------------- Functions for navigation --------------------------------- ##
def change_property_purpose(driver,purpose):
    pass

def change_property_location(driver,location):
    pass

def change_property_type(driver,property_type):
    pass

def change_property_area(driver,area):
    pass

def change_property_price(driver,max,min):
    pass

def change_property_bedrooms(driver,bedrooms):
    pass

def change_property_bathrooms(driver,bathrooms):
    pass

def change_more_options(driver):
    pass

def change_city(driver,city):
    pass

def get_locations_list_city_wise(driver):
    pass

## --------------------------------- Functions for Agent finder Features --------------------------------- ##
def change_agent_property_type(driver,property_type):
    pass

def change_agent_city(driver,city):
    pass

def get_agent_name(driver):
    pass

def get_agent_location(driver):
    pass

def get_agent_properties_listed_for_sale(driver):
    pass

def get_agent_properties_listed_for_rent(driver):
    pass

def get_agent_ranking(driver):
    pass

def get_agency_staff_names(driver):
    pass

def get_agency_staff_numbers(driver):
    pass

def get_agency_description(driver):
    pass

def get_agency_properties_types(driver):
    pass

def get_agency_properties_links(driver):
    pass

def get_titanium_agencies(driver):
    pass

def get_featured_agencies(driver):
    pass

def get_agencies_by_city(driver):
    pass

def  browse_agency_page(driver):
    #In This Function we would browse the agency page 
    #and get all the information about agencies
    pass