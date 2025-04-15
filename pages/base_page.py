class BasePage:
    def __init__(self, page):
        self.page = page

    def open_page(self, link):
        self.page.goto(link)