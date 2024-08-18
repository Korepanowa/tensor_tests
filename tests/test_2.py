import pytest
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

from pages.sbis_page import SbisPage
from pages.sbis_contacts_page import SbisContactsPage

def test_2(browser):

	sbis_page = SbisPage(browser)
	browser.get('https://sbis.ru/')
	browser.fullscreen_window()

	old_url = browser.current_url

	sbis_page.click_contacts_button()

	time.sleep(3)

	sbis_contacts_page = SbisContactsPage(browser)
	text_region1 = sbis_contacts_page.text_region1()

	assert text_region1 == "Свердловская обл."

	try: 
		block = sbis_contacts_page.block()
		assert block.is_displayed(), "Блок не найден." 
		
	except NoSuchElementException:  
		assert False, "Блок не найден." 

	partners_Yekaterinburg = sbis_contacts_page.text_partners_Yekaterinburg()
	sbis_contacts_page.click_regions()

	time.sleep(3)

	sbis_contacts_page.click_changing()

	find_region2 = sbis_contacts_page.text_region2()
	assert find_region2 == "Камчатский край"

	partners_Kamchatka = sbis_contacts_page.text_partners_Kamchatka()
	assert partners_Kamchatka != partners_Yekaterinburg

	title = browser.title

	assert "Камчатский край" in title

	WebDriverWait(browser, 10).until(lambda driver: browser.current_url != old_url)
	new_url1 = browser.current_url

	assert "kamchatskij-kraj" in new_url1