from shopstack.Lib.lib import SeleniumWrapper
from time import sleep

class MensPage(SeleniumWrapper):
    _lnk_mens = ("xpath","//a[@id='men']")
    _btn_add_to_cart = ("xpath","(//button[@type='button'][normalize-space()='add to cart'])[1]")
    def __init__(self, driver):
        self.driver = driver
    def open_mens_section_and_add_product(self):
        sw=SeleniumWrapper(self.driver)
        sw.click_element(self._lnk_mens)
        sleep(6)
        sw.click_element(self._btn_add_to_cart)
        sleep(2)
