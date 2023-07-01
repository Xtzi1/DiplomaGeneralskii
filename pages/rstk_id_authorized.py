from pages.base import WebPage
from pages.elements import WebElement


class IdAuthorizedPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/account_b2c/page?state=' \
              'd14f05ff-b47a-45b5-a862-4799dcdf6d62&client_id=account_b2c#/'
        super().__init__(web_driver, url)

    logout_btn = WebElement(id="logout-btn")

    # заголовок с текстом "Учетные данные"
    h3 = WebElement(css_selector='div#app > main > div > div:nth-of-type(2) > div > h3')

    edit_name_btn = WebElement(id="user_contacts_edit")

    first_name_input = WebElement(id="user_firstname")

    last_name_input = WebElement(id="user_lastname")

    fathers_name_input = WebElement(id="user_patronymic")

    save_btn = WebElement(css_selector='button#user_contacts_editor_save') #id="user_contacts_editor_save") #button#user_contacts_editor_save

    # тайтл с ФИО на странице
    h2 = WebElement(xpath='//*[@id="app"]/main/div/div[2]/div[1]/div[1]/div[1]/h2')

    logo_btn = WebElement(css_selector='header#app-header > div > div > a > svg')

    # region
    edit_region = WebElement(id="region_action")

    regions = WebElement(css_selector='div#app > main > div > div:nth-of-type(2) > div > div:nth-of-type(2) > div:nth-of-type(5) > div > div > div > div > div > div > div:nth-of-type(2) > svg')

    region1 = WebElement(css_selector='div#app > main > div > div:nth-of-type(2) > div > div:nth-of-type(2) > div:nth-of-type(5) > div > div > div > div > div > div > div:nth-of-type(2) > svg')

    save_region_btn = WebElement(css_selector='div#app > main > div > div:nth-of-type(2) > div > div:nth-of-type(2) > div:nth-of-type(5) > div > div > div > button')

    actual_region_on_page = WebElement(css_selector='div#app > main > div > div:nth-of-type(2) > div > div:nth-of-type(2) > div:nth-of-type(4) > div > span:nth-of-type(2) > span')

    region_close = WebElement(css_selector='div#app > main > div > div:nth-of-type(2) > div > div:nth-of-type(2) > div:nth-of-type(5) > div > div > button')

    history_btn = WebElement(css_selector='div#app > main > div > div:nth-of-type(2) > div:nth-of-type(2) > div > button')

    history_back_link = WebElement(css_selector='div#app > main > div > div > a > div > button ')

    lk_btn = WebElement(id="lk-btn")

    call_menu = WebElement(css_selector='div#root > div > div > div > div > div > div:nth-of-type(3) > div:nth-of-type(2) > h2')

    go_to_edit_data = WebElement(css_selector='html > body > div:nth-of-type(5) > div > div:nth-of-type(2) > div > div > div > div > div > svg')
