# noinspection SpellCheckingInspection
class ProjectPage:
    def __init__(self, page):
        self.project = page.get_by_role("link", name="Проекти")
        self.wallpapers = page.locator(text = "Произведение на изкуството върху стена")
        self.photo_paper = page.locator(text="Генерирана картина върху фотохартия")
        self.print_from_photo = page.locator(text="Стенен печат върху сандвич панел с изображение от снимка на клиента")
        self.print_from_customer_project = page.locator(text="Проект генериран от клиент")
        self.print_from_ai = page.locator(text="Използваме изкуствен интелект, за да ви помогнем да създадете")
