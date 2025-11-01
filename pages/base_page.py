class BasePage:
    def __init__(self, page):
        self.page = page

    def click(self, selector: str):
        self.page.wait_for_selector(selector)
        self.page.click(selector)

    def enter(self, selector: str, text: str):
        self.page.wait_for_selector(selector)
        self.page.fill(selector, text)

    def get_text(self, selector: str) -> str:
        self.page.wait_for_selector(selector)
        return self.page.inner_text(selector)
    
    def get_attribute(self, selector: str, attribute_name: str) -> str:
        self.page.wait_for_selector(selector)
        return self.page.get_attribute(selector, attribute_name)

    def is_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)
    
    def is_enabled(self, selector: str) -> bool:
        self.page.wait_for_selector(selector)
        return self.page.is_enabled(selector)

    def is_checked(self, selector: str) -> bool:
        self.page.wait_for_selector(selector)
        return self.page.is_checked(selector)

    def get_page_title(self) -> str:
        return self.page.title()

    def get_current_url(self) -> str:
        return self.page.url