from enum import Enum
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
import pdb

class Type(Enum):
    FIELD  = 0
    BUTTON = 1
    CHECK  = 2
    LIST   = 3
    DATE   = 4

class FormBase:

    def __init__(self, driver):
        self.driver = driver

    def passParams(self, params):
        self.params = params


    # Wait for loading elements
    def wait_until_page_load_by_class_name(self, value):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, str(value))))
        if element != None:
            element.click()

    def select_option(self, locator, value):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator))
        
        elements = self.driver.find_elements(*locator)
        for opt in elements:
            if opt.text == value:
                opt.click()

    def wait_funct(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        
            
    def fillForm(self, dictLoc, dictValue):
        """
            dictLoc : location dictionary - has (Type, x, y)
            x, y  : depends on type - can be additional locators
            dictValue : form field value dictionary, key is also the key to locator dict
            Pick the locator value and check the action needed by type
        """
        for field in dictValue.items():
            #import pdb; pdb.set_trace()
            key     = dictLoc[field[0]]    #locator entry
            value   = field[1]             #form data value
            locator = key[1:3]             #actual locator
            element = key[0]               #form field type

            if element == Type.BUTTON:
                self.driver.find_element(*locator).click()
                continue

            if element == Type.FIELD:
                # clickable element selector
                #self.wait_funct(*locator)
                self.driver.find_element(*locator).clear()
                self.driver.find_element(*locator).send_keys(value)
                continue

            if element == Type.CHECK:
                # Checkbox / Radiobox
                #self.driver.find_element(*locator).clear()
                if (value):
                    self.driver.find_element(*locator).click()
                continue    
            
            if element == Type.LIST:
                # Drop-down list selection
                list_locator = dictLoc[key[1]]
                el = self.driver.find_element(*list_locator[1:3])
                el.click()
                time.sleep(.1)
                # get the options locator and wait for elements to load
                option_locator = dictLoc[key[2]]
                self.select_option(option_locator[1:3], value)
                continue








