from selene import browser, have, command
from pathlib import Path

from homework_9.Part2.data.users import User
from homework_9.Part2.model import resource


class PracticeFormPage:
    def __init__(self):
        self.base_path = Path(__file__).parent.parent / 'resources'

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.driver.execute_script("$('#fixedban').remove()") # Для удаления баннеров
        browser.driver.execute_script("$('footer').remove()")    # Для удаления баннеров
        return self

    def register(self, user: User):
        # заполнение полей начальных
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        browser.element(f'[name=gender][value={user.gender.value}]').perform(command.js.click)
        browser.element('#userNumber').type(user.phone)

        # дата рождения
        browser.element('#dateOfBirthInput').click()
        (browser.element('.react-datepicker__month-select').click().all('option').
         element_by(have.text(user.formatted_month())).click())
        (browser.element('.react-datepicker__year-select').click().all('option').
         element_by(have.text(user.formatted_year())).click())
        browser.element(f'.react-datepicker__day--0{user.formatted_day()}').click()

        # занятия
        if user.subjects:
            browser.element('#subjectsInput').type(user.subjects).press_enter()

        # хобби
        if user.hobbies:
            browser.all('[for^=hobbies-checkbox]').element_by(have.text(user.hobbies.value)).click() 

        # загрузка фото
        if user.avatar:
            browser.element('#uploadPicture').set_value(resource.path(user.avatar))

        # адрес
        if user.current_address:
            browser.element('#currentAddress').type(user.current_address)

        # город
        if user.state:
            browser.element('#state').click().all('[id^=react-select-3-option]').element_by(have.text(user.state)).click()
        
        if user.city:
            browser.element('#city').click().all('[id^=react-select-4-option]').element_by(have.text(user.city)).click()

        # отправка
        browser.element('#submit').click()

    
    def should_have_registered(self, user: User):
        browser.element('.modal-title').should(have.text('Thanks for submitting the form'))

        results = browser.element('.table').all('td').even

        results.should(have.texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender.value,
            user.phone,
            f'{user.formatted_day()} {user.formatted_month()},{user.formatted_year()}'
        ))

        # Проверка необязательных полей
        if user.subjects:
            results.element_by(have.text(user.subjects))
        
        if user.hobbies:
            results.element_by(have.text(user.hobbies.value))
        
        if user.current_address:
            results.element_by(have.text(user.current_address))
        
        if user.state and user.city:
            results.element_by(have.text(f'{user.state} {user.city}'))

        return self