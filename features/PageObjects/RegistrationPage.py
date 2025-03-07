from features.PageObjects.BasePage import BasePage


class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open(self,url):
        self.driver.get(url)

    def setName(self, name):
        self.type("name_XPATH", name)

    def setPhoneNumber(self, phoneNum):
        self.type("phone_XPATH",phoneNum)

    def setEmail(self, email):
        self.type("email_XPATH", email)

    def setCountry(self, country):
        self.select("country_XPATH",country)

    def setCity(self, city):
        self.type("city_XPATH", city)

    def setUserName(self, username):
        self.type("username_XPATH", username)

    def setPassword(self, passwd):
        self.type("password_XPATH", passwd)

    def submitForm(self):
        self.click("submit_XPATH")
