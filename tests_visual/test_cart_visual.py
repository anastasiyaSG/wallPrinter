import time
import pytest
from pytest_playwright_visual.plugin import assert_snapshot
from pom.home_page_elements import HomePage


@pytest.mark.skip(reason="Available only when there is select item on it")
def test_cart_page(set_up, assert_snapshot) -> None:
    page = set_up
    generator_page = HomePage(page)
    time.sleep(3)

    generator_page.cart.click()

    assert_snapshot(page.screenshot())
