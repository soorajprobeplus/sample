from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

#import tests.settings as t
t=None
class PageBase:

    def __init__(self, driver):
        self.driver = driver

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, text)))
        return element

    def selectOptionByText(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
        
    def wait_for_correct_current_url(self, desired_url, timeout=10):
        driver = self.driver
        wait = WebDriverWait(driver, timeout)
        wait.until(lambda driver: driver.current_url == desired_url)

    def goTo(self, param):
        driver = self.driver
        url = param[0]
        if url != None:
            driver.get(t.BASE_URL + url)
            return
    
    def isElementVisible(self, locator):
        if (self.driver.find_element(*locator).is_displayed()):
            return True
        return False
    
    def isElementClickable(self, locator):
        if(self.driver.find_element(*locator).is_enabled()):
            return True
        return False
    
        # Click your way to destination
        # TODO: Implement
        pass