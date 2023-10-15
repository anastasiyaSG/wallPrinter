import pytest
from playwright.sync_api import expect

from pom.projects_page_elements import ProjectPage


@pytest.mark.smoke()
def test_existing_most_important_projects(set_up) -> None:
    page = set_up

    project_page = ProjectPage(page)

    expect(project_page.print_from_customer_project).to_be_visible()
    expect(project_page.photo_paper).to_be_visible()
    expect(project_page.wallpapers).to_be_visible()
    expect(project_page.print_from_ai).to_be_visible()
    expect(project_page.print_from_photo).to_be_visible()


    # TO DO