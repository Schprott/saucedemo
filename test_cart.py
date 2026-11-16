import time
from selenium.webdriver.common.by import By

def test_shopping_cart(browser):
    # Проходим авторизацию
    browser.get("https://www.saucedemo.com/")
    username = browser.find_element(By.ID, 'user-name')
    password = browser.find_element(By.NAME, "password")
    login = browser.find_element(By.CLASS_NAME, "submit-button")
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login.click()

    time.sleep(2)
    # Добавляем товар в корзину
    buy_backpack = browser.find_element(By. ID, 'add-to-cart-sauce-labs-backpack')
    buy_backpack.click()

    # Переходим в корзину
    step_shopping_cart = browser.find_element(By. CLASS_NAME, 'shopping_cart_link')
    step_shopping_cart.click()
    product_name = browser.find_element(By.CLASS_NAME, "inventory_item_name")
    product_price = browser.find_element(By.CLASS_NAME, "inventory_item_price")

    # Проверяем Название товара и стоимость
    assert product_name.text == "Sauce Labs Backpack" and product_price.text == "$29.99"

    browser.quit()