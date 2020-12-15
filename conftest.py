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
    Добавлены опции для запуска браузера Хром в Headless режиме.
    """
    options = webdriver.ChromeOptions()
    options.headless = True
    # options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    driver: WebDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    request.cls.driver = driver
    yield
    driver.close()
