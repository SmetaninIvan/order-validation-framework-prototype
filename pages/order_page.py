from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderPage(BasePage):
    CREATE_BTN = (By.ID, "create-order")
    NAME_INPUT = (By.ID, "order-name")
    SAVE_BTN = (By.ID, "save-order")

    def create_order(self, name):
        self.click(self.CREATE_BTN)
        self.type(self.NAME_INPUT, name)
        self.click(self.SAVE_BTN)