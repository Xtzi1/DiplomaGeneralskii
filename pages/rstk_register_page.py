from pages.base import WebPage
from pages.elements import WebElement


class RegisterPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions' \
              '/registration?client_id=account_b2c&tab_id=SY3VIzI7fB0'
        super().__init__(web_driver, url)

    first_name_input = WebElement(name='firstName')

    last_name_input = WebElement(name='lastName')

    email_input = WebElement(id="address")

    password_input = WebElement(id="password")

    password2_input = WebElement(id="password-confirm")

    register_btn = WebElement(name="register")
