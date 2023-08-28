import time
import pytest
from pytest_playwright_visual.plugin import assert_snapshot
from pom.generator_page_elements import GeneratorPage


def test_prices_page(set_up, assert_snapshot) -> None:
    page = set_up
    generator_page = GeneratorPage(page)

    generator_page.prices.click()
    time.sleep(3)

    assert_snapshot(page.screenshot())
