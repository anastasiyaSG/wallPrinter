class HomePage:
    def __init__(self, page):

        self.container_generator_empty = page.frame_locator("#picasso-container iframe").get_by_text(
            "Хей, все още нямаш нищо генерирано, опитай от полето по-долу.")
        self.logo = page.get_by_label("WPL")
        self.search_field = page.get_by_placeholder("Търсете всичко тук...")
        self.input_field = page.frame_locator("#picasso-container iframe").get_by_text("Какво искате да ви нарисуваме?")
        self.generate_product_button = page.get_by_text("Създай продукт")

    #links
        self.learn_more = page.get_by_role("link", name="Научете повече")
        self.shop = page.get_by_role("link", name="Магазин")
        self.projects = page.get_by_role("link", name="Проекти")
        self.prices = page.get_by_role("link", name="Цени")
        self.contacts = page.get_by_role("link", name="Контакти")
        self.profile = page.get_by_role("link", name="Вход")
        self.cart = page.get_by_role("link", name="Количка")




