# from selframe.Utilities.lib import SeleniumWrapper
from shopstack.Lib.lib import SeleniumWrapper
from shopstack.utils.logger import get_logger


class shoppersLoginpage():
    _btn_login_home=("xpath","//button[@id='loginBtn']")
    _txt_email=("xpath","//input[@name='Email']")
    _txt_pwd=("xpath","//input[@id='Password']")
    _btn_login_shopperlogin=("xpath","//button[@type='submit']")

    def __init__(self,driver):
        self.driver=driver
        self.logger = get_logger("LoginPage")


    def login(self,email,password):
        sw=SeleniumWrapper(self.driver)
        sw.click_element(self._btn_login_home)
        self.logger.info("Attempting to log in")
        sw.enter_text(self._txt_email,value=email)
        self.logger.debug(f"Entered username: {email}")
        sw.enter_text(self._txt_pwd,value=password)
        self.logger.debug(f"Entered password")
        sw.click_element(self._btn_login_shopperlogin)
        self.logger.info("Clicked login button")




