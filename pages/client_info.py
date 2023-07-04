
from selenium.webdriver.common.by import By
from base.base_class import Base


class Client_Info(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    first_name = '//*[@id="cart"]/div[2]/input[1]'
    phone = '//*[@id="cart"]/div[2]/input[2]'
    address_2 = '//*[@id="cart"]/div[2]/div[3]/div/div[2]/div'
    address = '//div[@class="ui dropdown shopsel selection"]'
    comment = '//textarea[@class="input"]'
    way_of_payment = '//li[@class="card"]'
    submit_order_button = '//button[@class="submit"]'

    # Getters
    def get_first_name(self):
        return self.driver.find_element(By.XPATH, self.first_name)

    def get_phone(self):
        return self.driver.find_element(By.XPATH, self.phone)

    def get_address(self):
        self.driver.find_element(By.XPATH, self.address).click()
        return self.driver.find_element(By.XPATH, self.address_2)

    def get_comment(self):
        return self.driver.find_element(By.XPATH, self.comment)

    def get_way_of_payment(self):
        return self.driver.find_element(By.XPATH, self.way_of_payment)

    def get_submit_order_button(self):
        return self.driver.find_element(By.XPATH, self.submit_order_button)

    # Actions
    def input_name(self, name):
        self.get_first_name().send_keys(name)
        print("input user name")

    def input_phone(self, phone):
        self.get_phone().send_keys(phone)
        print("input phone number")

    def input_address(self):
        self.get_address().click()
        print("Choose an address")

    def input_comment(self, comment):
        self.get_comment().send_keys(comment)
        print("input comment")

    def input_way_of_payment(self):
        self.get_way_of_payment().click()
        print("Choose way of payment")

    def input_submit_order_button(self):
        self.get_submit_order_button().click()


    #Run methods
    def input_information(self):
        self.input_name("Ivan")  # ввести имя клиента
        self.input_phone("916181-81-41")  # ввести номер телефона клиента
        self.input_address() # выбрать адрес самовывоза
        self.input_comment("C 10.00 - 12.00") # ввести комментарий
        self.input_way_of_payment()  # выбрать способ оплаты "Картой на сайте"
        self.input_submit_order_button() # кнопка


