from pages.base import WebPage
from pages.elements import WebElement


class RecoverPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions' \
              '/registration?client_id=account_b2c&tab_id=SY3VIzI7fB0'
        super().__init__(web_driver, url)

    telephone_btn = WebElement(id="t-btn-tab-phone")

    email_btn = WebElement(id="t-btn-tab-mail")

    login_btn = WebElement(id="t-btn-tab-login")

    ls_btn = WebElement(id="t-btn-tab-ls")

    login_input = WebElement(id="username")

    captcha_input = WebElement(id="captcha")

    next_btn = WebElement(id="reset")

    go_back_btn = WebElement(id="reset-back")

    error_massage = WebElement(css_selector='section#page-right > div > div > div > form > div > div:nth-of-type(2) > span')

    error_massage_no_captcha = WebElement(id="form-error-message")