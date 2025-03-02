import datetime

from homework_9.Part2.model.pages.practice_form_page import PracticeFormPage
from homework_9.Part2.data.users import User, Gender, Hobbies

def test_practice_form_register():
    student = User(
        first_name='Ivan', 
        last_name='Ivanov', 
        email='ivan@example.com',
        phone='1234567890',
        gender=Gender.MALE,
        date_of_birth=datetime.date(1990, 2, 5),
        subjects='Math',
        hobbies=Hobbies.SPORTS,
        avatar='test.jpg',
        current_address='Санкт-Петербург',  
        state='NCR',
        city='Delhi'
    )
    practice_form = PracticeFormPage()
    practice_form.open()

    # WHEN
    practice_form.register(student)

    # THEN
    practice_form.should_have_registered(student)