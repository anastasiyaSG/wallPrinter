import pytest
from playwright.sync_api import expect

from pom.decoration_page import DecorationPage
from pom.home_page_elements import HomePage


def test_decoration_page_has_last_projects(set_up) -> None:
    # Given
    page = set_up
    home_page = HomePage(page)
    home_page.decoration.click()

    # When
    decoration_page = DecorationPage(page)

    # Then
    expect(decoration_page.last_generated).to_be_visible()
    expect(decoration_page.first_of_four_45).to_be_visible()
    expect(decoration_page.first_of_four_175).to_be_visible()
    expect(decoration_page.last_of_four_45).to_be_visible()
    expect(decoration_page.last_of_four_175).to_be_visible()


def test_decoration_page_has_specific_static_text(set_up) -> None:
    # Given
    page = set_up
    home_page = HomePage(page)
    home_page.decoration.click()

    # When
    decoration_page = DecorationPage(page)

    # Then
    expect(decoration_page.free_delivery_pld).to_be_visible()
    expect(decoration_page.free_design).to_be_visible()
    expect(decoration_page.decoration_contacts).to_be_visible()


def test_learn_more_is_active(set_up) -> None:
    # Given
    page = set_up
    home_page = HomePage(page)
    home_page.decoration.click()

    # When
    decoration_page = DecorationPage(page)

    # Then
    expect(decoration_page.learn_more).to_be_enabled()


def test_learn_more_redirect_correct(set_up) -> None:
    # Given
    page = set_up
    home_page = HomePage(page)
    home_page.decoration.click()
    decoration_page = DecorationPage(page)

    # When
    decoration_page.learn_more.click()

    # Then
    expect(page.get_by_role("heading", name="Принтер – Технология")).to_be_visible()


def test_projects_button_is_active(set_up) -> None:
    # Given
    page = set_up
    home_page = HomePage(page)
    home_page.decoration.click()

    # When
    decoration_page = DecorationPage(page)

    # Then
    expect(decoration_page.projects_button).to_be_enabled()


def test_projects_button_redirect_correct(set_up) -> None:
    # Given
    page = set_up
    home_page = HomePage(page)
    home_page.decoration.click()
    decoration_page = DecorationPage(page)

    # When
    decoration_page.projects_button.click()

    # Then
    expect(page.locator(text="Произведение на изкуството върху стена")).to_be_visible()
    expect(page.locator(text="Генерирана картина върху фотохартия")).to_be_visible()


