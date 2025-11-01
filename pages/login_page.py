from pages.base_page import BasePage
from pages.logged_in_page import LoggedInPage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = '#username'
        self.password_input = '#password'
        self.submit_button = '#submit'
        self.error_toast = '#error'
    
    def valid_login(self, username:str, password:str) -> LoggedInPage:
        self.enter(self.username_input, username)
        self.enter(self.password_input, password)
        self.click(self.submit_button)
        return LoggedInPage(self.page)
    
    def invalid_login(self, username:str, password:str) -> bool:
        self.enter(self.username_input, username)
        self.enter(self.password_input, password)
        self.click(self.submit_button)
        return self.is_visible(self.error_toast)

