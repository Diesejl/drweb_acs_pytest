import pytest
from src.pages.acs_pages_locators import *
from src.pages.acs_pages_methods import HeaderPage

"""
Суть теста по возможности отображается в названии самой функции после def.
В самих тестах краткое описание на проверку чего они направлены.
Тесты используют фикстуры для маркирвоки формата "@pytest.mark.smoke"
Перед классом используется фикстура для использования функции install_driver, создающая объект драйвера и завершающая
свою работу после выполнения теста.
"""


@pytest.mark.usefixtures("install_driver")
class TestSmoke:
    @pytest.mark.smoke
    def test_mobile_icon_is_on_main_page(self):
        """
        Тест на наличие иконки дрвеб на главной странице.
        Создаем объект класса, далее используем метод класса указывая ему URL нашего ACS.
        Используем инструкцию Assert для утверждения результа работы функции поиска элемента. В случае ошибки,
        получим сообщение об отсутсвии необходимого элемента.
        """
        self.header_page = HeaderPage(self.driver)
        self.header_page.open_test_environment(url=URL)
        assert self.header_page.find_element(DRWEB_MOBILE), f"Элемент {DRWEB_MOBILE} не был найден"

    @pytest.mark.smoke
    def test_link_learn_more_is_on_main_page(self):
        """
        Тест на наличие ссылки "Подробнее..." на главной странице
        """
        self.header_page = HeaderPage(self.driver)
        self.header_page.open_test_environment(url=URL)
        assert self.header_page.find_element(LINK_LEARN_MORE), f"Элемент {LINK_LEARN_MORE} не был найден"

    @pytest.mark.smoke
    def test_link_drweb_com_is_on_main_page(self):
        """
        Тест на наличие ссылки "© «Доктор Веб», 1992–2020" на главной странице
        """
        self.header_page = HeaderPage(self.driver)
        self.header_page.open_test_environment(url=URL)
        assert self.header_page.find_element(LINK_DRWEB_COM), f"Элемент {LINK_DRWEB_COM} не был найден"

    @pytest.mark.smoke
    def test_link_private_policy_is_on_main_page(self):
        """
        Тест на наличие ссылки "Политика конфиденциальности" на главной странице
        """
        self.header_page = HeaderPage(self.driver)
        self.header_page.open_test_environment(url=URL)
        assert self.header_page.find_element(LINK_PRIVATE_POLICY), f"Элемент {LINK_PRIVATE_POLICY} не был найден"

    @pytest.mark.smoke
    def test_lang_combobox_is_on_main_page(self):
        """
        Тест на наличие элемента комбобокса с выбором языка на главной странице
        """
        self.header_page = HeaderPage(self.driver)
        self.header_page.open_test_environment(url=URL)
        assert self.header_page.find_element(LANG_COMBOBOX), f"Элемент {LANG_COMBOBOX} не был найден"

    @pytest.mark.smoke
    def test_key_field_is_on_main_page(self):
        """
        Тест на наличие элемента поле ввода ключа на главной странице
        """
        self.header_page = HeaderPage(self.driver)
        self.header_page.open_test_environment(url=URL)
        assert self.header_page.find_element(KEY_INPUT), f"Элемент {KEY_INPUT} не был найден"

    @pytest.mark.smoke
    def test_email_field_is_on_main_page(self):
        """
        Тест на наличие элемента поле ввода имейла на главной странице
        """
        self.header_page = HeaderPage(self.driver)
        self.header_page.open_test_environment(url=URL)
        assert self.header_page.find_element(EMAIL_INPUT), f"Элемент {EMAIL_INPUT} не был найден"

    @pytest.mark.smoke
    def test_button_submit_is_on_main_page(self):
        """
        Тест на наличие элемента кнопки "Получить код" на главной странице
        """
        self.header_page = HeaderPage(self.driver)
        self.header_page.open_test_environment(url=URL)
        assert self.header_page.find_element(BTN_SUBMIT), f"Элемент {BTN_SUBMIT} не был найден"

    @pytest.mark.smoke
    def test_text_version_is_on_main_page(self):
        """
        Тест на наличие элемента с текстом версии приложения на главной странице
        """
        self.header_page = HeaderPage(self.driver)
        self.header_page.open_test_environment(url=URL)
        assert self.header_page.find_element(ELEMENT_VERSION), f"Элемент {ELEMENT_VERSION} не был найден"

    def test_text_wrong_key_is_on_main_page(self):
        """
        Тест на наличие элемента текста ошибки "Неверный ключ" при вводе неверных данных и подтверждении кнопкой
        """
        self.header_page = HeaderPage(self.driver)
        self.header_page.open_test_environment(url=URL)
        self.header_page.enter_key("WRONG_KEY")
        self.header_page.enter_email("WRONG@EMAIL.MOC")
        self.header_page.click_submit_button()
        assert self.header_page.find_element(WRONG_KEY), f"Элемент {WRONG_KEY} не был найден"

    @pytest.mark.smoke
    @pytest.mark.parametrize("lang, title", [("ru", "Dr.Web Учетная запись")])
    def test_open_main_page_eng(self, lang, title):
        """
        Пример теста с указанием множественных аргументов. В данном случае указан список с одним кортежем содержащий
        2 элемента. Можно добавить все языки, в таком случае тест будет запускаться несколько раз используя
        разные аргументы.
        :param lang: Принимает строку языка для использвоания в качестве значения в методе для переключения языка
        :param title: Принимает строку языка для использвания в инструкции Assert при проверки элемента Title
        """
        self.header_page = HeaderPage(self.driver)
        self.header_page.open_test_environment(url=URL)
        self.header_page.change_site_language(lang_value=lang)
        assert self.header_page.at_page(text_title_page=title), f"Должен был быть получен {title}"

    @pytest.mark.smoke
    @pytest.mark.parametrize("lang", ["en"])
    def test_drweb_icon_is_on_main_page(self, lang):
        """
        Тест на наличие элемента иконки DrWeb на главной странице
        :param lang: Принимает строку языка для использвоания в качестве значения в методе для переключения языка
        """
        self.header_page = HeaderPage(self.driver)
        self.header_page.open_test_environment(url=URL)
        self.header_page.change_site_language(lang_value=lang)
        assert self.header_page.find_element(DRWEB_ICON), f"Элемент {DRWEB_ICON} не был найден"
