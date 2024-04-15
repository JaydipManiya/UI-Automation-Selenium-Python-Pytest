"""
Tests to perform below steps and verify product successfully added to the cart:
1. Go to https://www.amazon.in/ and maximize window.
2. SignIn to amazon.
3. Search 'macbook air m2'.
4. Add product to cart.

- If you are running tests/test_amazon_login_search_add_product_to_cart.py tests then make sure to update
login credentials (LOGIN_EMAIL and LOGIN_PASSWORD) in utils/data/amazon_add_product_to_cart_data.py file.
"""

import pytest
from utils.pages.AmazonAddProductToCart import AmazonProductToCartPage
import utils.data.amazon_add_product_to_cart_data as amazon_data
from utils.lib.LoggerUtils import set_logger


@pytest.fixture()
def class_fixture(request, initialize_browser):
    """
    Class fixture to go to amazon home page and maximize the window.
    :param request: request instance
    :param initialize_browser: fixture to initialize driver
    """
    request.cls.driver = initialize_browser
    request.cls.loginpage = AmazonProductToCartPage(request.cls.driver)
    request.cls.logger = set_logger(__name__)
    request.cls.logger.info("Go to amazon home page")
    request.cls.driver.get(amazon_data.BASE_URL)
    request.cls.logger.info("Maximize window")
    request.cls.driver.maximize_window()
    request.cls.driver.implicitly_wait(5)


@pytest.mark.usefixtures("class_fixture")
class TestAmazonPage:

    def test_amazon_login_search_add_product_to_cart(self):
        """
        Tests to perform below steps and verify product successfully added to the cart.
        1) Login to Amazon
        2) Search product
        3) Click on product and add product to the cart
        """
        self.logger.info("Login to Amazon")
        flag, err_msg = self.loginpage.login_to_amazon()
        assert flag, err_msg

        self.logger.info("Search product")
        flag, err_msg = self.loginpage.search_product()
        assert flag, err_msg

        self.logger.info("Click on product and add product to the cart")
        flag, err_msg = self.loginpage.click_on_product_and_add_to_cart()
        assert flag, err_msg

        print("------------ Test Passed -----------------")
