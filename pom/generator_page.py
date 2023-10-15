class GeneratorPage:
    def __init__(self, page):

        self.generator_container = page.frame_locator("#picasso-container iframe").locator("html")
        self.generator_not_created_text = page.frame_locator("#picasso-container iframe").get_by_text(
            "Хей, все още нямаш нищо генерирано, опитай от полето по-долу.")
        self.input_field = page.frame_locator("#picasso-container iframe").get_by_text("Какво искате да ви нарисуваме?")
        self.generate_product_button = page.get_by_text("Създай продукт")
