import pytest
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

from pages.sbis_page import SbisPage
from pages.sbis_contacts_page import SbisContactsPage
from pages.tensor_page import TensorPage
from pages.tensor_about_page import TensorAboutPage

def test_1(browser):

	sbis_page = SbisPage(browser)
	browser.get('https://sbis.ru/')
	browser.fullscreen_window()

	old_url = browser.current_url

	sbis_page.click_contacts_button()

	time.sleep(3)

	sbis_contacts_page = SbisContactsPage(browser)
	sbis_contacts_page.click_tensor_button()

	window_after = browser.window_handles[1]
	browser.switch_to.window(window_after)

	time.sleep(3)

	tensor_page = TensorPage(browser)
	tensor_page.scrolling()

	try: 
		block = tensor_page.block()
		assert block.is_displayed(), "Блок не найден." 
		
	except NoSuchElementException:  
		assert False, "Блок не найден." 

	tensor_page.click_detail_button()


	WebDriverWait(browser, 10).until(lambda driver: browser.current_url != old_url)
	new_url1 = browser.current_url

	assert new_url1 == "https://tensor.ru/about"

	tensor_about_page = TensorAboutPage(browser)
	tensor_about_page.scrolling()

	size1 = tensor_about_page.image1()
	size2 = tensor_about_page.image2()
	size3 = tensor_about_page.image3()
	size4 = tensor_about_page.image4()

	width1 = size1['width']
	neight1 = size1['height']

	width2 = size2['width']
	neight2 = size2['height']

	width3 = size3['width']
	neight3 = size3['height']


	width4 = size4['width']
	neight4 = size4['height']

	assert width1 == width2 and width1 == width3 and width1 == width4
	assert neight1 == neight2 and neight1 == neight3 and neight1 == neight4
	


