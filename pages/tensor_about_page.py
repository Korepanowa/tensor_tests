from selenium.webdriver.common.by import By

class TensorAboutPage:
    work = (By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[1]/h2")
    find_image1 = (By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/div[1]/a/div[1]/img")
    find_image2 = (By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/div[2]/a/div[1]/img")
    find_image3 = (By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/div[3]/a/div[1]/img")
    find_image4 = (By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/div[4]/a/div[1]/img")
    
    def __init__(self, driver):

        self.driver = driver

    def scrolling(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(*self.work))

    def image1(self):
        image1 = self.driver.find_element(*self.find_image1)
        size1 = image1.size
        return size1

    def image2(self):
        image2 = self.driver.find_element(*self.find_image2)
        size2 = image2.size
        return size2

    def image3(self):
        image3 = self.driver.find_element(*self.find_image3)
        size3 = image3.size
        return size3

    def image4(self):
        image4 = self.driver.find_element(*self.find_image4)
        size4 = image4.size
        return size4