from shopstack.POM.shoppersLogin import shoppersLoginpage
# class Login():
email="nagapriyakb@gmail.com"
password="Test@123"

def test_valid_login(setupteardown):
        logobj=shoppersLoginpage(setupteardown)
        logobj.login(email,password)

