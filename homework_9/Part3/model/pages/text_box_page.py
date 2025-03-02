from selene import browser, be, have

class TextBoxPage:
    def fill_form(self, full_name, email, current_address, permanent_address):
        browser.element('#userName').type(full_name)
        browser.element('#userEmail').type(email)
        browser.element('#currentAddress').type(current_address)
        browser.element('#permanentAddress').type(permanent_address)
        browser.element('#submit').click()
        
    def should_have_submitted(self, full_name, email, current_address, permanent_address):
        browser.element('#output').should(have.text(full_name))
        browser.element('#output').should(have.text(email))
        browser.element('#output').should(have.text(current_address))
        browser.element('#output').should(have.text(permanent_address))