import time

import pytest
from selenium import webdriver
from pages.cart_page import Cart_page
from pages.client_info import Client_Info
#from pages.finish_page import Finish_page
from pages.login_page import LoginP
from pages.main_page import Main_page
from pages.payment_page import Payment_page


class Test_1():
    def test_buy_product_1(self, set_up):
        driver = webdriver.Chrome()

        login = LoginP(driver)#экземпляр класса логирования
        login.authorization() #вызов метода авторизации на сайте

        mp = Main_page(driver) #экземпляр класса Main Page
        mp.select_products() # Add to cart продукта на главной странице

        cp = Cart_page(driver) #экземпляр класса Cart_page
        cp.click_cart_button() #метод экземпляра класса Cart_page

        cip = Client_Info(driver) #экземпляр класса Client_Info
        cip.input_information()
        time.sleep(10)

        p = Payment_page(driver) #экземпляр класса Payment_page
        p.payment()

        driver.quit()