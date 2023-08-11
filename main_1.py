from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date
import json
import sys


delay = 10 # seconds

# WebDriver
service = Service(executable_path='C:/Users/soorajKS/project1/chromedriver.exe')
browser = webdriver.Chrome()
browser.maximize_window()
#https://www.ecgvue.site/#/active-patients
browser.get("http://10.10.5.76/")



# Locator single element
def find_element_by_id(value):
    return browser.find_element(By.ID, str(value))

def find_element_by_class_name(value):
    return browser.find_element(By.CLASS_NAME, str(value))
       
def find_element_by_name(value) :
    return browser.find_element(By.NAME,str(value))

def find_element_by_link_text(value) :
    return browser.find_element(By.LINK_TEXT,str(value))

def find_element_by_partial_link_text(value) :
    return browser.find_element(By.PARTIAL_LINK_TEXT,str(value))

def find_element_by_tag_name(value) :
    return browser.find_element(By.TAG_NAME,str(value))

def find_element_by_css_selector(value) :
    return browser.find_element(By.CSS_SELECTOR,str(value))

def find_element_by_xpath(value) :
    return browser.find_element(By.XPATH,str(value))


# Locator iterable elements
def find_elements_by_id(id):
    return browser.find_elements(By.ID, str(id))

def find_elements_by_class_name(name):
    return browser.find_elements(By.CLASS_NAME, str(name))
       
def find_elements_by_name(value) :
    return browser.find_elements(By.NAME,str(value))
    
def find_elements_by_link_text(value) :
    return browser.find_elements(By.LINK_TEXT,str(value))

def find_elements_by_partial_link_text(value) :
    return browser.find_elements(By.PARTIAL_LINK_TEXT,str(value))

def find_elements_by_tag_name(value) :
    return browser.find_elements(By.TAG_NAME,str(value))

def find_elements_by_css_selector(value) :
    return browser.find_elements(By.CSS_SELECTOR,str(value))

def find_element_by_xpath(value) :
    return browser.find_element(By.XPATH,str(value))


# Wait for loading elements
def wait_until_page_load_by_class_name(value):
    try:
        element = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, str(value))))
        print("Page is Ready")
    except:
        print("Loading took too much time!")

def wait_until_page_load_by_id(value):
    try:
        element = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, str(value))))
        print("Page is Ready")
    except:
        print("Loading took too much time!")

def wait_until_page_load_by_xpath(value):
    try:
        element = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, str(value))))
        print("Page is Ready")
    except:
        print("Loading took too much time!")


def input_clear_funct(element):
    element.clear()

def wait_until(value):
    try:
        element = WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.CLASS_NAME, str(value))))
        print("Page is Ready")
    except:
        print("Loading took too much time!")


# Login function
def login_funct(_username,_password):
    try:
        username = find_element_by_id("username") 
        input_clear_funct(username)
        username.send_keys(str(_username))
        password = find_element_by_id("password") 
        input_clear_funct(password)
        password.send_keys(str(_password))
        print("username : ",_username)
        print("password : ",_password)
        find_element_by_id("kc-login").click()
    except Exception as ex:
        print(str(ex))

def patient_contact_funct(patient_contact_data):
    try:
        #wait_until_page_load_by_id('mat-error')

        elements=find_elements_by_class_name('mat-input-element')

        browser.implicitly_wait(50)

        print(elements[0])
        #for i in range(0,9):
        #    input_clear_funct(elements[i])

        #wait_until(elements[0].id)
        
        # Primary contact number
        element=browser.find_element(By.CLASS_NAME,"mat-input-element")
        elements[0].send_keys(int(patient_contact_data['primaryContactNo']))

        # Email ID
        elements[1].send_keys(str(patient_contact_data['emailID']))

        # Zip code
        elements[2].send_keys(int(patient_contact_data['zipCode']))

        # Street adress1
        elements[3].send_keys(str(patient_contact_data['streetAdress1']))

        # Street adress2
        elements[4].send_keys(str(patient_contact_data['streetAdress2']))

        # State
        elements[5].send_keys(str(patient_contact_data['state']))

        # City
        elements[6].send_keys(str(patient_contact_data['city']))

        # Emergency contact name
        elements[7].send_keys(str(patient_contact_data['emergencyContactName']))

        # Emergency contact number
        elements[8].send_keys(int(patient_contact_data['emergencyContactNo']))


        element=find_element_by_class_name('mat-select-value')
        element.click()
        wait_until_page_load_by_class_name('mat-option-text')
        element=find_element_by_class_name('mat-option-text')
        element.click()

        # Button
        wait_until_page_load_by_class_name('mat-flat-button')
        elements=find_elements_by_class_name('mat-flat-button')
        elements[1].click()

    except Exception as ex:
        print("Error from patient contact",str(ex))  
        elements=find_elements_by_class_name('mat-flat-button')
        elements[1].click()

# Provider info function
def provider_info_funct(provider_info_data):
    try:

        elements=find_elements_by_class_name('mat-select-value')

        # Prescribing Physician
        elements[0].click()
        wait_until_page_load_by_class_name('mat-option-text')
        elements[0]=find_element_by_class_name('mat-option-text')
        elements[0].click()

        # Referal Physician
        wait_until_page_load_by_class_name('mat-select-value')
        elements[1].click()
        time.sleep(.2)
        wait_until_page_load_by_class_name('mat-option-text')
        element=find_element_by_class_name('mat-option-text')
        element.click()
          

        # Interpreting Physician
        wait_until_page_load_by_class_name('mat-select-value')
        elements[2].click()
        time.sleep(.2)
        wait_until_page_load_by_class_name('mat-option-text')
        element=find_element_by_class_name('mat-option-text')
        element.click()

        # Preliminary Interpreting Physician
        wait_until_page_load_by_class_name('mat-select-value')
        elements[3].click()
        time.sleep(0.2)
        wait_until_page_load_by_class_name('mat-option-text')
        element=find_element_by_class_name('mat-option-text')
        element.click()

        # Technician
        wait_until_page_load_by_class_name('mat-select-value')
        elements[4].click()
        time.sleep(0.2)
        wait_until_page_load_by_class_name('mat-option-text')
        element=find_element_by_class_name('mat-option-text')
        element.click()

        wait_until_page_load_by_class_name('mat-select-value')

        # Button
        elements=find_elements_by_class_name('mat-flat-button')
        elements[1].click()

    except Exception as ex:
        print('Error from provider : ',str(ex))




# New patient registration function 
def new_patient_registration_funct(patient_register_dict):
    try:

        #patient_demographic_funct(patient_register_dict['patient_demography'])
        #patient_contact_funct(patient_register_dict['patient_contact'])
        provider_info_funct(patient_register_dict['provider_info'])
        #procedure_info_funct(patient_register_dict['procedure_info'])
        #additional_info_funct(patient_register_dict['additional_info'])
        #billing_info_funct(patient_register_dict['billing_info'])
    except Exception as ex:
        print(str(ex))



#patient_register_dict = json.load(sys.argv[1])
patient_register_dict=None
with open('patient_register.json') as json_file:
    patient_register_dict = json.load(json_file)
print("Type:", type(patient_register_dict))

login_funct("deepak@probeplus.in","deepak123")
wait_until_page_load_by_class_name("app-card")
find_element_by_class_name('registerBtn-in-card').click()
wait_until_page_load_by_id('mat-dialog-0')
_elements=find_elements_by_class_name('btn')
_elements[2].click()
new_patient_registration_funct(patient_register_dict)


time.sleep(20)