

class Base:

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " +get_url)

    #Method get current url
    def assert_word(self, word, result):
        value_word = word.text
        print(value_word)
        assert value_word == result
        print("Products - is appered")

    #Method screenshot
    def get_screenshot(self):
        self.driver.save_screenshot("C:\\Users\\master\\PycharmProjects\\main_projectAlex\\screen\\screentest.jpg")