import time

import pytest
from src.pages.acs_pages_locators import *
from src.pages.acs_pages_methods import HeaderPage


@pytest.mark.usefixtures("install_driver")
class TestDraft:
    @pytest.mark.devtests
    def test_drweb_icon_is_on_main_page(self):
        """
        Это просто черновой тест, в случае удачного использования, переносится в основной модуль.
        :return: nope =)
        """
        self.header_page = HeaderPage(self.driver)
        self.header_page.open_test_environment(url=URL)
        self.header_page.enter_key("FKJSFPMOWQUNSPDO")
        self.header_page.enter_email("some@text.com")
        self.header_page.click_submit_button()
        assert self.header_page.find_element(WRONG_KEY), f"Элемент {WRONG_KEY} не был найден"
