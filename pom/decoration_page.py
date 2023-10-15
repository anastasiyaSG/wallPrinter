class DecorationPage:
    def __init__(self, page):
        self.last_generated = page.get_by_role("heading", name="Последно генерирани картини от наши потребители")
        self.first_of_four_45 = page.get_by_label("1 / 4").get_by_text("45.00лв.")
        self.first_of_four_175 = page.get_by_label("1 / 4").get_by_text("175.00лв.")
        self.last_of_four_45 = page.get_by_label("4 / 4").get_by_text("45.00лв.")
        self.last_of_four_175 = page.get_by_label("4 / 4").get_by_text("175.00лв.")
        self.free_delivery_pld = page.get_by_role("heading", name="Безплатна доставка за Пловдив !")
        self.free_design = page.get_by_text("Към услугата плучавате безплатен дизайн и дигитална обработка на необходимите из")
        self.learn_more = page.get_by_role("link", name="Научи повече за Директния Стенен Печат")
        self.decoration_contacts = page.get_by_text("Свържете се с нас днес за декорация на стена")
        self.projects_button = page.locator("#post-5").get_by_role("link", name="Проекти")