import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        yield context
        browser.close()

def test_homepage(browser_context):
    page = browser_context.new_page()
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
    page.screenshot(path="screenshots/homepage.png")

def test_navigation(browser_context):
    page = browser_context.new_page()
    page.goto("https://example.com")
    page.click("text=More information...")
    assert page.url == "https://www.iana.org/domains/reserved"
    page.screenshot(path="screenshots/navigation.png")
