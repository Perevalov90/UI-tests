
from playwright.sync_api import Page, expect
import allure

class LoginPage():
    def __init__(self, page: Page):
        self.page = page
        #Локаторы
        self.login_button = page.locator("[data-qa='btn_header_signInOrUp-header-desktop']")
        self.modal_window = page.locator("[data-qa='cart-login-modal-panel']")
        self.email_input = page.get_by_placeholder('Please enter email or mobile number' )
        self.continue_button = page.locator("[data-qa='btn_Continue']")
        self.error_message = page.locator("[data-qa='lbl_email-addressError']")


    @allure.step('Открыть главную страницу')
    def open_base_page(self):
        self.page.goto('https://www.noon.com/egypt-en/', wait_until="domcontentloaded",
        timeout=110000 )
        expect(self.page).to_have_url('https://www.noon.com/egypt-en/')

    @allure.step('Открыть всплывающее меню авторизации')
    def open_login_page(self):
        self.login_button.click()
        expect(self.modal_window).to_be_visible()
        expect(self.email_input).to_have_attribute("placeholder", "Please enter email or mobile number")

    @allure.step('Ввести email')
    def enter_email(self, email=None):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

    @allure.step('Нажать кнопку продолжить')
    def click_button_continue(self):
        self.continue_button.click()

    @allure.step("Проверить, что появилась ошибка 'Invalid email address'")
    def should_see_invalid_email_error(self):
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_have_text("Invalid email address")
