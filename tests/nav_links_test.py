from tests.base_test import TestBase
from pages.login_page import LoginPage
import allure

@allure.title("Test Login Functionality")
class TestNavLinks(TestBase):
    
    @allure.title("Validate navigation links")
    def test_navigation_links(self):
        data = self.excel.get_all_data("nav links")
        for row in data:
            # Each excel row data
            link = row.get("link name")
            expected_url_end_point = row.get("expected url endpoint")
            expected_page_title = row.get("expected page title")
            # Login
            key = "valid credentials"
            login_data = self.excel.get("login",key)
            self.login_page = LoginPage(self.page)
            self.logged_in_page = self.login_page.enterValidCredentials(login_data["username"],login_data["password"])
            assert self.logged_in_page.get_logged_in_success_text() in login_data['validation'], f"Expected text {login_data['validation']} not found for {key}"
            # Clicking on links
            actual_url_end_point, actual_page_title = self.logged_in_page.click_on_nav_link(link)
            assert expected_url_end_point in actual_url_end_point
            assert expected_page_title in actual_page_title
           
        