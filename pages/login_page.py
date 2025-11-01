from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = '#username'
        self.password_input = '#password'
        self.submit_button = '#submit'
    
    def login(self, username:str, password:str):
        self.enter(self.username_input, username)
        self.enter(self.password_input, password)
        self.click(self.submit_button)
