import pytest

@pytest.mark.usefixtures("config", "page", "excel")
class TestBase:
    @pytest.fixture(autouse=True)
    def inject_fixtures(self, request):
        self.page = request.getfixturevalue("page")
        self.config = request.getfixturevalue("config")
        self.excel = request.getfixturevalue("excel")


