import pytest

from pom.top_products_page import TopProducts
from playwright.sync_api import expect


@pytest.mark.smoke()
def adding_top_product_in_cart(set_up) -> None:
    page = set_up
    top_products = TopProducts(page, 30)
    top_products.top_products.click()

    top_products.product_bear.click()
    page.get_by_role("cell", name="Размер", exact=True).click()
    page.get_by_label("Product quantity").click()
    page.get_by_role("button", name="Добавяне в количката").click()

    expect(page.get_by_role("heading", name="Имате 1 Артикул във вашата количка")).to_be_visible()


def has_sorting_options(set_up) -> None:
    page = set_up
    top_products = TopProducts(page, amount=30)

    top_products.top_products.click()

    expect(top_products.sort_by_date).to_be_enabled()
    expect(top_products.sort_by_name).to_be_enabled()
    expect(top_products.sort_by_price).to_be_enabled()
    expect(top_products.sort_by_popularity).to_be_enabled()
    expect(top_products.view_grid).to_be_enabled()
    expect(top_products.view_list).to_be_enabled()


@pytest.mark.parametrize("amount", ["30", "60", "90"])
def show_correct_amount_of_projects(set_up, amount) -> None:
    page = set_up
    top_products = TopProducts(page, amount)
    top_products.top_products.click()

    top_products.amount.click()

    expect(page.locator("span").filter(has_text=f"Show {amount} Products")).to_be_visible()


def for_us_redirected(set_up) -> None:
    page = set_up
    top_products = TopProducts(page, 30)
    top_products.top_products.click()

    top_products.for_us.click()

    expect(top_products.redirected_for_us).to_be_visible()


def wallpaper_redirected(set_up) -> None:
    page = set_up
    top_products = TopProducts(page, 30)
    top_products.top_products.click()

    top_products.wallpaper.click()

    expect(top_products.redirected_wallpaper).to_be_visible()
