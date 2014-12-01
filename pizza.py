from selenium import webdriver
from shhh import EMAIL, PASSWORD

# Globals
# DRIVER = webdriver.PhantomJS()
DRIVER = webdriver.Firefox()


def log_in_to_papa_johns():
    starting_url = 'http://order.papajohns.com/signin.html'
    DRIVER.get(starting_url)
    DRIVER.switch_to.frame("signInFrame")
    element_userName = DRIVER.find_element_by_id("userName")
    element_userName.send_keys(EMAIL)
    element_password = DRIVER.find_element_by_id("pwd")
    element_password.send_keys(PASSWORD)
    DRIVER.find_element_by_id('btnModalSignIn').click()
    DRIVER.switch_to.default_content()
    assert "My Account" in DRIVER.page_source
    DRIVER.find_element_by_class_name('accountBtn').click()
    print DRIVER.page_source
    # ensure a fave has been added
    assert "No Faves found" not in DRIVER.page_source
    DRIVER.close()


def add_favorite_order_to_shopping_cart():
    pass


def order_pizza():
    pass


def main():
    log_in_to_papa_johns()


if __name__ == '__main__':
    main()
