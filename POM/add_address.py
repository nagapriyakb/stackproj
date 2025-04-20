from shopstack.Lib.lib import SeleniumWrapper
from selenium.webdriver.common.by import By
from time import sleep
####some lines from sdet1
class AddAddress():
    _nav_mu=("xpath","//div[@class='MuiAvatar-root MuiAvatar-circular MuiAvatar-colorDefault css-bjoz8z']")
    _nav_profile=("xpath","//li[normalize-space()='My Profile']")
    _lnk_address=("xpath","//div[normalize-space()='My Addresses']")
    _btn_add_address = ("xpath", "//button[normalize-space()='Add Address']")
    _txt_name = ("xpath", "//input[@id='Name']")
    _txt_house = ("xpath", "//input[@id='House/Office Info']")
    _txt_street = ("xpath", "//input[@id='Street Info']")
    _txt_landmark = ("xpath", "//input[@id='Landmark']")
    _dropdown_country = ("xpath", "//select[@id='Country']")
    _dropdown_state = ("xpath", "//select[@id='State']")
    _dropdown_city = ("xpath", "//select[@id='City']")
    _txt_pincode = ("id", "Pincode")
    _txt_phonenumer = ("id", "Phone Number")
    _btn_submit = ("xpath", "//button[@id='addAddress']")
    def __init__(self, driver):
        self.driver = driver

    def add_new_address(self):
        sw=SeleniumWrapper(self.driver)
        sw.click_element(self._nav_mu)
        sw.click_element(self._nav_profile)
        sw.click_element(self._lnk_address)
        sleep(3)
        sw.click_element(self._btn_add_address)
        sw.enter_text(self._txt_name, value="John Doe")
        sw.enter_text(self._txt_house, value="123")
        sw.enter_text(self._txt_street, value="Main St")
        sw.enter_text(self._txt_landmark, value="Near Park")
        sw.select_item(self._dropdown_country, item="India")
        sw.select_item(self._dropdown_state, item="Karnataka")
        sw.select_item(self._dropdown_city, item="Bengaluru")
        # sw.select_item(self._dropdown_country, item="India")
        sw.enter_text(self._txt_pincode, value="560010")
        sw.enter_text(self._txt_phonenumer,value="9009009087")
        sleep(1)
        sw.click_element(self._btn_submit)
        sleep(3)
