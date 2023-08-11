import drivers.chromeDriver as driver
import tests.test_login as logintest

driver_=driver.chrome_driver('http://10.10.5.76/')

first_test=logintest.test_login(driver_)

