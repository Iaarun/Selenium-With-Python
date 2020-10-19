import pytest
from selenium import webdriver
from pageobjects.LoginPage import LoginPage
from utilitiespackage.readconfig import ReadConfiguration
from utilitiespackage.customlogger import GenerateLogs


class Test_01_Login:
    # appurl = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    # username = "admin@yourstore.com"
    # password = "admin"
    appurl = ReadConfiguration.geturl()
    username = ReadConfiguration.get_username()
    password = ReadConfiguration.get_password()

    logger = GenerateLogs.generatelog()

    def test_loginpage_title(self, setup):
        self.logger.info("#########################Test_01_Login Started########################")
        self.logger.info("##################test_loginpage_title  started......############")
        self.driver = setup
        self.driver.get(self.appurl)
        self.logger.info("########## Application Launched ###########")
        act_title = self.driver.title
        if act_title == 'Your store. Login':
            self.logger.info("....... test_loginpage_title  Pass...........")
            self.logger.info("....... Browser closed...........")
            self.driver.close()
            assert True
        else:
            filepath = ".\\Screenshot\\test_loginpage_title.png"
            self.driver.save_screenshot(filepath)
            #self.logger.info("Screenshot Stored at ", filepath)
            self.logger.info("....... test_loginpage_title  Fail...........")
            self.logger.info("....... Browser closed...........")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.logger.info("##################test_login  started......############")
        self.driver = setup
        self.driver.get(self.appurl)
        self.logger.info("########## Application Launched ###########")
        self.lp = LoginPage(self.driver)
        self.lp.set_email(self.username)
        self.logger.info("username entered....")
        self.lp.set_password(self.password)
        self.logger.info("password entered....")
        self.lp.click_login()
        homepagetitle = self.driver.title
        self.lp.click_logout()

        if homepagetitle == 'Dashboard / nopCommerce administration':
            self.logger.info("............test_login Pass.........")
            self.logger.info("....... Browser closed...........")
            self.driver.close()
            assert True, "Page Title is not matching"
        else:
            filepath = ".\\Screenshot\\test_login.png"
            self.driver.save_screenshot(filepath)
            #self.logger.info("Screenshot Stored at ", filepath)
            self.logger.info("............test_login Fail.........")
            self.logger.info("....... Browser closed...........")
            self.driver.close()
            assert False
