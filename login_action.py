from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def initialize_driver() :
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://discord.com/login")
    return driver


def login(driver, email, password) :
    driver.implicitly_wait(10)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#uid_7')))
    driver.find_element(By.CSS_SELECTOR, '#uid_7').send_keys(email)
    driver.find_element(By.CSS_SELECTOR, '#uid_9').send_keys(password)
    login_button = driver.find_element(By.CSS_SELECTOR, '.button_b83a05')
    login_button.click()
    WebDriverWait(driver, 20).until(EC.url_contains("channels"))