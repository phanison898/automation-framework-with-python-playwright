from pages.login_page import LoginPage
from tests.base_test import TestBase

class TestLogin(TestBase):
    def test_login(self):
        self.login_page = LoginPage(self.page)
        self.login_page.login(self.config["username"],self.config["password"])
        assert "Logged In Successfully" in self.page.content(), "Expected text 'Logged In Successfully' not found"
    

