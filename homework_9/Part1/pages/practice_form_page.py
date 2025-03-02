from selene import browser, have, be
from pathlib import Path

class PracticeFormPage:
    def __init__(self):
        self.base_path = Path(__file__).parent.parent / 'resources'

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.driver.execute_script("$('#fixedban').remove()") # Для удаления баннеров
        browser.driver.execute_script("$('footer').remove()")    # Для удаления баннеров
        return self

    def fill_personal_info(self, first_name, last_name, email, phone):
        browser.element('#firstName').type(first_name)
        browser.element('#lastName').type(last_name)
        browser.element('#userEmail').type(email)
        browser.element('[name=gender][value=Male]+label').click()
        browser.element('#userNumber').type(phone)
        return self

    def set_date_of_birth(self, month, year, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(f'[value="{month}"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'[value="{year}"]').click()
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def fill_subjects(self, *values):
        browser.element('#subjectsInput').type(*values).press_enter()
        return self

    def set_hobbies(self, *values):
        for value in values:
            browser.element(f'[for="hobbies-checkbox-{value}"]').set_true()
        return self

    def upload_picture(self, picture):
        browser.element('#uploadPicture').send_keys(self.base_path / picture)
        return self

    def set_current_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def select_state(self, value):
        browser.element('#state').click()
        browser.element('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()
        return self

    def select_city(self, value):
        browser.element('#city').click()
        browser.element('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()
        return self

    def submit(self):
        browser.element('#submit').press_enter()
        return self
    
    def should_have_registered(self, full_name, email, gender, phone, date_of_birth, subject, hobbies, current_address, city):
        browser.element('.modal-content').should(be.visible)
        browser.element('#example-modal-title').should(have.exact_text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name, 
                email, 
                gender,
                phone, 
                date_of_birth, 
                subject,
                hobbies,
                current_address,
                city
            )
        )