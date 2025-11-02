from pages.login_page import LoginPage
from tests.base_test import TestBase

class TestLogin(TestBase):
    def test_valid_login(self):
        self.data = self.excel.get("login","valid credentials")
        self.login_page = LoginPage(self.page)
        self.logged_in_page = self.login_page.valid_login(self.data["username"],self.data["password"])
        assert "Logged In Successfully" in self.logged_in_page.get_logged_in_success_text(), "Expected text 'Logged In Successfully' not found"
    
    def test_invalid_username(self):
        self.data = self.excel.get("login","invalid username")
        self.login_page = LoginPage(self.page)
        is_error_toast_displayed = self.login_page.invalid_login(self.data["username"],self.data["password"])
        assert is_error_toast_displayed, "Error toast not found for invalid username"

    def test_invalid_password(self):
        self.data = self.excel.get("login","invalid password")
        self.login_page = LoginPage(self.page)
        is_error_toast_displayed = self.login_page.invalid_login(self.data["username"],self.data["password"])
        assert is_error_toast_displayed, "Error toast not found for invalid password"

    def test_invalid_login(self):
        self.data = self.excel.get("login","invalid credentials")
        self.login_page = LoginPage(self.page)
        is_error_toast_displayed = self.login_page.invalid_login(self.data["username"],self.data["password"])
        assert is_error_toast_displayed, "Error toast not found for invalid credentials"
    
