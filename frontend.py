import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from login_action import initialize_driver, login



@pytest.fixture
def setup():
    driver = initialize_driver()
    yield driver
    driver.quit()


def test_textbox(setup):
    driver = setup
    email = 'moiseenkoalla8@gmail.com'
    password = 'hieveryone123456'

    login(driver, email, password)

    try:
        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.childWrapper_f90abb.acronym_f90abb')))
        element.click()
    except Exception as e:
        print("Элемент для клика не найден или не кликабельный:", e)

    try:
        input_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="textbox"]')))
        assert input_field.is_displayed()
    finally:
        driver.quit()


def test_button_plus(setup):
    driver = setup
    email = 'moiseenkoalla8@gmail.com'
    password = 'hieveryone123456'

    login(driver, email, password)

    try:
        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.childWrapper_f90abb.acronym_f90abb')))
        element.click()


        attach_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.attachButtonPlus_f298d4')))
        attach_button.click()
        print("Кнопка click css=.attachButtonPlus_f298d4 успешно нажата.")

    except Exception as e:
        print("Ошибка:", e)


def test_create_message(setup):
    driver = setup
    email = 'moiseenkoalla8@gmail.com'
    password = 'hieveryone123456'

    login(driver, email, password)

    try:
        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.childWrapper_f90abb.acronym_f90abb')))
        element.click()
    except Exception as e:
        print("Элемент для клика не найден или не кликабельный:", e)

    try:
        input_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="textbox"]')))
        assert input_field.is_displayed()

        input_field.send_keys("Тест 123345")
        input_field.send_keys(Keys.RETURN)

    finally:
        driver.quit()

def test_emoji(setup):
    driver = setup
    email = 'moiseenkoalla8@gmail.com'
    password = 'hieveryone123456'

    login(driver, email, password)

    try:
        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.childWrapper_f90abb.acronym_f90abb')))
        element.click()
    except Exception as e:
        print("Элемент для клика не найден или не кликабельный:", e)

    try:
        svg_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.contents_dd4f85 > svg'))
        )
        assert svg_element.is_displayed()
        print("Элемент присутствует на странице.")
    except Exception as e:
        print("Элемент не найден на странице:", e)

    driver.quit()











