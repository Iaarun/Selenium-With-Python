import pytest
from selenium import webdriver
from pageobjects.LoginPage import LoginPage
from utilitiespackage.readconfig import ReadConfiguration
from utilitiespackage.customlogger import GenerateLogs
from utilitiespackage import ExcelReading

class Test_01_Login:
    # appurl = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    # username = "admin@yourstore.com"
    # password = "admin"
    appurl = ReadConfiguration.geturl()
    #username = ReadConfiguration.get_username()
    #password = ReadConfiguration.get_password()
    datafile = "./TestData/LoginData.xlsx"

    logger = GenerateLogs.generatelog()

    def test_login(self, setup):
        self.logger.info("##################test_login  started......############")
        self.driver = setup
        self.driver.get(self.appurl)
        self.logger.info("########## Application Launched ###########")
        self.lp = LoginPage(self.driver)
        self.rows = ExcelReading.get_row_count(self.datafile, "Sheet1")

        for r in range(2, self.rows+1):
            self.username = ExcelReading.read_data(self.datafile, "Sheet1", r, 1)
            print(self.username)
            self.password = ExcelReading.read_data(self.datafile, "Sheet1", r, 2)
            #reading expected result
            self.expected = ExcelReading.read_data(self.datafile, "Sheet1", r, 3)
            self.lp.set_email(self.username)
            self.logger.info("username entered....")
            self.lp.set_password(self.password)
            self.logger.info("password entered....")
            self.lp.click_login()
            homepagetitle = self.driver.title
            expectedtitle = 'Dashboard / nopCommerce administration'
            lst_status = []
            if homepagetitle == expectedtitle:
                if self.expected == 'Pass':
                    self.logger.info("............Pass.........")
                    self.lp.click_logout()
                    lst_status.append("Pass")

                elif self.expected == 'Fail':
                    self.logger.info("............Fail.........")
                    filepath = ".\\Screenshot\\test_login.png"
                    self.driver.save_screenshot(filepath)
                    self.logger.info("............test_login Fail.........")
                    self.lp.click_logout()
                    lst_status.append("Fail")

            if homepagetitle != expectedtitle:
                if self.expected == 'Pass':
                    self.logger('..........Fail........')
                    lst_status.append("Fail")

                elif self.expected == 'Fail':
                    self.logger('..........Pass........')
                    lst_status.append("Pass")

        print(lst_status)
        if "Fail" not in list:
            self.logger.info(" DataDriver test pass")
            self.driver.close
            assert True
        else:
            self.logger.info(" DataDriver test Fail")
            self.driver.close
            assert False

