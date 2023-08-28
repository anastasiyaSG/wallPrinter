import pytest
from playwright.async_api import Playwright


@pytest.fixture()
def set_up(page):
    page.goto("https://wallprinter.bg/")
    page.set_default_timeout(3000)

    yield page

@pytest.fixture()
def set_up_visual(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://wallprinter.bg/")

    yield page


@pytest.fixture(scope='session')
def context_creation(playwright):
    browser = playwright.chromium.launch(headless=True, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)

    page = context.new_page()
    page.goto("https://wallprinter.bg/")
    page.set_default_timeout(3000)
    #
    # login_page = LoginPage(page)
    # login_page.username.fill("student")
    # login_page.password.fill("Password123")
    # login_page.submit.click()

    yield context


@pytest.fixture()
def login_session(context_creation):
    context = context_creation
    page = context.new_page()
    page.goto("https://wallprinter.bg/")
    page.set_default_timeout(3000)

    yield page
