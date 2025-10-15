import allure

from .pages.form_page import FormPage


@allure.feature('E2E form page test')
@allure.story('Проверка страницы формы')
@allure.severity('critical')
def test_main(browser):
    link = "https://practice-automation.com/form-fields/"
    page = FormPage(browser, link)
    page.open()
    page.set_name_to_form_page()
    page.set_password_to_form_page()
    page.choose_drink_to_form_page()
    page.choose_color_to_form_page()
    page.choose_select_to_form_page()
    page.set_email_to_form_page()
    page.set_message_to_form_page()
    page.click_submit_button_to_form_page()