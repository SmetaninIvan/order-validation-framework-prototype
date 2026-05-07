class BasePage:
    def __init__(self, driver, db = None):
        self.driver = driver
        self.db = db

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text):
        self.find(locator).send_keys(text)
