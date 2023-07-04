import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    add_product_1 = '/html/body/main/section[2]/section[1]/section/figure[3]/button'
    add_product_2 = '/html/body/main/section[2]/section[1]/section/figure[4]/button'
    #filter_product_1 = '/html/body/div[3]/div/div/div[2]/div[3]/div[1]'
    filter_product_1 = '//div[@class="item s40"]'
    filter_product_2 = '//div[@class="current pos1"]'
    add_to_cart_button = '//button[@class="tocart"]'
    s40_tradicionoe = '//*[@id="cart"]/div[2]/div[1]/div[2]/p'
    s30_tonkoe = '//*[@id="cart"]/div[2]/div[2]/div[2]/p'

    # Getters
    def get_add_product1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_product_1)))

    def get_add_product2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_product_2)))

    def set_filter_product1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_product_1)))

    def set_filter_product2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_product_2)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    # Actions
    def click_choose_product1(self):  # кликнуть на кнопку Выбрать product1
        self.get_add_product1().click()
        print("Click 'Выбрать' product 1")
    def click_choose_product2(self):  # кликнуть на кнопку Выбрать product2
        self.get_add_product2().click()
        print("Click 'Выбрать' product 2")
    def click_filter_product1(self):  # выбрать филтер размер 40 для product1
        self.set_filter_product1().click()
        print("Click filter for product 1")
    def click_filter_product2(self):  # выбрать филтер Тонкое тесто для product2
        self.set_filter_product2().click()
        print("Click filter for product 2")
    def click_add_to_cart(self):      # кликнуть на кнопку Добавить в корзину
        self.get_add_to_cart_button().click()
        print("Press add to cart button")

    #Run methods
    def select_products(self):
        self.click_choose_product1()
        self.click_filter_product1()
        self.click_add_to_cart()
        self.click_choose_product2()
        self.click_filter_product2()
        self.click_add_to_cart()
