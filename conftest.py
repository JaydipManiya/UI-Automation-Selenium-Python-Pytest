import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser on which you want to run automation tests,"
                                                                         " valid values are chrome/firefox")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def initialize_browser(request, browser):
    """
    Fixture to initialize browser.
    """
    global driver
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    if browser.lower() == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def function_finalizer():
        driver.quit()

    request.addfinalizer(function_finalizer)
    return driver
