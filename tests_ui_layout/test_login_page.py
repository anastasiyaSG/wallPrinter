from playwright.sync_api import expect

from pom.home_page_elements import HomePage
from pom.login_page_elements import LoginPage


def test_login_with_google(set_up) -> None:
    # Given
    page = set_up
    page = HomePage(page)
    # When
    page.profile.click()
    page = LoginPage(page)
    page.login_google_account.click()
    page.my_account.click()

    # Then
    expect(page.successful).to_be_visible()

# TO DO