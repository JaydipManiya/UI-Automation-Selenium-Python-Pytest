"""
This file contains common methods.
You can find all the explicit wait methods at: https://selenium-python.readthedocs.io/waits.html
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseClass(object):
    def __init__(self, driver):
        """
        Initialize BaseClass.
        """
        self.driver = driver

    def wait_element_to_be_clickable(self, driver, element_method, element_to_wait, wait_time=40):
        """
        Method to wait till element to be clickable.
        :param driver: driver
        :element_method: Method used to find locator (XPATH, ID, CSS_SELECTOR, etc)
        :element_to_wait: Element to wait.
        :wait_time: time to wait
        """
        element = None
        if element_method.upper() == "XPATH":
            element = WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, element_to_wait)))
        elif element_method.upper() == "ID":
            element = WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.ID, element_to_wait)))
        elif element_method.upper() == "CLASS_NAME":
            element = WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.CLASS_NAME, element_to_wait)))
        elif element_method.upper() == "CSS_SELECTOR":
            element = WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.CSS_SELECTOR, element_to_wait)))
        else:
            print("Pass valid method to find locator")
        return element

    def wait_element_to_be_visible(self, driver, element_method, element_to_wait, wait_time=40):
        """
        Method to wait till element to be visible.
        :param driver: driver
        :element_method: Method used to find locator (XPATH, ID, CSS_SELECTOR, etc)
        :element_to_wait: Element to wait.
        :wait_time: time to wait
        """
        element = None
        if element_method.upper() == "XPATH":
            element = WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, element_to_wait)))
        elif element_method.upper() == "ID":
            element = WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.ID, element_to_wait)))
        elif element_method.upper() == "CLASS_NAME":
            element = WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.CLASS_NAME, element_to_wait)))
        elif element_method.upper() == "CSS_SELECTOR":
            element = WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((By.CSS_SELECTOR, element_to_wait)))
        else:
            print("Pass valid method to find locator")
        return element

    def find_element(self, driver, element_method, element_to_find, retry=2, wait_time=40):
        """

        """
        element = None
        if element_method.upper() == "XPATH":
            element = driver.find_element(By.XPATH, element_to_find)
        else:
            print("Pass valid method to find locator")

        return element