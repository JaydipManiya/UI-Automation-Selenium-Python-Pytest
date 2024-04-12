# UI Automation using Selenium and Python Pytest
- This is generic UI Automation framework using Selenium and Python Pytest.

## Setup:
- Download and install Python3 from [here](https://www.python.org/downloads/) (Ignore the step if you already have python installed)
- Clone this repo, navigate to UI-Automation-Framework-Selenium-Python-Pytest folder.
- Execute requirements.txt file to install all the dependent python libraries using following command and make it pass without any error: pip install -r requirements.txt

## Running the tests:
- Run below command to execute tests. ex: pytest -vs tests/test_amazon_login_search_add_product_to_cart.py
- Run below command to execute and generate pytest html report: 
pytest -vs --capture sys tests/test_amazon_login_search_add_product_to_cart.py --html=report.html
