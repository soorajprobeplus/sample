from pageObject.loginPage import *
from locators.locators import *
import pytest
import json



locators=locators['login_page']
datas=None
with open('./testData/user_login.json') as json_file:
    data = json.load(json_file)
class test_login():

    def __init__(self, driver):
        self.driver = driver
    
    def form_submission(self):

        loginpage=LoginPage(self.driver)

        username=loginpage.get_username(locators['user_name']).send_keys(data['username'])
        password=loginpage.get_password(locators['password']).send_keys(data['password'])
        submitbutton=loginpage.get_submit_button().click()

    @pytest.fixture(params='test passed')
    def getResult(self, request):
        return request.param



