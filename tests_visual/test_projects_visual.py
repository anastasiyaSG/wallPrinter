import time
import pytest
from pytest_playwright_visual.plugin import assert_snapshot
from pom.home_page_elements import HomePage


def test_projects_page(set_up, assert_snapshot) -> None:
    page = set_up
    generator_page = HomePage(page)

    generator_page.projects.click()
    time.sleep(3)

    assert_snapshot(page.screenshot())
