import time

import pytest
from playwright.async_api import expect

from pom.generator_page_elements import GeneratorPage


@pytest.mark.smoke()
def test_generator_page(set_up_visual) -> None:
    page = set_up_visual
    generator_page = GeneratorPage(page)
    time.sleep(3)

    # expect(generator_page.container_generator_empty).to_be_visible()
    # expect(generator_page.send_text_field).to_be_visible()
