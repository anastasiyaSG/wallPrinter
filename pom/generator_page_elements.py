class GeneratorPage:
    def __init__(self, page):
        self.container_generator_empty = page.frame_locator("#picasso-container iframe").get_by_role("img", name="Празно платно")
        self.send_text_field = page.locator("")
