from shopstack.Lib.lib import SeleniumWrapper
from time import sleep
class ViewCart(SeleniumWrapper):
    _btn_cart = ("xpath", "//a[@id='cart']")
    _btn_buy_now = ("xpath", "//button[@id='buynow_fl']")
    _radio_addr=("xpath","(// input[@ id='109975'])[1]")
    _btn_proceed=("xpath","//button[text()='Proceed']")
    # _radio_cod=("xpath","(//input[@class='PrivateSwitchBase-input css-1m9pwf3'])[2]")
    # _rad_cash=("xpath","//input[@value='COD']")
    _sp_cash=("xpath","// span[normalize-space() = 'Cash On Delivery (COD)']")
    _sp_proceed=("xpath","// span[normalize-space() = 'Cash On Delivery (COD)']")

    def __init__(self, driver):
        self.driver = driver

    def go_to_cart_and_buy(self):
        sleep(6)
        sw=SeleniumWrapper(self.driver)
        sw.click_element(self._btn_cart)
        sw.click_element(self._btn_buy_now)
        sw.click_element(self._radio_addr)
        sw.click_element(self._btn_proceed)
        sleep(3)
        sw.click_element(self._sp_cash)
        sw.click_element
