from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def chrome_driver(url):

    # WebDriver
    service = Service(executable_path='C:/Users/soorajKS/project1/chromedriver.exe')
    options = Options()
    options.add_experimental_option("detach", True)
    browser = None
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    #browser.implicitly_wait(10)
    #https://www.ecgvue.site/  http://10.10.5.76/
    browser.get(url)
    return browser