import pytest
from pages.rstk_auth_page import AuthPage
from pages.rstk_register_page import RegisterPage
from pages.rstk_recover_pass_page import RecoverPage
from pages.rstk_id_authorized import IdAuthorizedPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# !!!ОСТОРОЖНО!!!
# При запуске всех тестов может сработать защита ростелекома, что приведет к блокировке IP
# Команда для запуска тестов
# python -m pytest -v tests/tests_rostelekom.py
# Все тесты рабочие, ничего не должно падать
# Если падает, вероятно срабатывает защита ростелекома

@pytest.fixture(scope="session")
def driver(request):

    options = Options()
    # options.add_argument("--headless")  # Запустить хром в фоновом режиме
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def prepair_data(driver):

    auth_page = AuthPage(driver)
    page_id_authorized = IdAuthorizedPage(driver)

    auth_page.login_input.send_keys('masalan157@fulwark.com')
    auth_page.password_input.send_keys('Test123e')
    auth_page.enter_btn.click()

    yield

    page_id_authorized.logo_btn.click()
    page_id_authorized.logout_btn.click()


#1
def test_auth_page_elements_presence(driver):
    """Проверка наличия элементов на странице авторизации"""

    page = AuthPage(driver)

    assert page.telephone_btn.is_presented()
    assert page.email_btn.is_presented()
    assert page.login_btn.is_presented()
    assert page.ls_btn.is_presented()
    assert page.login_input.is_presented()
    assert page.password_input.is_presented()
    assert page.forgot_password_btn.is_presented()
    assert page.enter_btn.is_presented()
    assert page.register_btn.is_presented()
    assert page.remember_me.is_presented()
    assert page.section_page_left.is_presented()


#2
def test_register_page_elements_presence(driver):
    """Проверка наличия элементов на странице регистрации"""

    auth_page = AuthPage(driver)
    page = RegisterPage(driver)

    auth_page.register_btn.click()

    assert page.first_name_input.is_presented()
    assert page.last_name_input.is_presented()
    assert page.email_input.is_presented()
    assert page.password_input.is_presented()
    assert page.password2_input.is_presented()
    assert page.register_btn.is_presented()


#3
def test_recover_pass_page_elements_presence(driver):
    """Проверка наличия элементов на странице восстановления пароля"""

    auth_page = AuthPage(driver)
    page = RecoverPage(driver)

    auth_page.forgot_password_btn.click()

    assert page.telephone_btn.is_presented()
    assert page.email_btn.is_presented()
    assert page.login_btn.is_presented()
    assert page.ls_btn.is_presented()
    assert page.login_input.is_presented()
    assert page.captcha_input.is_presented()
    assert page.next_btn.is_presented()
    assert page.go_back_btn.is_presented()


#4 #5
@pytest.mark.parametrize('login, password', [
    ('norine3287@fulwark.com', 'Test123e'),
    ('963 788-10-07', 'Test123e')
])
def test_authorization_with_email_and_logout(driver, login, password):
    """Проверка логина с валидными данными и логаута, параметры: email, телефон"""

    page = AuthPage(driver)
    page_id_authorized = IdAuthorizedPage(driver)

    page.login_input.send_keys(login)
    page.password_input.send_keys(password)
    page.enter_btn.click()

    h3_text = page_id_authorized.h3.get_text()
    msg = 'Wrong text in search "{}"'.format(h3_text)
    assert 'учетные данные' in h3_text.lower(), msg

    page_id_authorized.logout_btn.click()
    assert page.login_btn


#6
@pytest.mark.usefixtures("prepair_data")
def test_edit_name(driver):
    """Проверка редактирования имени и отображения в личном кабинете"""

    page_id_authorized = IdAuthorizedPage(driver)
    first_name = 'Тестимени'

    page_id_authorized.edit_name_btn.click()
    page_id_authorized.first_name_input.send_keys(first_name)
    assert page_id_authorized.save_btn.is_clickable()

    page_id_authorized.save_btn.click()
    page_id_authorized.refresh()
    h2_text = page_id_authorized.h2.get_text()
    assert first_name in h2_text

    # Возвращаем как было
    page_id_authorized.edit_name_btn.click()
    page_id_authorized.first_name_input.send_keys('Имя')
    page_id_authorized.save_btn.is_clickable()
    page_id_authorized.save_btn.click()


#7
@pytest.mark.usefixtures("prepair_data")
def test_edit_name(driver):
    """Проверка редактирования фамилии и отображения в личном кабинете"""

    page_id_authorized = IdAuthorizedPage(driver)
    last_name = 'Тестфамилии'

    page_id_authorized.edit_name_btn.click()
    page_id_authorized.last_name_input.send_keys(last_name)
    assert page_id_authorized.save_btn.is_clickable()

    page_id_authorized.save_btn.click()
    page_id_authorized.refresh()
    h2_text = page_id_authorized.h2.get_text()
    assert last_name in h2_text

    # Возвращаем как было
    page_id_authorized.edit_name_btn.click()
    page_id_authorized.last_name_input.send_keys('Фамилия')
    page_id_authorized.save_btn.is_clickable()
    page_id_authorized.save_btn.click()


#8
@pytest.mark.usefixtures("prepair_data")
def test_edit_patronymic(driver):
    """Проверка добавления отчества и отображения в личном кабинете"""

    page_id_authorized = IdAuthorizedPage(driver)
    fathers_name = 'Отчество'

    page_id_authorized.edit_name_btn.click()
    page_id_authorized.fathers_name_input.send_keys(fathers_name)

    assert page_id_authorized.save_btn.is_clickable()

    page_id_authorized.save_btn.click()
    page_id_authorized.refresh()
    h2_text = page_id_authorized.h2.get_text()

    assert fathers_name in h2_text


#9
@pytest.mark.usefixtures("prepair_data")
def test_delete_patronymic(driver):
    """Проверка удаления отчества"""

    page_id_authorized = IdAuthorizedPage(driver)

    # Добавляем отчество
    page_id_authorized.edit_name_btn.click()
    page_id_authorized.fathers_name_input.send_keys('Некоеотчество')
    page_id_authorized.save_btn.is_clickable()
    page_id_authorized.save_btn.click()

    # Удаляем отчество
    page_id_authorized.edit_name_btn.click()
    page_id_authorized.fathers_name_input.clear_text()

    assert page_id_authorized.save_btn.is_clickable()
    page_id_authorized.save_btn.click()


#10
def test_error_massage_if_invalid_pass(driver):
    """Проверка что нельзя авторизоваться с невалидными данными и выводится ожидаемый текст ошибки"""

    page = AuthPage(driver)

    page.login_input.send_keys('masalan157@fulwark.com')
    page.password_input.send_keys('Terrsef21')
    page.enter_btn.click()

    assert page.error_massage.is_visible()
    assert 'Неверный логин или пароль' in page.error_massage.get_text()


#11
@pytest.mark.usefixtures("prepair_data")
def test_edit_region(driver):
    """Проверка кликабельности кнопок в редактировании региона
    и наличие региона на странице личного кабинета"""

    page_id_authorized = IdAuthorizedPage(driver)

    page_id_authorized.edit_region.click()
    page_id_authorized.regions.is_presented()

    assert not page_id_authorized.save_region_btn.is_clickable()
    page_id_authorized.region_close.click()
    assert page_id_authorized.actual_region_on_page.is_presented()


#12
@pytest.mark.usefixtures("prepair_data")
def test_looking_history_and_back(driver):
    """Проверка просмотра истории действий и возвращения на страницу ЛК"""

    page_id_authorized = IdAuthorizedPage(driver)

    assert page_id_authorized.history_btn.is_presented()
    page_id_authorized.history_btn.click()
    assert page_id_authorized.history_back_link
    page_id_authorized.history_back_link.click()
    assert page_id_authorized.history_btn.is_presented()


#13
@pytest.mark.usefixtures("prepair_data")
def test_go_to_lk_and_back(driver):
    """Проверка перехода в личный кабинет и обратно в личные данные"""

    page_id_authorized = IdAuthorizedPage(driver)

    page_id_authorized.lk_btn.click()
    page_id_authorized.call_menu.click()
    page_id_authorized.go_to_edit_data.click()

    h3_text = page_id_authorized.h3.get_text()
    assert 'учетные данные' in h3_text.lower()


#14
def test_error_massage_if_no_data(driver):
    """Проверка что если попытаться авторизоваться с пустыми полями, выводится ошибка"""

    page = AuthPage(driver)

    page.enter_btn.click()

    assert page.error_massage_empty_data.is_presented()
    assert page.error_massage_empty_data.is_visible()
    assert 'Введите номер телефона' in page.error_massage_empty_data.get_text()


#15
def test_vk_button_is_presented(driver):
    """Проверка что кнопкa VK.COM доступна"""

    page = AuthPage(driver)

    assert page.vk_btn.is_presented()
    assert page.vk_btn.is_clickable()
    assert page.vk_btn.is_visible()


#16
def test_ok_button_is_presented(driver):
    """Проверка что кнопкa OK.RU доступна"""

    page = AuthPage(driver)

    assert page.ok_btn.is_presented()
    assert page.ok_btn.is_clickable()
    assert page.ok_btn.is_visible()


#17
def test_mailru_button_is_presented(driver):
    """Проверка что кнопкa MAIL.RU доступна"""

    page = AuthPage(driver)

    assert page.mailru_btn.is_presented()
    assert page.mailru_btn.is_clickable()
    assert page.mailru_btn.is_visible()


#18
def test_socials_are_presented(driver):
    """Проверка что кнопкa YANDEX доступна"""

    page = AuthPage(driver)

    assert page.yandex_btn.is_presented()
    assert page.yandex_btn.is_clickable()
    assert page.yandex_btn.is_visible()


#19
def test_error_massage_if_empty_telephone_in_recovery_pass(driver):
    """Проверка что если попытаться "Продолжить" восстановление пароля не введя телефон,
    выводится сообщение об ошибке и валидация этого сообщения"""

    auth_page = AuthPage(driver)
    recovery_page = RecoverPage(driver)

    auth_page.forgot_password_btn.click()
    recovery_page.telephone_btn.click()
    recovery_page.next_btn.click()

    assert recovery_page.error_massage.is_presented()
    assert recovery_page.error_massage.is_visible()
    assert 'Введите номер телефона' in recovery_page.error_massage.get_text()


#20
def test_error_massage_if_empty_email_in_recovery_pass(driver):
    """Проверка что если попытаться "Продолжить" восстановление пароля не введя email,
    выводится сообщение об ошибке и валидация этого сообщения"""

    auth_page = AuthPage(driver)
    recovery_page = RecoverPage(driver)

    auth_page.forgot_password_btn.click()
    recovery_page.email_btn.click()
    recovery_page.next_btn.click()

    assert recovery_page.error_massage.is_presented()
    assert recovery_page.error_massage.is_visible()
    assert 'Введите адрес, указанный при регистрации' in recovery_page.error_massage.get_text()


#21
def test_error_message_if_empty_captcha_in_recovery_pass(driver):
    """Проверка что если попытаться "Продолжить" восстановления пароля с валидным email не введя капчу,
    выводится сообщение об ошибке и валидация этого сообщения"""

    auth_page = AuthPage(driver)
    recovery_page = RecoverPage(driver)

    auth_page.forgot_password_btn.click()
    recovery_page.email_btn.click()
    recovery_page.login_input.send_keys('norine3287@fulwark.com')
    recovery_page.next_btn.click()

    assert recovery_page.error_massage_no_captcha.is_presented()
    assert recovery_page.error_massage_no_captcha.is_visible()
    assert 'Неверный логин или текст с картинки' in recovery_page.error_massage_no_captcha.get_text()