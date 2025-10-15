import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from .base_page import BasePage
from ..locators.locators import FormPageLocators
from ..data.values import FormPageValues
from ..page_factory.component import PageFactory


class FormPage(BasePage):

    def set_name_to_form_page(self):
        with allure.step('Set name'):
            component = PageFactory(self.browser)
            component.input(FormPageLocators.NAME_INPUT).set(FormPageValues.NAME)

    def set_password_to_form_page(self):
        with allure.step('Set password'):
            component = PageFactory(self.browser)
            component.input(FormPageLocators.PASSWORD_INPUT).set(FormPageValues.PASSWORD)

    def choose_drink_to_form_page(self):
        with allure.step('Choose drink'):
            component = PageFactory(self.browser)
            component.checkbox(FormPageLocators.MILK_CHECKBOX).check()
            component.checkbox(FormPageLocators.COFFEE_CHECKBOX).check()

    def choose_color_to_form_page(self):
        with allure.step('Choose color'):
            component = PageFactory(self.browser)
            component.checkbox(FormPageLocators.YELLOW_CHECKBOX).check()

    def choose_select_to_form_page(self):
        with allure.step('Choose select'):
            component = PageFactory(self.browser)
            component.select(FormPageLocators.ELEM_SELECT).select_by_index(FormPageValues.SELECT)

    def set_email_to_form_page(self):
        with allure.step('Set email'):
            component = PageFactory(self.browser)
            component.input(FormPageLocators.EMAIL_INPUT).set(FormPageValues.EMAIL)

    def set_message_to_form_page(self):
        with allure.step('Set message'):
            component = PageFactory(self.browser)
            component.textarea(FormPageLocators.MESSAGE_TEXTAREA).set(self.message_text())

    def click_submit_button_to_form_page(self):
        with allure.step('Click submit button'):
            component = PageFactory(self.browser)
            component.button(FormPageLocators.SUBMIT_BUTTON).click()
            try:
                alert = WebDriverWait(self.browser, 5).until(EC.alert_is_present())
            except UnexpectedAlertPresentException:
                allure.attach(
                    self.browser.get_screenshot_as_png(),
                    name="screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
            assert alert.text == "Message received!", "Текст alert не соответствует Message received!"
            alert.accept()

    def message_text(self):
        elements = self.browser.find_elements(By.XPATH, "//*[@id='feedbackForm']/ul/li")
        names = [el.text.strip() for el in elements]
        count = len(names)
        if count == 0:
            return count

        max_len_tool = max(len(n) for n in names)
        longest_name_idx = (next(i for i, n in enumerate(names) if len(n) == max_len_tool) + 1)
        longest_name_selector = self.browser.find_element(By.XPATH,
                                                          f"//*[@id='feedbackForm']/ul/li[{longest_name_idx}]")
        longest_name = longest_name_selector.text
        message = " ".join(map(str, [count, longest_name]))
        return message
