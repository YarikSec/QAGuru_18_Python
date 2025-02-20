import os
from selene import browser, have
import pytest

def test_form():
    browser.open("/automation-practice-form")

    browser.driver.execute_script("$('#fixedban').remove()") # Для удаления баннеров
    browser.driver.execute_script("$('footer').remove()")    # Для удаления баннеров

    browser.element('#firstName').type("Ivan")
    browser.element('#lastName').type("Ivanov")
    browser.element('#userEmail').type("ivan@exampe.com")
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type("1234567890")

    # browser.element('#dateOfBirthInput').type("05.02.1990")

    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").element(
        "[value='1']"
    ).click()
    browser.element(".react-datepicker__year-select").element("[value='1990']").click()
    browser.element(".react-datepicker__day--005").click()


    # browser.element('#subjectsInput').type("Computer Science").press_enter()
    browser.element('#subjectsInput').send_keys('Computer Science').press_enter()

    browser.element('[for="hobbies-checkbox-1"]').click()

    browser.element('#uploadPicture').type(os.path.abspath('resources/test.jpg'))

    browser.element('#currentAddress').type('Санкт-Петербург')

    browser.element('#state').click()
    browser.element("#react-select-3-option-0").click()
    browser.element("#city").click()
    browser.element("#react-select-4-option-0").click()

    browser.element("#submit").click()


    browser.element(".table-responsive").wait_until(have.text("HOME"))
    browser.element(".modal-content").should(have.text("Thanks for submitting the form"))
    browser.element(".table-responsive").should(have.text("Ivan Ivanov"))
    browser.element(".table-responsive").should(have.text("ivan@exampe.com"))
    browser.element(".table-responsive").should(have.text("Male"))
    browser.element(".table-responsive").should(have.text("1234567890"))
    browser.element(".table-responsive").should(have.text("05 February,1990"))
    browser.element(".table-responsive").should(have.text("Computer Science"))
    browser.element(".table-responsive").should(have.text("Sports"))
    browser.element(".table-responsive").should(have.text("Санкт-Петербург"))
    browser.element(".table-responsive").should(have.text("NCR Delhi"))