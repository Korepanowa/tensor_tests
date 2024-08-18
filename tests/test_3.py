import pytest
import time

import os

from pages.sbis_page import SbisPage
from pages.sbis_download_page import SbisDownloadPage

def test_3(browser):

	sbis_page = SbisPage(browser)
	browser.get('https://sbis.ru/')
	browser.fullscreen_window()

	sbis_page.scrolling()
	sbis_page.click_download_button()

	time.sleep(3)

	sbis_download_page = SbisDownloadPage(browser)
	sbis_download_page.click_download_button()

	time.sleep(30)

	initial_size = os.path.getsize('/home/korens/Загрузки/sbisplugin-setup-web.exe')

	time.sleep(10)

	final_size = os.path.getsize('/home/korens/Загрузки/sbisplugin-setup-web.exe')

	size_mg = "{0:.2f}".format(final_size / 1048576)

	assert initial_size == final_size

	text_download = sbis_download_page.text_download()

	assert size_mg in text_download
