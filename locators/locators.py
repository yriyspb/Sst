from selenium.webdriver.common.by import By


class FormPageLocators():
    NAME_INPUT = (By.ID, "name-input")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    MILK_CHECKBOX = (By.XPATH, " //label[text()='Milk']")
    COFFEE_CHECKBOX = (By.XPATH, "//label[text()='Coffee']")
    YELLOW_CHECKBOX = (By.XPATH, "//label[text()='Yellow']")
    ELEM_SELECT = (By.CSS_SELECTOR, 'select[data-testid="automation"]')
    EMAIL_INPUT = (By.ID, "email")
    MESSAGE_TEXTAREA = (By.ID, "message")
    SUBMIT_BUTTON = (By.ID, "submit-btn")
