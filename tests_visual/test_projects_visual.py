import time
import pytest
from pytest_playwright_visual.plugin import assert_snapshot
from pom.home_page_elements import HomePage
from pom.projects_page_elements import ProjectPage


def test_projects_page(set_up, assert_snapshot) -> None:
    page = set_up

    page.get_by_role("link", name="Проекти")
    time.sleep(3)

    assert_snapshot(page.screenshot())
