import pytest
import allure
import rep
from selenium import webdriver
from services.db_client import MockDBClient
from services.corba_client import MockCorbaOrderProcessor

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def db():
    return MockDBClient()

@pytest.fixture
def order_processor(db):
    return MockCorbaOrderProcessor(db)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )
