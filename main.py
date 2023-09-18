from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
import time
from faker import Faker
from datetime import date
import json
import sys
import locators.locators as locators
from testDatas.test_data import admit_patient_test_data_generation


delay = 10 # seconds

# WebDriver
service = Service(executable_path='C:/Users/soorajKS/project1/chromedriver.exe')
options = Options()
options.add_experimental_option("detach", True)
browser = None
browser = webdriver.Chrome(options=options)
browser.maximize_window()
#browser.implicitly_wait(10)
#https://www.ecgvue.site/  http://10.10.5.76/
browser.implicitly_wait(0.5)
browser.get("https://www.ecgvue.site/")

faker=Faker()



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

def find_elements_by_xpath(value) :
    return browser.find_element(By.XPATH,str(value))


# Wait for loading elements
def wait_until_page_load_by_class_name(value):
    try:
        element = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, str(value))))
        #print("Page is Ready")
    except:
        print("Loading took too much time!")

def wait_until_page_load_by_id(value):
    try:
        element = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, str(value))))
        #print("Page is Ready")
    except:
        print("Loading took too much time!")

def wait_until_page_load_by_xpath(value):
    try:
        element = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, str(value))))
        #print("Page is Ready")
    except:
        print("Loading took too much time!")


# Clear previous texts in teaxt fields
def input_clear_funct(element):
    element.clear()


# Select value from selection element
def select_value_funct(elements,text_vale):
    length=len(elements)
    for i in range(0,length):
        value=elements[i].text
        if(str(value) == str(text_vale)):
            return elements[i]

# country selection function
def country_select_value_funct(elements,text_vale):
    length=len(elements)
    for i in range(0,length):
        value=elements[i].text
        value=value[:-5]
        if(str(value) == str(text_vale)):
            return elements[i]

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

# Admit patient mandatory field
admit_patient_mandatory_field_dict={

    'patient_demography':{
        'patientID':0,
        'firstName':1,
        'lastName':2,
 #       'dateOfBirth':3,
 #       'sex':0,
        },

    'patient_contact':{
        'PRIMARY_CONTACT_NUMBER':0,
        'COUNTRY':0,
        'ZIP_CODE':2,
        'STATE':5,
        'CITY':6,
    },

    'provider_info':{
        'PRESCIBING_PHYSICIAN':0,
        'REFERAL_PHYSICIAN':1,
        'INTERPRETING_PHYSICIAN':2,
        'TECHNICIAN':4,
    },

    'procedure_info':{
        'PRECRIPTION_ID':0,
        'PROCEDURE_DURATION':0,
        'LOCATION_GROUP':1
    }

}


# Patient Demographics
def patient_demographic_funct(demography_data,locator):
        

    wait_until_page_load_by_class_name('mat-button')

    #time.sleep(.1)


    elements=find_elements_by_class_name('mat-input-element')

    #time.sleep(.1)
    #  Patient ID
    try:
        element=find_element_by_name(str(locator['patient_id']))
        input_clear_funct(element)
        element.send_keys(str(demography_data['patientID']))

    except Exception as ex:
        print("Error from patient ID",str(ex)) 

    time.sleep(.1)
    # First name
    try:
        element=find_element_by_name(str(locator['first_name']))
        input_clear_funct(element)
        element.send_keys(str(demography_data['firstName']))
    except Exception as ex:
        print("Error from first name",str(ex)) 
    
    #time.sleep(.1)
    # Last name
    try:
        element=find_element_by_name(str(locator['last_name']))
        input_clear_funct(element)
        element.send_keys(str(demography_data['lastName']))
    except Exception as ex:
        print("Error from last name",str(ex)) 

    #time.sleep(.1)
    # Date of birth
    try:
        element=find_element_by_name(str(locator['date_of_birth']))
        element.send_keys(str(demography_data['dateOfBirth']))
    except Exception as ex:
        print("Error from date of birth",str(ex)) 

    #time.sleep(.1)
    # Weight
    try:
        element=find_element_by_name(str(locator['weight']))
        input_clear_funct(element)
        element.send_keys(int(demography_data['weight']))
    except Exception as ex:
        print("Error from weight",str(ex)) 

    #time.sleep(.1)
    # Height
    try:
        element=find_element_by_name(str(locator['height']))
        input_clear_funct(element)
        element.send_keys(int(demography_data['height']))
    except Exception as ex:
        print("Error from height",str(ex)) 

    #time.sleep(.1)
    # Sex
    try:
        element=find_element_by_class_name('mat-select-value')
        element.click()
        time.sleep(.1)
        wait_until_page_load_by_class_name('mat-option-text')
        #element=find_element_by_class_name('mat-option-text')
        element=select_value_funct(find_elements_by_class_name('mat-option-text'),str(demography_data['sex']))
        element.click() 
    except Exception as ex:
        print("Error from sex",str(ex)) 

        
        # Button
        """ wait_until_page_load_by_class_name('mat-flat-button')
        elements=find_elements_by_class_name('mat-flat-button')
        elements[1].click() """
    time.sleep(1)

# Patient contact
def patient_contact_funct(patient_contact_data,locator):

    #wait_until_page_load_by_id('mat-error')

    #time.sleep(.5)


    elements=find_elements_by_class_name('mat-input-element')

    #time.sleep(.5)
    # Primary contact number
    try:
        element=find_element_by_xpath(str(locator['primary_contact_number']))
        input_clear_funct(element)
        element.send_keys(int(patient_contact_data['primaryContactNo']))
    except Exception as ex:
        print("Error from primary contact number",str(ex)) 

    #time.sleep(.5)
    # Email ID
    try:
        element=find_element_by_name(str(locator['email_id']))
        input_clear_funct(element)
        element.send_keys(str(patient_contact_data['emailID']))
    except Exception as ex:
        print("Error from email ID",str(ex)) 

    #time.sleep(.1)
    # Country
    try:
        element=find_element_by_name(str(locator['country']))
        input_clear_funct(element)
        element.send_keys(str(patient_contact_data['country']))
        wait_until_page_load_by_class_name('mat-option-text')
    
        find_element_by_class_name('mat-option-text').click()
    except Exception as ex:
        print("Error from country",str(ex)) 

    #time.sleep(.1)
    # Zip code
    try:
        element=find_element_by_name(str(locator['zip_code']))
        input_clear_funct(element)
        element.send_keys(int(patient_contact_data['zipCode']))
    except Exception as ex:
        print("Error from zip code",str(ex)) 

    #time.sleep(.1)
    # Street adress1
    try:
        element=find_element_by_name(str(locator['street_adress_1']))
        input_clear_funct(element)
        element.send_keys(str(patient_contact_data['streetAdress1']))
    except Exception as ex:
        print("Error from street adress 1",str(ex)) 

    #time.sleep(.1)
    # Street adress2
    try:
        element=find_element_by_name(str(locator['street_adress_2']))
        input_clear_funct(element)
        element.send_keys(str(patient_contact_data['streetAdress2']))
    except Exception as ex:
        print("Error from street adress 2",str(ex)) 

    #time.sleep(.1)
    # State
    try:
        element=find_element_by_name(str(locator['state']))
        element.send_keys(str(patient_contact_data['state']))
    except Exception as ex:
        print("Error from state",str(ex)) 

    #time.sleep(1)

    #time.sleep(.1)
    # City
    try:
        element=find_element_by_name(str(locator['city']))
        element.send_keys(str(patient_contact_data['city']))
    except Exception as ex:
        print("Error from city",str(ex)) 

    #time.sleep(.1)
    # Emergency contact name
    try:
        element=find_element_by_name(str(locator['emergency_contact_name']))
        input_clear_funct(element)
        element.send_keys(str(patient_contact_data['emergencyContactName']))
    except Exception as ex:
        print("Error from emergency contact name",str(ex)) 

    #time.sleep(.1)
    # Emergency contact number
    try:
        element=find_element_by_xpath(str(locator['emergency_contact_number']))
        input_clear_funct(element)
        element.send_keys(int(patient_contact_data['emergencyContactNo']))
    except Exception as ex:
        print("Error from emergency contact number",str(ex)) 
    


        """ element=find_element_by_class_name('mat-select-value')
        element.click()
        wait_until_page_load_by_class_name('mat-option-text')
        #element=find_element_by_class_name('mat-option-text')
        element=country_select_value_funct(find_elements_by_class_name('mat-option-text'),str(patient_contact_data['country']))
        element.click() """

        # Button
        """ wait_until_page_load_by_class_name('mat-flat-button')
        elements=find_elements_by_class_name('mat-flat-button')
        elements[1].click()
 """


# Provider info function
def provider_info_funct(provider_info_data,locator):
    time.sleep(.5)

    elements=find_elements_by_class_name('mat-select-value')

    # Prescribing Physician
    try:
        element=find_element_by_xpath(str(locator['prescribing_physician']))
        element.click()
        wait_until_page_load_by_class_name('mat-option-text')
        time.sleep(.5)
        #print(str(find_element_by_class_name('mat-option-text').text))
        element=select_value_funct(find_elements_by_class_name('mat-option-text'),str(provider_info_data['prescribingPhysician']))
        element.click()
    except Exception as ex:
        print("Error from prescribing physician",str(ex)) 

    # Referal Physician
    """  try:
        wait_until_page_load_by_class_name('mat-select-value')
        element=find_element_by_xpath(str(locator['referal_physician']))
        element.click()
        time.sleep(0.1)
        wait_until_page_load_by_class_name('mat-option-text')
        element=select_value_funct(find_elements_by_class_name('mat-option-text'),str(provider_info_data['referalPhysician']))
        element.click()
    except Exception as ex:
        print("Error from referal physician",str(ex)) """ 
          

    # Interpreting Physician
    try:
        wait_until_page_load_by_class_name('mat-select-value')
        element=find_element_by_xpath(str(locator['interpreting_physycian']))
        element.click()
        time.sleep(0.5)
        wait_until_page_load_by_class_name('mat-option-text')
        element=select_value_funct(find_elements_by_class_name('mat-option-text'),str(provider_info_data['interpretingPhysician']))
        element.click()
    except Exception as ex:
        print("Error from interpreting physician",str(ex)) 

    # Preliminary Interpreting Physician
    try:
        wait_until_page_load_by_class_name('mat-select-value')
        element=find_element_by_xpath(str(locator['preliminary_interpreting_physician']))
        element.click()
        time.sleep(.5)
        wait_until_page_load_by_class_name('mat-option-text')
        element=select_value_funct(find_elements_by_class_name('mat-option-text'),str(provider_info_data['preliminaryInterpretingPhysician']))
        element.click()
    except Exception as ex:
        print("Error from preliminary interpreting pysician",str(ex)) 

    # Technician
    try:
        wait_until_page_load_by_class_name('mat-select-value')
        element=find_element_by_xpath(str(locator['technician']))
        element.click()
        time.sleep(0.5)
        wait_until_page_load_by_class_name('mat-option-text')
        element=select_value_funct(find_elements_by_class_name('mat-option-text'),str(provider_info_data['technician']))
        element.click()
    except Exception as ex:
        print("Error from technician",str(ex)) 

        wait_until_page_load_by_class_name('mat-select-value')

        # Button
        """ elements=find_elements_by_class_name('mat-flat-button')
        elements[1].click() """


# Procedure info function
def procedure_info_funct(procedure_info_data,locator):

    elements=find_elements_by_class_name('mat-input-element')

    time.sleep(.5)

    # Prescription ID
    try:
        element=find_element_by_name(str(locator['prescription_id']))
        element.send_keys(str(procedure_info_data['prescriptionID']))
    except Exception as ex:
        print("Error from prescribing ID",str(ex)) 

    # Order ID
    try:
        element=find_element_by_name(str(locator['order_id']))
        element.send_keys(str(procedure_info_data['orderID']))
    except Exception as ex:
        print("Error from order ID",str(ex)) 

    # Primary Clinical Indication
    try:
        element=find_element_by_name(str(locator['primary_clinical_indicaton']))
        element.send_keys(str(procedure_info_data['primaryClinicalIndication']))
    except Exception as ex:
        print("Error from primary clinical indication",str(ex)) 


    elements=find_elements_by_class_name('mat-select-value')

    # Procedure Duration
    try:
        wait_until_page_load_by_class_name('mat-select-value')
        element=find_element_by_xpath(str(locator['procedure_duration']))
        browser.implicitly_wait(50)
        element.click()
        time.sleep(.5)
        wait_until_page_load_by_class_name('mat-option-text')
        element=select_value_funct(find_elements_by_class_name('mat-option-text'),str(procedure_info_data['procedureDuration']))
        element.click()
    except Exception as ex:
        print("Error from procedure duration",str(ex)) 

        # Location Group

        """  wait_until_page_load_by_class_name('mat-select-value')
        browser.implicitly_wait(50)
        elements[1].click()
        time.sleep(.1)
        wait_until_page_load_by_class_name('mat-option-text')
        element=select_value_funct(find_elements_by_class_name('mat-option-text'),str(procedure_info_data['locationGroup']))
        element.click() """

    try:
        wait_until_page_load_by_class_name('w100')
        element=find_element_by_xpath(str(locator['location_group']))
        element.click()
        time.sleep(.5)
        wait_until_page_load_by_class_name('nested-menu-item')
        #element_=select_value_funct(find_elements_by_class_name('mat-option-text'),str(procedure_info_data['locationGroup']))
        element=find_element_by_class_name('nested-menu-item')
        element.click()

        # Button
        """ elements=find_elements_by_class_name('mat-flat-button')
        elements[2].click() """

    except Exception as ex:
        print('Error from location group : ',str(ex))

    #time.sleep(2)

    # Biosensor ID
    """ try:
        element=find_element_by_name(str(locator['biosensor_id']))
        element.send_keys(str(procedure_info_data['biosensorID']))
        time.sleep(.1)
        browser.find_element(By.CLASS_NAME,"mat-option-text").click()
    except Exception as ex:
        print("Error from biosensor ID",str(ex)) """ 


    """ try:
        element = browser.find_element(By.NAME,'biosensor_start_date').click()
        time.sleep(.5)
        browser.find_element(By.XPATH,'/html/body/div[2]/div[4]/div/owl-date-time-container/div[2]/div/button[2]').click()
    except:
        print()
 """

# Additional info function
def additional_info_funct(additional_info_data,locator):
    time.sleep(.5)
    try:
        # Aditional information

        #wait_until_page_load_by_class_name('mat-checkbox-input')

        element=find_element_by_name(str(locator['additional_information']))

        input_clear_funct(element)

        element.send_keys(str(additional_info_data['additionalInformation']))

        #elements=find_elements_by_name('mat-checkbox-input')

        # Pacemaker
        try:
            element=find_element_by_xpath(str(locator['pacemaker']))
            if(str(additional_info_data['pacemaker'])=='True'):
                element.click()
        except Exception as ex:
            print('error from pacemaker',str(ex))

        # ICD
        try:
            element=find_element_by_xpath(str(locator['icd']))
            if(str(additional_info_data['icd'])=='True'):
                element.click()
        except Exception as ex:
            print('error from icdr',str(ex))

        # Button
        """ elements=find_elements_by_class_name('mat-flat-button')
        elements[1].click() """

    except Exception as ex:
        print('Message from additional info : ',str(ex))


# Billing info function
def billing_info_funct(billing_info_data,locator):

    time.sleep(.5)
        
    elements=find_elements_by_class_name('mat-select-value')

    # Billing indication
    try:
        wait_until_page_load_by_class_name('mat-select-value')
        elements[0].click()
        time.sleep(.15)
        wait_until_page_load_by_class_name('mat-option-text')
        element=select_value_funct(find_elements_by_class_name('mat-option-text'),str(billing_info_data['billingIndication']))
        element.click()
    except Exception as ex:
        print("Error from billing indication",str(ex)) 

    # Billing method
    try:
        wait_until_page_load_by_class_name('mat-select-value')
        elements[1].click()
        time.sleep(0.15)
        wait_until_page_load_by_class_name('mat-option-text')
        element=select_value_funct(find_elements_by_class_name('mat-option-text'),str(billing_info_data['billingMethod']))
        element.click()
    except Exception as ex:
        print("Error from billing method",str(ex)) 

        # Button
        """ elements=find_elements_by_class_name('mat-flat-button')
        elements[1].click() """



def admit_patient_save_button_click():
    try:
        wait_until_page_load_by_class_name('mat-flat-button')
        elements=find_elements_by_class_name('mat-flat-button')
        elements[1].click()
    except Exception as ex:
        print("Error from save button",str(ex)) 

data=None

def admit_patient_verify_funct():
    
    try:
        element=find_element_by_id('searchString')
        element.send_keys(str(data['procedure_info']['prescriptionID']))
    except Exception as ex:
        print("error from search",str(ex))

    try:
        time.sleep(1)
        elements=find_elements_by_class_name('me-2')
        result = 0
        for i in elements:
            if(i.text==data["procedure_info"]["prescriptionID"]):
                result=result+1
        print()
        if(result==1):
            print('summary page : registration successfull')
        elif(result>1):
            print('summary page : duplicate datas')
        elif(result==0):
            print('summary page : registration failed')
    except Exception as ex:
        print('error from search list results',str(ex))


browser.implicitly_wait(2)

def isElementVisible(locator):
    if (browser.find_element(*locator).is_displayed()):
        return True
    return False

def pateient_registration_successfull_popup_funct():
    try:
        #print(browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/mat-dialog-container/app-patient-admitted-modal/div/button'))
        #if (browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/mat-dialog-container/app-patient-admitted-modal/div/button').is_displayed()):
        t=(By.XPATH,'/html/body/div[2]/div[2]/div/mat-dialog-container/app-patient-admitted-modal/div/button')
        if(isElementVisible(t)):
            print("patient registration passed")
            find_element_by_xpath('/html/body/div[2]/div[2]/div/mat-dialog-container/app-patient-admitted-modal/div/button').click()
            return True 
        
        print('patient registration failed')
        find_element_by_xpath('/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[4]/button').click()
        return False
    except Exception:
        print("inside exception Registration failed")
        find_element_by_xpath('/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[4]/button').click()
        return False

# New patient registration function 
def new_patient_registration_funct(patient_register_dict,locator):
    try:
        patient_demographic_funct(patient_register_dict['patient_demography'],locator['patient_demographics'])
        admit_patient_save_button_click()
        patient_contact_funct(patient_register_dict['patient_contact'],locator['patient_contact'])
        admit_patient_save_button_click()
        provider_info_funct(patient_register_dict['provider_info'],locator['provider_info'])
        admit_patient_save_button_click()
        procedure_info_funct(patient_register_dict['procedure_info'],locator['procedure_info'])
        wait_until_page_load_by_class_name('mat-flat-button')
        elements=find_elements_by_class_name('mat-flat-button')
        elements[2].click()
        additional_info_funct(patient_register_dict['additional_info'],locator['additional_info'])
        admit_patient_save_button_click()
        billing_info_funct(patient_register_dict['billing_info'],locator['billing_info'])
        admit_patient_save_button_click() 
    except Exception as ex:
        print(str(ex))

# Test case 
""" def patient_admited_popup_message(test_case):
    try:
        time.sleep(.1)
        element=find_element_by_class_name('mb-0')
        text_value=element.text

        if(str(test_case)=='good'):
            if(str(text_value)=="Patient Admitted"):
                print("[+]Test passed : Patient admitted")
                find_element_by_class_name('mat-flat-button').click()
            else:
                print("[!]Test not passed : Patient not admitted")
        else:
            if(str(text_value)=="Patient Admitted"):
                print("[!]Test not passed : Patient admitted")
                find_element_by_class_name('mat-flat-button').click()
            else:
                print("[+]Test passed : Patient not admitted")
    except NoSuchElementException as ex:
        if(str(test_case)=='bad'):
            print("[+]Test passed : Patient not admitted")
        else:
            print("[!]Test failed : Patient not admitted")
            find_element_by_class_name('mat-flat-button').click() """


# Admit patient Mandatory field checking
def patient_admit_mandatory_field_checking():

    pateint_demographics_mandatory_field_funct(admit_patient_mandatory_field_dict['patient_demography'])
    """ patient_contact_mandatory_field_funct(admit_patient_mandatory_field_dict['patient_contact'])
    provider_info_mandatory_field_funct(admit_patient_mandatory_field_dict['procedure_info'])
    procedure_info_mandatory_field_funct(admit_patient_mandatory_field_dict['provider_info']) """




def pateint_demographics_mandatory_field_funct(demography_data):

    find_elements_by_class_name('mat-button')[0].click()

    time.sleep(.5)
    new_dict=patient_register_dict['patient_demographics']

    for i in demography_data:
        new_dict[i]="."
        patient_demographic_funct(new_dict)
        time.sleep(1)
        save_button_isEnabled_or_not()
        time.sleep(1)
        find_elements_by_class_name('mat-button')[5].click()
        time.sleep(1)
        save_button_isEnabled_or_not()
        admit_patient_save_button_click()
        print('save button clicked')
        time.sleep(1)
        print('mat error',find_element_by_class_name('mat-error').is_enabled())

        new_dict[i]='sssss'
        print(new_dict[i])





def patient_contact_mandatory_field_funct():
    print
def provider_info_mandatory_field_funct():
    print
def procedure_info_mandatory_field_funct():
    print



def save_button_isEnabled_or_not():
    element=find_elements_by_class_name('mat-flat-button')
    time.sleep(.1)
    try:
        print(element[1].is_enabled())
    except WebDriverException:
        print ("Element is not clickable")



def current_patient_search_fields():

    current_patient_location_search()
    current_patient_prescribing_physician()
    current_patient_monitoring_duration()
    current_patient_status()

def current_patient_location_search(locator):
    
    element=find_element_by_name(str())
    element.send_keys(str())

def current_patient_prescribing_physician():
    
    element=find_element_by_name(str())
    element.send_keys(str())

def current_patient_monitoring_duration():
    
    element=find_element_by_name(str())
    element.send_keys(str())

def current_patient_status():
    
    element=find_element_by_name(str())
    element.send_keys(str())
    


#patient_register_dict = json.load(sys.argv[1])
patient_register_dict=None
with open('patient_register.json') as json_file:
    patient_register_dict = json.load(json_file)



print(admit_patient_test_data_generation())
login_funct("deepak@probeplus.in","ecg123")
wait_until_page_load_by_class_name("app-card")
#find_element_by_class_name('registerBtn-in-card').click()
#wait_until_page_load_by_id('mat-dialog-0')
for i in range(0,100000):
    data=admit_patient_test_data_generation()
    print(data)
    #print(locators.locators['admit_patient'])
    wait_until_page_load_by_class_name("app-card")
    find_element_by_class_name('registerBtn-in-card').click()
    wait_until_page_load_by_id('mat-dialog-0')
    new_patient_registration_funct(data,locators.locators['admit_patient'])
    time.sleep(.5)
    """ pateient_registration_successfull_popup_funct()
    #find_element_by_xpath('/html/body/app-root/app-root/app-header/mat-toolbar/div[2]/app-navigation/span/span[1]/a').click()
    time.sleep(.5)
    wait_until_page_load_by_xpath('/html/body/app-root/app-root/app-summary/div/div/div[1]/app-setting-card[3]/div/div[1]/div[3]/a')
    time.sleep(.2)
    find_element_by_xpath('/html/body/app-root/app-root/app-summary/div/div/div[1]/app-setting-card[3]/div/div[1]/div[3]/a').click()
    time.sleep(.2)
    admit_patient_verify_funct()
    find_element_by_xpath('/html/body/app-root/app-root/app-header/mat-toolbar/div[2]/app-navigation/span/span[1]/a').click()
    time.sleep(1) """
    browser.refresh()
    time.sleep(2)

#patient_admited_popup_message('good')
#browser.back()

#time.sleep(30)

#patient_admit_mandatory_field_checking()


#print(admit_patient_test_data_generation())

#print(locators)




