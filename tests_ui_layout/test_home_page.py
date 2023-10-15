import time

import pytest
from playwright.sync_api import expect

from pom.home_page_elements import HomePage


@pytest.mark.smoke()
def test_home_page_load_successfully(set_up) -> None:
    # Given
    page = set_up

    # When
    home_page = HomePage(page)

    # Then
    expect(home_page.logo_button).to_be_visible()
    expect(home_page.search_field).to_be_visible()


@pytest.mark.skip(reason="not generate too much images for tests")
@pytest.mark.smoke()
def test_home_page_generate_image(set_up) -> None:
    # Given
    page = set_up
    home_page = HomePage(page)
    # When

    home_page.generator.click()
    home_page.input_field.fill("Kрасиво цвете")

    # Then
    expect(home_page.generate_product_button).to_be_visible()


@pytest.mark.skip(reason="not generate too much images for tests")
@pytest.mark.smoke()
def test_home_search_field_find_correctly_in_context(creating_image_student) -> None:
    # Given
    page = creating_image_student
    generator_page = HomePage(page)
    # When
    generator_page.search_field.fill("student")
    # Then
    expect(page.get_by_text("student").nth(1)).to_be_visible()


@pytest.mark.parametrize("search_letter", ["happiness", "щастие", "любов"])
@pytest.mark.smoke()
def test_home_search_field_find_correctly(set_up_visual, search_letter) -> None:
    # Given
    page = set_up_visual
    home_page = HomePage(page)
    # When
    home_page.generator.click()
    home_page.search_field.fill(search_letter)
    home_page.search_field.press("Enter")
    # Then
    expect(page.get_by_role("heading", name=f"You searched for : {search_letter}")).to_be_visible()
