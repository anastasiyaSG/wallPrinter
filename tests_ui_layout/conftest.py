import pytest
from playwright.async_api import Playwright

from pom.home_page_elements import HomePage


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

    generator_page = HomePage(page)
    generator_page.input_field.fill("student")

    yield context


@pytest.fixture()
def creating_image_student(context_creation):
    context = context_creation
    page = context.new_page()
    page.goto("https://wallprinter.bg/")
    page.set_default_timeout(3000)

    yield page
