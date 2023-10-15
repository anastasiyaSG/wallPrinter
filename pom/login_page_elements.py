class LoginPage:
    def __init__(self, page):
        self.login_google_account = page.get_by_text("Влез с Гугъл")
        self.my_account = page.get_by_text("anastasiya.qa.2023")
        self.successful = page.get_by_text("Successfully login with anastasiya.qa.2023")

        # TO DO