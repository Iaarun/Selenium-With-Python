class LoginPage:
    email_id = "Email"
    password_id = "Password"
    login_xpath = "//input[@value='Log in']"
    logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, username):
        self.driver.find_element_by_id(self.email_id).clear()
        self.driver.find_element_by_id(self.email_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element_by_id(self.password_id).clear()
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_linktext).click()
