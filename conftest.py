import os

import allure
import pytest
from data.test_data import BASE_URL
from playwright.sync_api import sync_playwright
from utils.logger import get_logger


@pytest.fixture
def logger(request):
    return get_logger(request.node.name)


@pytest.fixture
def page(browser_name, browser_type_launch_args):
    with sync_playwright() as p:
        browser_type = getattr(p, browser_name)
        browser = browser_type.launch(**browser_type_launch_args)
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        page.goto(BASE_URL)
        yield page
        context.close()
        browser.close()
