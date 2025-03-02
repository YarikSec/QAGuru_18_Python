import datetime

from homework_9.Part3.model.application_manager import ApplicationManager
from homework_9.Part3.data.users import User, Gender, Hobbies

def test_practice_form_register():
    app = ApplicationManager()
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

    # WHEN
    app.practice_form_page.open()
    app.practice_form_page.register(student)

    # THEN
    app.practice_form_page.should_have_registered(student)