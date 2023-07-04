from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    url = 'https://tashirpizza.ru/mycart'
    press_cart_button = '//button[@class="submit tocheckout"]'
    press_samovivoz = '//li[@class="tab"]'
    s40_tradicionoe = '//*[@id="cart"]/div[2]/div[1]/div[2]/p'
    s30_tonkoe = '//*[@id="cart"]/div[2]/div[2]/div[2]/p'

    # Getters
    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.press_cart_button))).click()

    def get_samovivoz(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.press_samovivoz))).click()

    def check_product1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.s40_tradicionoe))).text

    def check_product2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.s30_tonkoe))).text

    # Actions
    def click_cart_button(self):
        self.driver.get(self.url)
        print("Click cart button")
        tradicionoe_40s = self.check_product1()
        assert tradicionoe_40s == "40см традиционное", "Добавился не тот товар"
        print("Проверен product1")
        tonkoe_30s = self.check_product2()
        assert tonkoe_30s == "30см тонкое", "Добавился не тот товар"
        print("Проверен product2")
        self.get_cart_button()
        print("Click Перейти к оформлению")
        #time.sleep(5)
        self.get_samovivoz()
        print("Click Самовывоз")
