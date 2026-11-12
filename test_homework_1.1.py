from selenium.webdriver.common.by import By
from confest import browser


def test_locators(browser):
    browser.get("https://www.saucedemo.com/")
    # Основные локаторы + авторизация
    username = browser.find_element(By. ID, 'user-name')
    password = browser.find_element(By. NAME, 'password')
    login = browser.find_element(By. CLASS_NAME, 'submit-button')
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login.click()
    image = browser.find_element(By. TAG_NAME, 'img')

    # Локаторы + XPATH
    all_menu = browser.find_elements(By. ID, 'react-burger-menu-btn')
    all_menu.click()
    catalog_pr_link = browser.find_element(By. PARTIAL_LINK_TEXT, 'dynamic_catalog_sidebar_link')
    catalog_pr_link.click()
    spinner_link_text = browser.find_element(By. LINK_TEXT, 'Spinner')
    onesie_xpath_attribute = browser.find_element(By. XPATH, '//div[@data-test="spinner-item-2-name"]')
    backpack_xpath_text = browser.find_elements(By. XPATH, '//div[@text()="Sauce Labs Backpack"]')
    bike_light_part_attribute = browser.find_elements(By. XPATH, '//div[contains(text(),"Bike Light")]')
    shopping_cart_part_text = browser.find_elements(By. XPATH, '//a[contains(@class,"shopping")]')
    ancestor = browser.find_element(By.XPATH, "//button[@type='button']/ancestor::div")
    descendant = browser.find_element(By.XPATH, "//div[contains(@class, 'inventory_item')]/descendant::button")
    following = browser.find_element(By.XPATH, "//div[contains(@class, 'inventory_item')]/following::button")
    parent = browser.find_element(By.XPATH, "//div[contains(text(), 'A red light')]/parent::*")
    preceding = browser.find_element(By.XPATH, "//div[contains(text(), 'A red light')]/preceding::button")

    buy_backpack = browser.find_elements(By. ID, 'add-to-cart-sauce-labs-backpack')
    buy_backpack.click()
    step_shopping_cart = browser.find_elements(By. CLASS_NAME, 'shopping_cart_link')
    step_shopping_cart.click()
    checkout = browser.find_element(By. ID, 'checkout')
    checkout.click()
    shopping_cart_xpath_search = browser.find_elements(By. XPATH, '//input[@data-test="firstName" and @id="first-name"]')

    # CSS Селекторы
    class_css = browser.find_elements(By. CSS_SELECTOR, ".bm-item")
    classes_css = browser.find_elements(By. CSS_SELECTOR, ".bm-item.menu-item")
    two_class_css = browser.find_elements(By. CSS_SELECTOR, ".bm-item-list .bm-item")
    id_css = browser.find_elements(By. CSS_SELECTOR, "#inventory_sidebar_link")
    tag_css = browser.find_elements(By. CSS_SELECTOR, "div")
    tag_class_css = browser.find_elements(By. CSS_SELECTOR, "div.bm-menu")
    attribute_css = browser.find_elements(By. CSS_SELECTOR, "data-test=inventory-item-price")
    attribute_two_css = browser.find_element(By.CSS_SELECTOR, "[data-test|=inventory]")
    attribute_tree_css = browser.find_element(By.CSS_SELECTOR, "[data-test|=inventory]")
    attribute_four_css = browser.find_element(By.CSS_SELECTOR, "[data-test$=shopping]")
    attribute_five_css = browser.find_element(By.CSS_SELECTOR, "[data-test*=title]")
