from shopstack.POM.view_cart import ViewCart
from shopstack.POM.shoppersLogin import shoppersLoginpage
from shopstack.POM.add_address import AddAddress
from shopstack.POM.MensPage import MensPage


# from shopstack.POM.placing_order import PlacingOrder

def test_complete_checkout_flow(setupteardown):
    # driver = setupteardown
    #
    # login = shoppersLoginpage(driver)
    # mens = MensPage(driver)
    # cart = ViewCart(driver)
    # address = AddAddress(driver)
    # order = PlacingOrder(driver)
    #
    # login.login("testuser@example.com", "Test@123")
    # mens.open_mens_section_and_add_product()
    # cart.go_to_cart_and_buy()
    # address.add_new_address()
    # order.place_order_cod()\
    login = shoppersLoginpage(setupteardown)
    address=AddAddress(setupteardown)
    login.login("nagapriyakb@gmail.com", "Test@123")
    # address.add_new_address()
    mens = MensPage(setupteardown)
    mens.open_mens_section_and_add_product()
    cart = ViewCart(setupteardown)
    cart.go_to_cart_and_buy()
    # // h1[normalize - space() = 'Order Confirmed']

