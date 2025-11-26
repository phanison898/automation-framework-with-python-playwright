import allure
from pages.base_page import BasePage

class LoggedInPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.logged_in_success_text_locator = ".post-title"
        self.nav_links = "ul#menu-primary-items li"
    
    def get_logged_in_success_text(self):
        with allure.step("Login success"):
            self._attach_screenshot("login-success")
            return self.get_text(self.logged_in_success_text_locator)
    
    def click_on_nav_link(self, link_name):
        with allure.step(f"Click on {link_name} link"):
            self.click(self.nav_links,link_name)
            return [self.get_current_url(), self.get_page_title()]
