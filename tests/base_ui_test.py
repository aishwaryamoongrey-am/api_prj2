import pytest
from helper.ui.home_helper import HomeHelper


class BaseUiTest:

    @pytest.fixture(autouse=True)
    def setup(self, page, logger):
        logger.info("UI Test Started")
        self.homehelper = HomeHelper(page, logger)
        yield
        logger.info("UI Test Completed")
