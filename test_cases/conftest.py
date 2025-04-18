from selenium import webdriver
from time import sleep
from pytest import fixture
@fixture()
def setupteardown():
    driver=webdriver.Chrome()
    driver.get("https://shoppersstack.com/")
    driver.maximize_window()
    sleep(5)
    yield driver
    sleep(10)
    driver.quit()