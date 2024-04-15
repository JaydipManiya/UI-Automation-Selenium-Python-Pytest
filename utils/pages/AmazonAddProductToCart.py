"""
Common methods to test Amazon Login, Search product and add product to cart scenarios.
"""

import time
from selenium.webdriver.common.action_chains import ActionChains
import utils.locators.amazon_add_product_to_cart as amazon_locators
import utils.data.amazon_add_product_to_cart_data as amazon_data
import utils.data.common_defines as cd
from utils.lib.LoggerUtils import set_logger
from .BasePage import BaseClass


class AmazonProductToCartPage(BaseClass):
    def __init__(self, driver):
        """
        Initialize AmazonProductToCartPage class.
        """
        super().__init__(driver)
        self.logger = set_logger(__name__)

    def login_to_amazon(self):
        """
        Method to Signin to Amazon.
        :return login_success: True if login is successful else False.
                err_msg: Error message on failure.
        """
        login_success = False
        err_msg = ""
        try:
            self.logger.info("Click on Account & Lists button")
            account_list_ele = self.find_element(self.driver, cd.LOCATE_BY_XPATH, amazon_locators.ACCOUNT_LIST_BTN)
            hover = ActionChains(self.driver).move_to_element(account_list_ele)
            hover.perform()
            self.wait_element_to_be_clickable(self.driver, cd.LOCATE_BY_XPATH, amazon_locators.SIGNIN_BTN).click()

            self.logger.info("Enter Signin email")
            if amazon_data.LOGIN_EMAIL == "<SET_ME>":
                assert False, "Please set Amazon login credential LOGIN_EMAIL " \
                              "in utils/data/amazon_add_product_to_cart_data.py file"
            self.wait_element_to_be_visible(self.driver, cd.LOCATE_BY_XPATH, amazon_locators.SIGNIN_EMAIL).\
                send_keys(amazon_data.LOGIN_EMAIL)

            self.logger.info("Click on Continue button")
            self.wait_element_to_be_clickable(self.driver, cd.LOCATE_BY_XPATH, amazon_locators.SIGNIN_CONTINUE_BTN).click()

            self.logger.info("Enter Signin password")
            if amazon_data.LOGIN_PASSWORD == "<SET_ME>":
                assert False, "Please set Amazon login credential LOGIN_PASSWORD " \
                              "in utils/data/amazon_add_product_to_cart_data.py file"
            self.wait_element_to_be_visible(self.driver, cd.LOCATE_BY_XPATH, amazon_locators.SIGNIN_PASSWORD).\
                send_keys(amazon_data.LOGIN_PASSWORD)

            self.logger.info("Click on Submit button")
            self.wait_element_to_be_clickable(self.driver, cd.LOCATE_BY_XPATH, amazon_locators.SIGNIN_SUBMIT_BTN).click()
            login_success = True
        except Exception as ex:
            err_msg = "Exception raised during signin, exception is : {}".format(ex)

        return login_success, err_msg

    def search_product(self):
        """
        Method to search product.
        :return login_success: True if login is successful else False.
                err_msg: Error message on failure.
        """
        flag = False
        err_msg = ""
        try:
            self.logger.info("SEARCH {} ".format(amazon_data.PRODUCT_TO_SEARCH))
            self.wait_element_to_be_clickable(self.driver, cd.LOCATE_BY_XPATH, amazon_locators.SEARCH_BAR).\
                send_keys(amazon_data.PRODUCT_TO_SEARCH)

            self.logger.info("Click on search button")
            self.wait_element_to_be_clickable(self.driver, cd.LOCATE_BY_XPATH, amazon_locators.SEARCH_BTN).click()
            flag = True
        except Exception as ex:
            err_msg = "Exception raised while searching product, exception is : {}".format(ex)

        return flag, err_msg

    def click_on_product_and_add_to_cart(self):
        """
        Method to click on product and add to cart.
        :return login_success: True if login is successful else False.
                err_msg: Error message on failure.
        """
        flag = False
        err_msg = ""
        try:
            self.logger.info("Click on expected product")
            current_window = self.driver.current_window_handle
            self.wait_element_to_be_clickable(self.driver, cd.LOCATE_BY_XPATH, amazon_locators.PRODUCT_ELE).click()
            time.sleep(2)
            all_window = self.driver.window_handles
            self.driver.switch_to.window(all_window[1])
            current_window = self.driver.current_window_handle
            self.logger.info("Click on add to cart button")
            self.wait_element_to_be_clickable(self.driver, cd.LOCATE_BY_XPATH, amazon_locators.ADD_TO_CART_BTN).click()
            time.sleep(3)
            flag = True
        except Exception as ex:
            err_msg = "Exception raised while click on product and adding to cart, exception is : {}".format(ex)

        return flag, err_msg
