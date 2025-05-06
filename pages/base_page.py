class BasePage:
    def __init__(self, page):
        self.page = page

    def open_page(self, link):
        self.page.goto(link)

    def get_url(self):
        return self.page.url

    def reload_page(self):
        self.page.reload()

    def get_back(self):
        self.page.go_back()
