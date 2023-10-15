import pytest
from playwright.sync_api import expect

from pom.generator_page import GeneratorPage
from pom.home_page_elements import HomePage


def test_successfully_load_generator_page(set_up) -> None:
    # Given
    page = set_up

    # When
    home_page = HomePage(page)
    home_page.generator.click()

    # Then
    generator_page = GeneratorPage(page)
    expect(generator_page.generator_container).to_be_visible()
    expect(generator_page.generator_not_created_text).to_be_visible()
    expect(generator_page.input_field).to_be_visible()
    expect(generator_page.generate_product_button).to_be_visible()


@pytest.mark.skip(reason='creation of images is out of scope')
def test_create_image(set_up) -> None:
    # Given
    page = set_up
    home_page = HomePage(page)
    home_page.generator.click()

    # When
    generator_page = GeneratorPage(page)
    generator_page.input_field.fill("Cat")
    generator_page.generate_product_button.click()

    # Then
    expect(page.get_by_role("img", name="Cat")).to_be_visible()
