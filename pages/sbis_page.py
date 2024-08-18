from selenium.webdriver.common.by import By

class SbisPage:
    contacts_BUTTON = (By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/a")
    useful = (By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/div[3]/div[3]/h4/span")
    find_download = (By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/div[3]/div[3]/ul/li[8]/a")

    def __init__(self, driver):
        self.driver = driver

    def click_contacts_button(self):
        self.driver.find_element(*self.contacts_BUTTON).click()

    def scrolling(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(*self.useful))

    def click_download_button(self):
        self.driver.find_element(*self.find_download).click()