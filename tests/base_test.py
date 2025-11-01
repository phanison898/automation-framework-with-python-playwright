import pytest

@pytest.mark.usefixtures("config", "page")
class TestBase:
    @pytest.fixture(autouse=True)
    def inject_fixtures(self, request):
        self.page = request.getfixturevalue("page")
        self.config = request.getfixturevalue("config")


