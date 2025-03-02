from homework_9.Part3.model.application_manager import ApplicationManager

def test_simple_registration_form():
    app = ApplicationManager()
    
    # WHEN
    app.left_panel.open_simple_registration_form()
    
    app.text_box_page.fill_form(
        name='Ivan Ivanov',
        email='ivan@example.com',
        current_address='Санкт-Петербург',
        permanent_address='Москва'
    )
    
    # THEN
    app.text_box_page.should_have_submitted(
        name='Ivan Ivanov',
        email='ivan@example.com',
        current_address='Санкт-Петербург',
        permanent_address='Москва'
    )