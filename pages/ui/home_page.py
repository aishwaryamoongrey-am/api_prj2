class HomePage:

    # Constructor to initialize the HomePage class with page and logger
    def __init__(self, page, logger):
        """
        Initialize the HomePage class with the given page and logger.
        :param page: The Playwright page object.
        :param logger: The logger object for logging messages."""
        self.page = page
        self.logger = logger

    # Open the home page and wait for it to load
    def open_home(self, url):
        """
        Open the home page and wait for it to load.
        :param url: The URL of the home page to open."""
        self.logger.info(f"Opening URL: {url}")
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")
        self.logger.info("Home page loaded successfully")
