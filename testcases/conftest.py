import pytest
from selenium import webdriver

# conftest file
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="D:\\projectjars\\browserdriver\\chromedriver.exe")
        print('......Launching Chrome browser.......')
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="D:\\projectjars\\browserdriver\\geckodriver.exe")
        print('.........Launching Firefox browser.........')
    driver.maximize_window()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata['Project Name'] = "Nop Ecommerce Automation"
    config._metadata['Module Name '] = "Customers"
    config._metadata['QA'] = "Arun"


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)
