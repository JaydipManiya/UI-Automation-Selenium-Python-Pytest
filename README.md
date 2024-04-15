# UI Automation using Selenium and Python Pytest
- This is generic UI Automation framework using Selenium and Python Pytest.

## Setup:
- [optional] Download and install Python3 from [here](https://www.python.org/downloads/) (Ignore the step if you already have python installed)
- [optional] Install pip module by following steps mentioned at [pip_installation_guide](https://pip.pypa.io/en/stable/installation/)
- Clone this repo, navigate to UI-Automation-Framework-Selenium-Python-Pytest folder.
- Execute requirements.txt file to install all the dependent python libraries using following command and make it pass without any error: pip install -r requirements.txt

## Running the tests:
- By default tests will run on Chrome browser, if you want to run on Firefox browser then pass following argument in run command: pytest -vs tests/test_amazon_login_search_add_product_to_cart.py --browser firefox
- At the end of tests execution, framework will generate Log file at current folder with name "log-<YYMMDD_HHMMSS>.log".
- Run following command to execute tests on Chrome. ex: pytest -vs tests/test_amazon_login_search_add_product_to_cart.py
- Run following command to execute and generate pytest html report: 
pytest -vs --capture sys tests/test_amazon_login_search_add_product_to_cart.py --html=report.html

## Notes:
- No need to download browser drivers as this is implemented using webdriver manager which will automatically download driver.
- If you are running tests/test_amazon_login_search_add_product_to_cart.py tests then make sure to update login credentials (LOGIN_EMAIL and LOGIN_PASSWORD) in utils/data/amazon_add_product_to_cart_data.py file.
