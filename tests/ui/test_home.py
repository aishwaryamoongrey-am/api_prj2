import allure
import pytest
from data.test_data import HOME_URL

from tests.base_ui_test import BaseUiTest


@pytest.mark.home
@pytest.mark.smoke
class TestHome(BaseUiTest):
    @allure.title("Verify Diagnostic Centres url loads successfully")
    def test_app_url_loads(self):
        """
        Test to verify that the application URL loads successfully.
        Steps:
        1. Load the application URL.
        2. Verify that the home page has loaded successfully.
        """
        self.homehelper.load_app_url(url=HOME_URL)
