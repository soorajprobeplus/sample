from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

delay = 10 # seconds

# Locator single element
def find_element_by_id(value,browser):
    return browser.find_element(By.ID, str(value))

def find_element_by_class_name(value,browser):
    return browser.find_element(By.CLASS_NAME, str(value))
       
def find_element_by_name(value,browser) :
    return browser.find_element(By.NAME,str(value))

def find_element_by_link_text(value,browser) :
    return browser.find_element(By.LINK_TEXT,str(value))

def find_element_by_partial_link_text(value,browser) :
    return browser.find_element(By.PARTIAL_LINK_TEXT,str(value))

def find_element_by_tag_name(value,browser) :
    return browser.find_element(By.TAG_NAME,str(value))

def find_element_by_css_selector(value,browser) :
    return browser.find_element(By.CSS_SELECTOR,str(value))

def find_element_by_xpath(value,browser) :
    return browser.find_element(By.XPATH,str(value))


# Locator iterable elements
def find_elements_by_id(id,browser):
    return browser.find_elements(By.ID, str(id))

def find_elements_by_class_name(name,browser):
    return browser.find_elements(By.CLASS_NAME, str(name))
       
def find_elements_by_name(value,browser) :
    return browser.find_elements(By.NAME,str(value))
    
def find_elements_by_link_text(value,browser) :
    return browser.find_elements(By.LINK_TEXT,str(value))

def find_elements_by_partial_link_text(value,browser) :
    return browser.find_elements(By.PARTIAL_LINK_TEXT,str(value))

def find_elements_by_tag_name(value,browser) :
    return browser.find_elements(By.TAG_NAME,str(value))

def find_elements_by_css_selector(value,browser) :
    return browser.find_elements(By.CSS_SELECTOR,str(value))

def find_element_by_xpath(value,browser) :
    return browser.find_element(By.XPATH,str(value))


# Wait for loading elements
def wait_until_page_load_by_class_name(browser,value):
    try:
        element = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, str(value))))
        #print("Page is Ready")
    except:
        print("Loading took too much time!")

def wait_until_page_load_by_id(browser,value):
    try:
        element = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, str(value))))
        #print("Page is Ready")
    except:
        print("Loading took too much time!")

def wait_until_page_load_by_xpath(browser,value):
    try:
        element = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, str(value))))
        #print("Page is Ready")
    except:
        print("Loading took too much time!")