from selenium.webdriver.common.by import By
"""
Тут указаны переменные используемые в функциях при поиске элементов на странице.
Присваивается значение согласно выбранному способу поиска элемента. По ID, XPATH, CSS и так далее.
"""

URL = "https://acs.drweb.com/"
LANG_COMBOBOX = (By.XPATH, '//*[@id="lang"]/select')
KEY_INPUT = (By.ID, "search_item")
EMAIL_INPUT = (By.ID, "email_item")
BTN_SUBMIT = (By.ID, "submit_button")
DRWEB_ICON = (By.XPATH, '//*[@id="top_menu"]/h1/a/img')
DRWEB_TITLE = (By.XPATH, '//*[@id="top_menu"]/h1/a/span')
DRWEB_MOBILE = (By.XPATH, '//*[@id="main"]/div[1]/div[1]/div')
LINK_LEARN_MORE = (By.XPATH, '//*[@id="main"]/div[2]/a')
LINK_DRWEB_COM = (By.XPATH, '//*[@id="langForm"]/ul/li[1]/a')
LINK_PRIVATE_POLICY = (By.XPATH, '//*[@id="langForm"]/ul/li[2]/a')
ELEMENT_VERSION = (By.XPATH, '//*[@id="langForm"]/ul/li[3]/span')
WRONG_KEY = (By.XPATH, '//*[@id="messageBlock"]')

