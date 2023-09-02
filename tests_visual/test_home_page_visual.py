import time
import pytest
from pytest_playwright_visual.plugin import assert_snapshot



def test_home_page(set_up, assert_snapshot) -> None:
    page = set_up
    time.sleep(3)

    assert_snapshot(page.screenshot())
