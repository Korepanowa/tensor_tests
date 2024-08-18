from selenium.webdriver.common.by import By

class TensorPage:
    news = (By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[5]/div/div/div[1]/div/p[1]")
    find_block = (By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[5]/div/div/div[1]/div/p[1]")
    find_detail = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')

    def __init__(self, driver):

        self.driver = driver

    def scrolling(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(*self.news))

    def block(self):
        block = self.driver.find_element(*self.find_block)
        return block

    def click_detail_button(self):
        self.driver.find_element(*self.find_detail).click()