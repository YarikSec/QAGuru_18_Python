from selene import browser, be, have

class LeftPanel:
    def open(self, category, subcategory):
        browser.element(f'.header-text:text("{category}")').click()
        browser.element(f'.text:text("{subcategory}")').click()
        
    def open_simple_registration_form(self):
        self.open('Elements', 'Text Box')