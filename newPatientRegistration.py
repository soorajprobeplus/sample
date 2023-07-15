from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date


delay = 10 # seconds

# WebDriver
service = Service(executable_path='C:/Users/soorajKS/project1/chromedriver.exe')
browser = webdriver.Chrome(service=service)
browser.maximize_window()
#https://www.ecgvue.site/#/active-patients
browser.get("http://www.ecgvue.site/")


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


# Login function
def login_funct(username,password):
    try:
        uname = find_element_by_id("username") 
        uname.clear()
        uname.send_keys(str(username))
        pword = find_element_by_id("password") 
        pword.clear()
        pword.send_keys(str(password))
        print("username : ",username)
        print("password : ",password)
        find_element_by_id("kc-login").click()
    except Exception as ex:
        print(str(ex))

    error_message = "Invalid username or password."
    # Retrieve any errors found. 
    errors = ""
    errors = find_elements_by_id("input-error")

    # When errors are found, the login will fail. 
    if any(error_message in e.text for e in errors): 
        print("[!] Login failed")
    else:
        print("[+] Login successful")
    wait_until_page_load_by_class_name("app-card")

    get_url = browser.current_url
    print('current page url : ',get_url)
    if(get_url=="https://www.ecgvue.site/#/summary"):
        print("[+] successfully redirect to next page")
    else:
        print("[!] unsuccessfully redirect to next page")


# Patient Demographics
def patient_demographic_funct(patientID,
                              firstName,lastName,
                              dateOfBirth,
                              age,
                              sex,
                              weight,
                              height
                              ):
    try:
        wait_until_page_load_by_class_name('mat-button')

        elements=find_elements_by_class_name('mat-input-element')

        #  Patient ID
        elements[0].clear
        elements[0].send_keys(str(patientID))

        # First name
        elements[1].clear
        elements[1].send_keys(str(firstName))

        # Last name
        elements[2].clear
        elements[2].send_keys(str(lastName))

        # Date of birth
        elements[3].clear
        elements[3].send_keys(str(dateOfBirth))

        # Weight
        elements[5].clear
        elements[5].send_keys(int(weight))

        # Height
        elements[6].clear
        elements[6].send_keys(int(height))

        # Sex
        element=find_element_by_class_name('mat-select-value')
        element.click()
        element=find_element_by_class_name('mat-option-text')
        element.click() 

        # Button
        element=find_element_by_class_name('mat-flat-button')
        element.click()

    except Exception as ex:
        print(str(ex))

# Patient contact
def patient_contact_funct(primaryContactNo,
                          emailID,
                          country,
                          zipCode,
                          streetAdress1,
                          streetAdress2,
                          state,
                          city,
                          emergencyContactName,
                          emergencyContactNo
                          ):
    try:
        wait_until_page_load_by_class_name('mat-button')

        elements=find_elements_by_class_name('mat-input-element')

        # Primary contact number
        elements[0].clear()
        elements[0].send_keys(int(primaryContactNo))

        # Email ID
        elements[1].clear()
        elements[1].send_keys(str(emailID))

        # Zip code
        elements[2].clear()
        elements[2].send_keys(int(zipCode))

        # Street adress1
        elements[3].clear()
        elements[3].send_keys(str(streetAdress1))

        # Street adress2
        elements[4].clear()
        elements[4].send_keys(str(streetAdress2))

        # State
        elements[5].clear()
        elements[5].send_keys(str(state))

        # City
        elements[6].clear()
        elements[6].send_keys(str(city))

        # Emergency contact name
        elements[7].clear()
        elements[7].send_keys(str(emergencyContactName))

        # Emergency contact number
        elements[8].clear()
        elements[8].send_keys(int(emergencyContactNo))

        element=find_element_by_class_name('mat-select-value')
        element.click()
        element=find_element_by_class_name('mat-option-text')
        element.click()

         # Button
        element=find_element_by_class_name('mat-flat-button')
        element.click()

    except Exception as ex:
        print(str(ex))  


# Provider info function
def provider_info_funct(prescribingPhysician,
                        referalPhysician,
                        interpretingPhysician,
                        preliminaryInterpretingPhysician,
                        technician
                        ):
    try:
        elements=find_elements_by_class_name('mat-select-value')

        # Prescribing Physician
        browser.implicitly_wait(50)
        elements[0].clear
        elements[0].click()
        wait_until_page_load_by_class_name('mat-option-text')
        element=find_element_by_class_name('mat-option-text')
        element.click()

        # Referal Physician
        wait_until_page_load_by_class_name('mat-select')
        browser.implicitly_wait(50)
        elements[1].clear
        elements[1].click()
        wait_until_page_load_by_class_name('mat-option-text')
        element=find_element_by_class_name('mat-option-text')
        element.click()

        # Interpreting Physician
        wait_until_page_load_by_class_name('mat-select')
        browser.implicitly_wait(50)
        elements[2].clear
        elements[2].click()
        wait_until_page_load_by_class_name('mat-option-text')
        element=find_element_by_class_name('mat-option-text')
        element.click()

        # Preliminary Interpreting Physician
        wait_until_page_load_by_class_name('mat-select')
        browser.implicitly_wait(50)
        elements[3].clear
        elements[3].click()
        wait_until_page_load_by_class_name('mat-option-text')
        element=find_element_by_class_name('mat-option-text')
        element.click()

        # Technician
        wait_until_page_load_by_class_name('mat-select')
        browser.implicitly_wait(50)
        elements[4].clear
        elements[4].click()
        wait_until_page_load_by_class_name('mat-option-text')
        element=find_element_by_class_name('mat-option-text')
        element.click()

        wait_until_page_load_by_class_name('mat-select')
        browser.implicitly_wait(50)

        # Button
        element=find_element_by_class_name('mat-flat-button')
        element.click()

    except Exception as ex:
        print(str(ex))


# Producer info function
def producer_info_funct(prescriptionID,
                        orderID,
                        primaryClinicalIndication,
                        biosensorID,
                        procedureDuration,
                        locationGroup
                        ):
    try:
        elements=find_elements_by_class_name('mat-input-element')

        # Prescription ID
        elements[0].clear()
        elements[0].send_keys(str(prescriptionID))

        # Order ID
        elements[1].clear()
        elements[1].send_keys(str(orderID))

        # Primary Clinical Indication
        elements[2].clear()
        elements[2].send_keys(str(primaryClinicalIndication))

        # Biosensor ID
        elements[3].clear()
        elements[3].send_keys(str(biosensorID))

        elements=find_elements_by_class_name('mat-select-value')

        # Procedure Duration
        wait_until_page_load_by_class_name('mat-select-value')
        browser.implicitly_wait(50)
        #el[0].clear()
        elements[0].click()
        wait_until_page_load_by_class_name('mat-option-text')
        elemnt=find_element_by_class_name('mat-option-text')
        elemnt.click()

        # Location Group
        wait_until_page_load_by_class_name('mat-select-value')
        browser.implicitly_wait(50)
        #el[1].clear()
        elements[1].click()
        wait_until_page_load_by_class_name('mat-option-text')
        elemnt=find_element_by_class_name('mat-option-text')
        elemnt.click()

        # Button
        element=find_element_by_class_name('mat-flat-button')
        element.click()

    except Exception as ex:
        print(str(ex))


# Additional info function
def additional_info_funct(additionalInformation,
                          pacemaker,
                          icd
                          ):
    try:
        # Aditional information
        element=find_element_by_class_name('mat-input-element')
        element.send_keys(str(additionalInformation))

        elements=find_elements_by_class_name('mat-checkbox-input')

        # Pacemaker
        elements[0].click()

        # ICD
        elements[1].click()

        # Button
        element=find_element_by_class_name('mat-flat-button')
        element.click()

    except Exception as ex:
        print(str(ex))


# Billing info function
def billing_info_funct(billingIndication,
                          billingMethod
                          ):
    try:
        elements=find_elements_by_class_name('mat-select-value')

        # Billing indication
        wait_until_page_load_by_class_name('mat-select-value')
        browser.implicitly_wait(50)
        #el[0].clear()
        elements[0].click()
        wait_until_page_load_by_class_name('mat-option-text')
        element=find_element_by_class_name('mat-option-text')
        element.click()

        # Billing method
        wait_until_page_load_by_class_name('mat-select-value')
        browser.implicitly_wait(50)
        #el[1].clear()
        elements[1].click()
        wait_until_page_load_by_class_name('mat-option-text')
        element=find_element_by_class_name('mat-option-text')
        element.click()

        # Button
        elements=find_element_by_class_name('mat-flat-button')
        elements.click()


    except Exception as ex:
        print(str(ex))


# New patient registration function 
def new_patient_registration_funct():
    try:
        patient_demographic_funct()
        patient_contact_funct()
        provider_info_funct()
        producer_info_funct()
        additional_info_funct()
        billing_info_funct()
    except Exception as ex:
        print(str(ex))




# new patient registration
el=None

# New patient Registration
def new_patient_registration():
    find_element_by_class_name('registerBtn-in-card').click()
    wait_until_page_load_by_id('mat-dialog-0')

    

    #patient demographics
    try:
        el_pat_demographics = find_element_by_xpath('//*[@id="mat-dialog-0"]/app-admit-patient-modal/mat-dialog-content/form/div[1]/button[1]/span[1]')
        print("[+] demographics btn  found")
    except:
        print('[!] demographics btn not found')

    time.sleep(.8)

    el_pat = find_elements_by_class_name('mat-button')

    try:
        el=find_elements_by_class_name('mat-input-element')
        el[0].clear
        el[0].send_keys('P123')
        el[1].clear
        el[1].send_keys('abcdefgh')
        el[2].clear
        el[2].send_keys('abc')
        el[3].clear
        el[3].send_keys('10/10/2000')
        #browser.execute_script("arguments[0].value = '1980-06-30T00:00:00Z';", date)
        #el[4].clear()
        #el[4].send_keys(22)
        el[5].clear
        el[5].send_keys(59)
        el[6].clear
        el[6].send_keys(200)

        l=find_element_by_class_name('mat-select-value')
        l.click()
        l=find_element_by_class_name('mat-option-text')
        l.click()    
    except:
        print('error')

    el_pat[1].click()

    time.sleep(.8)

    try:
        el=find_elements_by_class_name('mat-input-element')
        el[0].clear()
        el[0].send_keys(1234567890)
        el[1].clear()
        el[1].send_keys('abcde@gmail.com')
        el[2].clear()
        el[2].send_keys(123456)
        el[3].clear()
        el[3].send_keys('ahsvcaka')
        #browser.execute_script("arguments[0].value = '1980-06-30T00:00:00Z';", date)
        #el[4].clear()
        #el[4].send_keys(22)
        el[4].clear()
        el[4].send_keys('sajvfjfve')
        el[5].clear()
        el[5].send_keys('kajdevk')
        el[6].clear()
        el[6].send_keys('ktdtijlmi')
        el[7].clear()
        el[7].send_keys('kkfuenks')
        el[8].clear()
        el[8].send_keys(9987654321)

        el=find_element_by_class_name('mat-select-value')
        el.click()
        l=find_element_by_class_name('mat-option-text')
        l.click()    

        
    except:
        print('error')

    time.sleep(.8)

    el_pat[2].click()


    try:
        el=find_elements_by_class_name('mat-select-value')
        print('el : ',el)

        browser.implicitly_wait(50)
        el[0].clear
        el[0].click()
        wait_until_page_load_by_class_name('mat-option-text')
        l=find_element_by_class_name('mat-option-text')
        l.click()

        wait_until_page_load_by_class_name('mat-select')
        browser.implicitly_wait(50)
        el[1].clear
        el[1].click()
        wait_until_page_load_by_class_name('mat-option-text')
        l=find_element_by_class_name('mat-option-text')
        l.click()

        wait_until_page_load_by_class_name('mat-select')
        browser.implicitly_wait(50)
        el[2].clear
        el[2].click()
        wait_until_page_load_by_class_name('mat-option-text')
        l=find_element_by_class_name('mat-option-text')
        l.click()

        wait_until_page_load_by_class_name('mat-select')
        browser.implicitly_wait(50)
        el[3].clear
        el[3].click()
        wait_until_page_load_by_class_name('mat-option-text')
        l=find_element_by_class_name('mat-option-text')
        l.click()

        wait_until_page_load_by_class_name('mat-select')
        browser.implicitly_wait(50)
        el[4].clear
        el[4].click()
        wait_until_page_load_by_class_name('mat-option-text')
        l=find_element_by_class_name('mat-option-text')
        l.click()

        wait_until_page_load_by_class_name('mat-select')
        browser.implicitly_wait(50)
        
        #l=find_element_by_class_name('mat-select-value')
        #l.click()
        #l=find_element_by_class_name('mat-option-text')
        #l.click()    
    except Exception as ex:
        print('error',str(ex))

    time.sleep(.8)

    el_pat[3].click()

    try:
        el=find_elements_by_class_name('mat-input-element')
        print('el : ',el)

        el[0].clear()
        el[0].send_keys('akjbcj')
        el[1].clear()
        el[1].send_keys('jksbxjc')
        el[2].clear()
        el[2].send_keys('ajvxuqs')
        el[3].clear()
        el[3].send_keys('DP000')

        el=find_elements_by_class_name('mat-select-value')
        
        wait_until_page_load_by_class_name('mat-select-value')
        browser.implicitly_wait(50)
        #el[0].clear()
        el[0].click()
        wait_until_page_load_by_class_name('mat-option-text')
        l=find_element_by_class_name('mat-option-text')
        l.click()

        wait_until_page_load_by_class_name('mat-select-value')
        browser.implicitly_wait(50)
        #el[1].clear()
        el[1].click()
        wait_until_page_load_by_class_name('mat-option-text')
        l=find_element_by_class_name('mat-option-text')
        l.click()

    except Exception as ex:
        print("error : ",str(ex))

    browser.implicitly_wait(50)

    el_pat[4].click()

    wait_until_page_load_by_class_name('mat-input-element')

    try:
        el=find_element_by_class_name('mat-input-element')
        el.send_keys('qsjvxjhwc')
        el=find_elements_by_class_name('mat-checkbox-input')
        el[0].click()
        el[1].click()
    except Exception as ex:
        print('error : ',str(ex))

    browser.implicitly_wait(50)
    el_pat[5].click()

    try:
        el=find_elements_by_class_name('mat-select-value')

        wait_until_page_load_by_class_name('mat-select-value')
        browser.implicitly_wait(50)
        #el[0].clear()
        el[0].click()
        wait_until_page_load_by_class_name('mat-option-text')
        l=find_element_by_class_name('mat-option-text')
        l.click()

        wait_until_page_load_by_class_name('mat-select-value')
        browser.implicitly_wait(50)
        #el[1].clear()
        el[1].click()
        wait_until_page_load_by_class_name('mat-option-text')
        l=find_element_by_class_name('mat-option-text')
        l.click()

        el=find_element_by_class_name('mat-flat-button')
        el.click()


    except Exception as ex:
        print('error : ',str(ex))

    try:
        wait_until_page_load_by_class_name('view-btn')

        el=find_element_by_class_name('view-btn')
        el.click()
    except Exception as ex:
        print("error : ",ex)
    

    

    

    



login_funct("deepak@probeplus.in","deepak123")
new_patient_registration()


time.sleep(30)