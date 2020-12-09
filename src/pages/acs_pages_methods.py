import allure
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.acs_pages_locators import *


class HeaderPage:
    def __init__(self, driver):
        self.KEY_INPUT = KEY_INPUT
        self.EMAIL_INPUT = EMAIL_INPUT
        self.BTN_SUBMIT = BTN_SUBMIT
        self.driver = driver
        self.LANG_COMBOBOX = LANG_COMBOBOX

    def at_page(self, text_title_page: str):
        """
        Объявлена функция для проверки нахождения на странице с помощью title. Использовать на случай необходимости
        проверки на какой странице находишься во время теста.
        :param text_title_page: Аннотация к типу переменной String
        :return: Возвращает True or False
        """
        return text_title_page in self.driver.title

    @allure.step
    def open_test_environment(self, url: str):
        """
        :param url: Объявлена функция с параметром URL, аннотация к типу переменной String
        :return: К объекту driver применяется метод get() в который передается в качестве аргумента URL для его открытия
        """
        self.driver.get(url)
        return self

    @allure.step
    def change_site_language(self, lang_value: str):
        """
        Объявлена функция для выбора значения в комбобоксе языка интерфейса. Ищется элемент по комбобокса, к нему
        применяется метод выбора значения, в качестве значения берется аргумент при вызове функции
        :param lang_value: В качестве параметра указывается строка необходимого языка
        """
        Select(self.driver.find_element(*self.LANG_COMBOBOX)).select_by_value(lang_value)

    @allure.step
    def find_element(self, locator, time=10):
        """
        Объявлена фукнция для поиска элемента, используется в тестах в совокупности с Assert
        :param locator: В качестве параметра принимается локатор, переменная из модуля с локаторами страницы
        :param time: Указывается допустимое время в секундах для ожидания драйвером, в случае долгой загрузки страницы
        :return: Возвращает True or False
        """
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    @allure.step
    def click_submit_button(self, time=10):
        """
        Объявлена функиция для клацанья на кнопку "подтвердить" на странице к форме ввода Ключ:Имейл
        Создается объект кнопки. В качестве аргумента используется локатор кнопки, в случае ошибки выполнится message
        :param time: Указывается допустимое время в секундах для ожидания драйвером, в случае долгой загрузки страницы
        """
        submit_btn = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(self.BTN_SUBMIT),
                                                            message=f"Can't find element by locator {self.BTN_SUBMIT}")
        submit_btn.click()

    @allure.step
    def enter_email(self, text, time=10):
        """
        Объявлена функция для ввода строки в поле ввода имейла.
        :param text: В качестве текста указывается на усмотрение создаваемых тестов
        :param time: Все как обычно, ждем указанное количество времени)
        """
        email_field = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(self.EMAIL_INPUT),
                                                             message=f"Can't find element by locator {self.EMAIL_INPUT}")
        email_field.send_keys(text)

    @allure.step
    def enter_key(self, text: str, time=10):
        """
        Объявлена функция для ввода строки в поле ключа.
        :param text: В качестве текста указывается так же на усмотрение тестировщика при создании тестов
        :param time: да да, все тоже самое, что было выше
        :return: Nope
        """
        key_field = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(self.KEY_INPUT),
                                                           message=f"Can't find element by locator {self.KEY_INPUT}")
        key_field.send_keys(text)
