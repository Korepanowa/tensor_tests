from selenium.webdriver.common.by import By

class SbisDownloadPage:
    download = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div/a")

    def __init__(self, driver):
        self.driver = driver

    def click_download_button(self):
        self.driver.find_element(*self.download).click()

    def text_download(self):
        text_download = self.driver.find_element(*self.download).text
        return text_download