import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    # Start Playwright and open the browser
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page

        browser.close()
