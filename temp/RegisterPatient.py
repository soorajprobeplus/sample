from selenium.webdriver.common.by import By
#import Type
from temp.FormBase import FormBase, Type

#from libs.FormBase import FormBase
#import tests.settings as t



class RegisterPatientPage():

  # Regiser Patient Form Locators
  formDict0 = {
    # Tab : 
    "patient_demography" : {
      "_"           : (Type.FIELD, By.CSS_SELECTOR, '.mat-primary > .mat-button-wrapper'),
      "patientID"   : (Type.FIELD, By.NAME, 'option'),
      "firstName"   : (Type.FIELD, By.NAME, 'first_name'),
      "lastName"    : (Type.FIELD, By.NAME, 'last_name'),
      "dateOfBirth" : (Type.FIELD, By.NAME, 'dob'),
      "weight"      : (Type.FIELD, By.NAME, 'weight'),
      "height"      : (Type.FIELD, By.NAME, 'height'),
      "sex-selector": (Type.BUTTON, By.CLASS_NAME, 'mat-select-value'),
      "sex-opt"     : (Type.BUTTON, By.CLASS_NAME, 'mat-option-text'),
      "sex"         : (Type.LIST, "sex-selector", "sex-opt")
    }
  }

  formDict = {
    # Tab : 
    "patient_demography" : {
      "_"           : (Type.BUTTON, By.CSS_SELECTOR, '.mat-primary > .mat-button-wrapper'),
      "patientID"   : (Type.FIELD, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[2]/div/mat-form-field/div/div[1]/div/input'),
      "firstName"   : (Type.FIELD, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[3]/div[1]/mat-form-field/div/div[1]/div/input'),
      "lastName"    : (Type.FIELD, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[3]/div[2]/mat-form-field/div/div[1]/div/input'),
      "dateOfBirth" : (Type.FIELD, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[4]/div[1]/div/div[1]/mat-form-field/div/div[1]/div[1]/input'),
      "weight"      : (Type.FIELD, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[5]/div[1]/div/mat-form-field/div/div[1]/div/input'),
      "height"      : (Type.FIELD, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[5]/div[2]/mat-form-field/div/div[1]/div/input'),
      "sex-selector": (Type.BUTTON, By.CLASS_NAME, 'mat-select-value'),
      "sex-opt"     : (Type.BUTTON, By.CLASS_NAME, 'mat-option-text'),
      "sex"         : (Type.LIST, "sex-selector", "sex-opt")
    },

    "patient_contact" : {
        "_"                     : (Type.BUTTON, By.CSS_SELECTOR, '.mat-primary > .mat-button-wrapper'),
        "countryCode"           : (Type.LIST, 'countryCode-selector', 'countryCode-opt'),
        "countryCode-selector"  : (Type.BUTTON, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[2]/div[1]/app-tel-input/div/mat-form-field/div/div[1]/div[1]/lac-mat-country-selector/button'),
        "countryCode-opt"       : (Type.BUTTON, By.CLASS_NAME, 'label-wrapper'),
        "primaryContactNo"      : (Type.FIELD, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[2]/div[1]/div/app-tel-input/div/mat-form-field/div/div[1]/div[2]/lac-mat-tel-input/input'),
        "emailID"               : (Type.FIELD, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[2]/div[2]/mat-form-field/div/div[1]/div/input'),
        "country"               : (Type.FIELD, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[3]/div[1]/mat-form-field/div/div[1]/div/input'),
        "country-selector"      : (Type.BUTTON, By.XPATH , '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[3]/div[1]/mat-form-field/div/div[1]/div/input'),
        "country-opt"           : (Type.BUTTON, By.CLASS_NAME, 'mat-option-text'),
        "zipCode"               : (Type.FIELD, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[3]/div[2]/mat-form-field/div/div[1]/div/input'),
        "streetAdress1"         : (Type.FIELD, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[4]/mat-form-field/div/div[1]/div/input'),
        "streetAdress2"         : (Type.FIELD, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[5]/mat-form-field/div/div[1]/div/input'),
        "state_"                : (Type.BUTTON, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[6]/div[1]/mat-form-field/div/div[1]/div/input'),
        "state"                 : (Type.FIELD, By.XPATH,'/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[6]/div[1]/mat-form-field/div/div[1]/div/input'),
        "city"                  : (Type.FIELD, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[6]/div[2]/mat-form-field/div/div[1]/div/input'),
        "emergencyContactName"    : (Type.FIELD, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[7]/div[1]/mat-form-field/div/div[1]/div/input'),
        "emergencyContactNo"  : (Type.FIELD, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[7]/div[2]/div/app-tel-input/div/mat-form-field/div/div[1]/div[2]/lac-mat-tel-input/input'),
    },

    "provider_info": {
        "_"                                         : (Type.BUTTON, By.CSS_SELECTOR, '.mat-primary > .mat-button-wrapper'),
        "prescribingPhysician"                      : (Type.LIST ,'prescribingPhysician-selector', "prescribingPhysician-opt" ),
        "prescribingPhysician-selector"             : (Type.BUTTON, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[2]/div[1]/mat-form-field/div/div[1]/div/mat-select/div/div[1]'),
        "prescribingPhysician-opt"                  : (Type.BUTTON, By.CLASS_NAME, 'mat-option-text'),
        "referalPhysician"                          : (Type.LIST, "referalPhysician-selector", "referalPhysician-opt"),
        "referalPhysician-selector"                 : (Type.BUTTON, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[2]/div[2]/mat-form-field/div/div[1]/div/mat-select/div/div[1]'),
        "referalPhysician-opt"                      : (Type.BUTTON, By.CLASS_NAME, 'mat-option-text'),
        "interpretingPhysician"                     : (Type.LIST, "interpretingPhysician-selector", "interpretingPhysician-opt"),
        "interpretingPhysician-selector"            : (Type.BUTTON, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[2]/div[3]/mat-form-field/div/div[1]/div/mat-select/div/div[1]'),
        "interpretingPhysician-opt"                 : (Type.BUTTON, By.CLASS_NAME, 'mat-option-text'),
        "preliminaryInterpretingPhysician"          : (Type.LIST, "preliminaryInterpretingPhysician-selector", "preliminaryInterpretingPhysician-opt"),
        "preliminaryInterpretingPhysician-selector" : (Type.BUTTON, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[2]/div[4]/mat-form-field/div/div[1]/div/mat-select/div/div[1]'),
        "preliminaryInterpretingPhysician-opt"      : (Type.BUTTON, By.CLASS_NAME, 'mat-option-text'),
        "technician"                                : (Type.LIST, "technician-slector", "technician-opt"),
        "technician-slector"                        : (Type.LIST, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[2]/div[5]/mat-form-field/div/div[1]/div/mat-select/div/div[1]'),
        "technician-opt"                            : (Type.BUTTON, By.CLASS_NAME, 'mat-option-text')
    },

    "procedure_info": {
        "_"                             : (Type.BUTTON, By.CSS_SELECTOR, '.mat-primary > .mat-button-wrapper'),
        "prescriptionID"                : (Type.FIELD, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[2]/div[1]/mat-form-field/div/div[1]/div/input'),
        "orderID"                       : (Type.FIELD, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[2]/div[2]/mat-form-field/div/div[1]/div/input'),
        "primaryClinicalIndication"     : (Type.FIELD, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[3]/div/mat-form-field/div/div[1]/div/input'),
        "biosensorID"                   : (Type.FIELD, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[4]/div/mat-form-field/div/div[1]/div[1]/input'),
        "procedureDuration"             : (Type.LIST, "procedureDuration-selector" , "procedureDuration-opt" ),
        "procedureDuration-selector"    : (Type.BUTTON, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[4]/div[2]/div/mat-form-field/div/div[1]/div/mat-select/div/div[1]'),
        "procedureDuration-opt"         : (Type.BUTTON, By.CLASS_NAME, 'mat-option-text'),
        "locationGroup"                 : (Type.LIST, "locationGroup-selector", "locationGroup-opt" ),
        "locationGroup-selector"        : (Type.BUTTON, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[4]/div[1]/div/app-nested-dropdown/div'),
        "locationGroup-opt"             : (Type.BUTTON, By.CLASS_NAME, 'nested-menu-item')
    },

    "additional_info": {
        "_"                     : (Type.BUTTON, By.CSS_SELECTOR, '.mat-primary > .mat-button-wrapper'),
        "additionalInformation" : (Type.FIELD, By.CLASS_NAME, 'mat-input-element'),
        "pacemaker"             : (Type.CHECK, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[2]/div[2]/div[1]/input'),
        "icd"                   : (Type.CHECK, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[2]/div[2]/div[2]/input')
    },

    "billing_info": {
        "_"                         : (Type.BUTTON, By.CSS_SELECTOR, '.mat-primary > .mat-button-wrapper'),
        "billingIndication"         : (Type.LIST, "billingIndication-selector", "billingIndication-opt"),
        "billingIndication-selector": (Type.BUTTON, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[2]/div[1]/mat-form-field/div/div[1]/div/mat-select/div/div[1]'),
        "billingIndication-opt"     : (Type.BUTTON, By.CLASS_NAME, 'mat-option-text'),
        "billingMethod"             : (Type.LIST, "billingMethod-selector", "billingMethod-opt"),
        "billingMethod-selector"    : (Type.BUTTON, By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[2]/div[2]/mat-form-field/div/div[1]/div/mat-select/div/div[1]'),
        "billingMethod-opt"         : (Type.BUTTON, By.CLASS_NAME, 'mat-option-text'),
    }
  }

  # Routing Table
  #  There is no routes from Register Patient Dialog 

  def __init__(self, driver):
    self.driver = driver

  def Up(self):
    label =  "/html/body/app-root/app-root/app-summary/div/div/div[1]/app-setting-card[1]/div/div/div[2]/label[1]"
    #self.wait_for_correct_current_url(t.BASE_URL + "/#/summary")
    posted_final = self.driver.find_element(By.XPATH, label).text
    return posted_final == "Posted Final" 
  
  def clickTab(self, tab):
    #self.driver.find_element(By.XPATH, tab).click()
    pass

  def fillPatientDetails(self, patientData):
    typist = FormBase(self.driver)

    for tabs in list(patientData.keys()):
        typist.fillForm(self.formDict[tabs], patientData[tabs])
        continue
    

    #Press OK to submit..
    # check if patient is succcessfully registered.
    # check if dialog is closed..
    #return elementisPresent #True / False