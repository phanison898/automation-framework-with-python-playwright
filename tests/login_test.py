import allure
from pages.login_page import LoginPage
from tests.base_test import TestBase

@allure.title("Test Login Functionality")
class TestLogin(TestBase):

    @allure.title("Valid credentials")
    def test_valid_login(self):
        key = "valid credentials"
        self.data = self.excel.get("login",key)
        self.login_page = LoginPage(self.page)
        self.logged_in_page = self.login_page.enterValidCredentials(self.data["username"],self.data["password"])
        assert self.logged_in_page.get_logged_in_success_text() in self.data['validation'], f"Expected text {self.data['validation']} not found for {key}"
    
    @allure.title("Invalid username")
    def test_invalid_username(self):
        key = "invalid username"
        self.data = self.excel.get("login",key)
        self.login_page = LoginPage(self.page)
        error_text = self.login_page.enterInvalidCredentials(self.data["username"],self.data["password"])
        assert error_text in self.data["validation"], f"Error toast not found for {key}"

    @allure.title("Invalid password")
    def test_invalid_password(self):
        key = "invalid password"
        self.data = self.excel.get("login",key)
        self.login_page = LoginPage(self.page)
        error_text = self.login_page.enterInvalidCredentials(self.data["username"],self.data["password"])
        assert error_text in self.data["validation"], f"Error toast not found for {key}"

    @allure.title("Invalid credentials")
    def test_invalid_login(self):
        key = "invalid credentials"
        self.data = self.excel.get("login",key)
        self.login_page = LoginPage(self.page)
        error_text = self.login_page.enterInvalidCredentials(self.data["username"],self.data["password"])
        assert error_text in self.data["validation"], f"Error toast not found for {key}"
    
    @allure.title("Links validation")
    def test_navigation_links(self):
        link = "Home"
        expected_title = "Practice Test Automation"
        key = "valid credentials"
        self.data = self.excel.get("login",key)
        self.login_page = LoginPage(self.page)
        self.logged_in_page = self.login_page.enterValidCredentials(self.data["username"],self.data["password"])
        actual_title = self.logged_in_page.click_on_nav_link(link)
        assert expected_title in actual_title, f"Title {expected_title} not found"