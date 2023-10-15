class TopProducts:
    def __init__(self, page, amount):
        self.top_products = page.get_by_role("link", name="Топ Продукти ")
        self.sort_by_date = page.locator("span").filter(has_text="Sort by Дата").nth(1)
        self.sort_by_price = page.get_by_role("link", name="Sort by Цена")
        self.sort_by_rate = page.get_by_role("link", name="Sort by Рейтинг")
        self.sort_by_name = page.get_by_role("link", name="Sort by Име")
        self.sort_by_popularity = page.get_by_role("link", name="Sort by Популярност")
        self.sort_desc = page.get_by_label("Descending order")
        self.sort_asc = page.get_by_label("Ascending order")
        self.amount = page.get_by_role("link", name=f"Show {amount} Products")
        self.view_list = page.get_by_label("View as list")
        self.view_grid = page.get_by_label("View as grid")

        self.for_us = page.get_by_text("Стенен печат Блог За нас Общи условия Политика за поверителност")
        self.redirected_for_us = page.get_by_role("heading", name="Запознайте се с нашия “Дрийм Тийм”")

        self.wallpaper = page.get_by_text("Картини Декорация за стени Фототапет Декорация за дома Дкоративни тапети")
        self.redirected_wallpaper = page.get_by_role("heading", name="Фототапет или стенен печат?")

        self.product_bear = page.get_by_role("link", name="“Мечка сред кайсиевите градини”")
