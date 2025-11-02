import allure
from pages.base_page import BasePage

class LoggedInPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.logged_in_success_text_locator = ".post-title"
    
    def get_logged_in_success_text(self):
        with allure.step("Login success"):
            self._attach_screenshot("login-success")
            return self.get_text(self.logged_in_success_text_locator)