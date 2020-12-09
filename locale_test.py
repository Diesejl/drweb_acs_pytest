import pytest
import gettext
from src.pages.acs_pages_locators import URL
from src.pages.acs_pages_methods import HeaderPage


@pytest.mark.usefixtures("install_driver")
class TestLocale:
    @pytest.mark.Locale
    @pytest.mark.parametrize("lang, title",
                             [
                                 ("en", "Dr.Web Account"),
                                 ("ru", "Dr.Web Учетная запись"),
                             ]
                             )
    def test_open_main_page_eng(self, lang, title):
        """
        Пример теста с указанием множественных аргументов. В данном случае указан список с парой кортежей содержащий
        2 элемента. Можно добавить все языки, в таком случае тест будет запускаться несколько раз используя
        разные аргументы.
        !!!!Необходимо использовать gettext для использования искходников текстов от техписов.!!!!
        :param lang: Принимает строку языка для использвоания в качестве значения в методе для переключения языка
        :param title: Принимает строку языка для использвания в инструкции Assert при проверки элемента Title
        """
        self.header_page = HeaderPage(self.driver)
        self.header_page.open_test_environment(url=URL)
        self.header_page.change_site_language(lang_value=lang)
        assert self.header_page.at_page(text_title_page=title)
