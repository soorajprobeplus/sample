from utilities.utilities import *

class LoginPage :
    def __init__(self, driver):
        self.driver = driver
    
    def get_username(self,value):
        return find_element_by_class_name(str(value),self.driver)
    
    def get_password(self,value):
        return find_element_by_class_name(str(value),self.driver)
    
    def get_submit_button(self,value):
        return find_element_by_class_name(str(value),self.driver)
    
