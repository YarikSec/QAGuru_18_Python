from homework_9.Part1.pages.practice_form_page import PracticeFormPage

def test_practice_form():
    practice_form = PracticeFormPage()
    
    # WHEN
    (
        practice_form.open()
            .fill_personal_info(
                first_name='Ivan',
                last_name='Ivanov',
                email='ivan@example.com',
                phone='1234567890'
            )
            .set_date_of_birth(month='1', year='1990', day='05')
            .fill_subjects('Maths', 'English')
            .set_hobbies('Sports', 'Music')
            .upload_picture('test.jpg')
            .set_current_address('Санкт-Петербург')
            .select_state('NCR')
            .select_city('Delhi')
            .submit()
    )

    # THEN
    practice_form.should_have_registered(
        full_name='Ivan Ivanov',
        email='ivan@example.com',
        gender='Male',
        phone='1234567890',
        date_of_birth='05 February,1990',
        subject='Maths, English',
        hobbies='Sports, Music',
        avatar='test.jpg',
        current_address='Санкт-Петербург',
        city='NCR Delhi'
    )