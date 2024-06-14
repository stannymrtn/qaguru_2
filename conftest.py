import pytest
from selene import browser


@pytest.fixture(scope="session")
def browser_driver():
    browser.config.base_url = 'https://google.com'
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    yield
    browser.quit()
