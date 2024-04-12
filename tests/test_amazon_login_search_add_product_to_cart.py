"""
Tests to perform below steps:
1. Go to https://www.amazon.in/ and maximize window.
2. SignIn to amazon.
3. Search 'macbook air m2'.
4. Add product to cart.
"""

import pytest
from utils.pages.AmazonAddProductToCart import AmazonProductToCartPage
import utils.data.amazon_add_product_to_cart_data as amazon_data


@pytest.fixture()
def function_fixture(request, initialize_browser):
    request.cls.driver = initialize_browser
    request.cls.loginpage = AmazonProductToCartPage(request.cls.driver)
    print("Go to amazon home page")
    request.cls.driver.get(amazon_data.BASE_URL)
    print("Maximize window")
    request.cls.driver.maximize_window()
    request.cls.driver.implicitly_wait(5)


@pytest.mark.usefixtures("function_fixture")
class TestAmazonPage(object):

    def test_amazon_login_search_add_product_to_cart(self):
        print("Executing test_amazon_login_search_add_product_to_cart test")
        flag, err_msg = self.loginpage.login_to_amazon()
        assert flag, err_msg

        print("Search product")
        flag, err_msg = self.loginpage.search_product()
        assert flag, err_msg

        print("Click on product and add product to the cart")
        flag, err_msg = self.loginpage.click_on_product_and_add_to_cart()
        assert flag, err_msg

        print("Done --------------------------------")
