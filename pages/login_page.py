import allure
from pages.base_page import BasePage
from pages.logged_in_page import LoggedInPage

class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.username_input = '#username'
        self.password_input = '#password'
        self.submit_button = '#submit'
        self.error_toast = '#error'

    def _attach_screenshot(self, name: str):
        allure.attach(
            self.page.screenshot(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    def enterValidCredentials(self, username: str, password: str) -> LoggedInPage:
        self.login(username,password)
        with allure.step("Navigate to LoggedInPage"):
            return LoggedInPage(self.page)
        
    def enterInvalidCredentials(self, username: str, password: str) -> str:
        self.login(username,password)
        with allure.step("Error toast"):
            self.scroll_into_view(self.error_toast)
            self._attach_screenshot("error-toast")
            return self.get_text(self.error_toast)

    def login(self, username: str, password: str):
        with allure.step("Enter username and password"):
            self.enter(self.username_input, username)
            self.enter(self.password_input, password)
            self._attach_screenshot("entered-credentials")
        with allure.step("Click on Submit button"):
            self.click(self.submit_button)
