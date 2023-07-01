from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/' \
              'protocol/openid-connect/auth?client_id=account_' \
              'b2c&redirect_uri=https://b2c.passport.rt.ru/account' \
              '_b2c/login&response_type=code&scope=openid&state=' \
              'd14f05ff-b47a-45b5-a862-4799dcdf6d62&theme&auth_type'
        super().__init__(web_driver, url)

    login_input = WebElement(id="username") #id="username"

    password_input = WebElement(id="password") #id="password"

    enter_btn = WebElement(id="kc-login")

    telephone_btn = WebElement(id="t-btn-tab-phone")

    email_btn = WebElement(id="t-btn-tab-mail")

    login_btn = WebElement(id="t-btn-tab-login")

    ls_btn = WebElement(id="t-btn-tab-ls")

    forgot_password_btn = WebElement(id="forgot_password")

    register_btn = WebElement(id="kc-register")

    remember_me = WebElement(css_selector='section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')

    section_page_left = WebElement(css_selector='section#page-left')

    error_massage = WebElement(id="form-error-message")

    error_massage_empty_data = WebElement(css_selector='section#page-right > div > div > div > form > div > div:nth-of-type(2) > span')

    vk_btn = WebElement(id="oidc_vk")

    ok_btn = WebElement(id="oidc_ok")

    mailru_btn = WebElement(id="oidc_mail")

    yandex_btn = WebElement(id="oidc_ya")