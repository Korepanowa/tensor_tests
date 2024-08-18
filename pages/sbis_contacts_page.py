from selenium.webdriver.common.by import By

class SbisContactsPage:
    find_tensor = (By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[1]/div/div/div[2]/div/a")
    find_region1 = (By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span")
    partners_Yekaterinburg = (By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[4]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[2]/div/div/div[1]/div[1]")
    find_regions = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
    changing_region = (By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span/span')
    find_region2 = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
    partners_Kamchatka = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[4]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[2]/div/div/div[1]/div[1]')

    def __init__(self, driver):
        self.driver = driver

    def click_tensor_button(self):
        self.driver.find_element(*self.find_tensor).click()

    def text_region1(self):
        text_region1 = self.driver.find_element(*self.find_region1).text
        return text_region1

    def block(self):
        block = self.driver.find_element(*self.partners_Yekaterinburg)
        return block

    def text_partners_Yekaterinburg(self):
        text_partners_Yekaterinburg = self.driver.find_element(*self.partners_Yekaterinburg).text
        return text_partners_Yekaterinburg

    def click_regions(self):
        self.driver.find_element(*self.find_regions).click()

    def click_changing(self):
        self.driver.find_element(*self.changing_region).click()

    def text_region2(self):
        text_region2 = self.driver.find_element(*self.find_region2).text
        return text_region2

    def text_partners_Kamchatka(self):
        text_partners_Kamchatka = self.driver.find_element(*self.partners_Kamchatka).text
        return text_partners_Kamchatka