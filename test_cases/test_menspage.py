from shopstack.POM.shoppersLogin import shoppersLoginpage
from shopstack.POM.MensPage import MensPage

def test_add_mens_product(setupteardown):
    # driver = setupteardown
    login = shoppersLoginpage(setupteardown)
    mens = MensPage(setupteardown)
    login.login("nagapriyakb@gmail.com", "Test@123")
    mens.open_mens_section_and_add_product()
