# Import the libraries.
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import time
# Create variables for login credentials.
username = "deepak@probeplus.in"
password = "deepak123"


#browser = webdriver.Chrome('chrome-driver',"C:/Users/soorajKS/project1/chromedriver")

service = Service(executable_path='C:/Users/soorajKS/project1/chromedriver.exe')
browser = webdriver.Chrome(service=service)


#driver = webdriver.Chrome(executable_path="C:/Users/soorajKS/project1/chromedriver.exe")

browser.maximize_window()

# webdriver.Chrome()

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
# Launch the browser and open the github URL in your web driver.
browser.get("http://10.10.5.76")

sessionid = browser.session_id
print("session id : ",sessionid)

localstoage = browser.execute_script("return window.localStorage;")
cookies = browser.get_cookies
print('cookies :',cookies)
print('local storage : ',localstoage)
delay = 2 # seconds


def wait_until_page_load(name):
    try:
        myyElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, str(name))))
        print("Page is Ready")
    except:
        print("Loading took too much time!")

def login(usr,passd):

    uname = find_element_by_id("username") 
    uname.clear()
    uname.send_keys(str(usr))
    pword = find_element_by_id("password") 
    pword.clear()
    pword.send_keys(str(passd))
    find_element_by_id("kc-login").click()
    print("username : ",usr)
    print("password : ",passd)
    time.sleep(1)
    # Verify that the login was successful.
    error_message = "Invalid username or password."
    # Retrieve any errors found. 
    errors = ""
    errors = find_elements_by_id("input-error")

    # When errors are found, the login will fail. 
    if any(error_message in e.text for e in errors): 
        print("[!] Login failed")
    else:
        print("[+] Login successful")
    wait_until_page_load("app-card")

    get_url = browser.current_url
    print(get_url)
    if(get_url=="http://10.10.5.76/#/summary"):
        print("[+] url Login successful")
    else:
        print("[!] url Login failed")
    
# End of login


def common_page():
    tiles=[]
    tiles=find_elements_by_class_name("app-card")
    print('tiles count : ',tiles.count)





def find_element_by_id(id):
    return browser.find_element(By.ID, str(id))

def find_element_by_class_name(name):
    return browser.find_element(By.CLASS_NAME, str(name))

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

# iterable elements

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




# Find the username/email field and send the username to the input field.
#uname = browser.find_element("id", "username") 
#uname.send_keys("deepak@probeplus.in")

# Find the password input field and send the password to the input field.
#pword = browser.find_element("id", "password") 
#pword.send_keys("deepak123")

# Click sign in button to login the website.
#browser.find_element("id", "kc-login").click()

# time.sleep(20)



login("deepak@probepls.in","deepak")
login("deepak@probepls.in","deepak")

login("deepak@probeplus.in","deepak123")
common_page()
find_element_by_class_name("app-card").click()

#try:
#    myyElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'app-card')))
#    print("Page is Ready")
#except:
#    print("Loading took too much time!")

#browser.find_element(By.CLASS_NAME,'app-card').click()

#find_element_by_class_name("app-card").click()

time.sleep(3)

browser.back()


time.sleep(10)