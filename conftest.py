import pytest
from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def install_driver(request):
    """
    Объявлена фикстура, она же функция которая будет использоватья при запуске теста.
    Необходима для того, что бы не дублировать код и создавать объект драйвера и закрывать
    браузер после завершения теста
    """
    driver: WebDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    request.cls.driver = driver
    yield
    driver.close()
