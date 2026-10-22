from pages.ui.home_page import HomePage


class HomeHelper(HomePage):

    def __init__(self, page, logger):
        super().__init__(page, logger)

    # Load the application URL and wait for the home page to load
    def load_app_url(self, url):
        """
        Load the application URL and wait for the home page to load.
        :param url: The URL of the application to load.
        """
        self.logger.info(f"Loading application URL: {url}")
        self.open_home(url)
        # verify the home page has loaded successfully using url.
        assert self.page.url == url, f"Expected URL: {url}, but got: {self.page.url}"
        self.logger.info("Application URL loaded successfully.")
