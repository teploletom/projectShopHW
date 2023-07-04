from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base.base_class import Base

class LoginP(Base):
    url = 'https://tashirpizza.ru/murom'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Run methods
    def authorization(self):
        self.driver.get(self.url)
