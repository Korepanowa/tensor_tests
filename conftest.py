import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


# Создаем фикстуру с областью видимости "function" для создания и закрытия веб-драйвера
@pytest.fixture(scope="function")

def browser():

    
    cService = webdriver.FirefoxService(executable_path = '/home/korens/py1/geckodriver')
    driver = webdriver.Firefox(service = cService)
    driver.implicitly_wait(10)

    yield driver
    
    driver.quit()