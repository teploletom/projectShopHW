from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base.base_class import Base

class Payment_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Run methods
    def payment(self):
        print("Payment order page")
        y = self.get_current_url()
