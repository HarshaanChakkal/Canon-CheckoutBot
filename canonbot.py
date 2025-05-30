from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def setup_driver():
    options = Options()
    #options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
    options.add_argument("--incognito")
    #options.add_argument("--ignore-certificate-errors")
    #options.add_argument("--allow-running-insecure-content")
    #options.add_argument("--remote-debugging-port=9222")  
    options.add_experimental_option('detach', True)
    #options.add_experimental_option("excludeSwitches", ["enable-automation"])
    #options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)
    return driver


def check_stock_and_add_to_cart(driver, url):
    driver.get(url)
    time.sleep(3)  # Allow page to load
    driver.refresh()
    cookie = 'onetrust-accept-btn-handler'
    cookies = driver.find_element(By.ID, cookie)
    cookies.click()
    try:
        stock_status = driver.find_element(By.CSS_SELECTOR, "div.stock.available")
        print("Item is in stock! Proceeding to checkout.")
        scroll = driver.find_element(By.CLASS_NAME, 'pagebuilder-column-group')
        ActionChains(driver)\
            .scroll_to_element(scroll)\
            .perform()
        time.sleep(1)
        addtocart = driver.find_element(By.ID, 'product-addtocart-button')
        addtocart.click()
        return True
    except:
        print("Item is out of stock. Checking again in 5 minutes...")
        return False
'''try:
    while True:
        driver.get(url)
        time.sleep(5)  # Allow page to load

        # Locate the stock status element (modify selector if needed)
        try:
            stock_status = driver.find_element(By.CSS_SELECTOR, "div.stock.available")
            # Check if the product is in stock
            print("Item is in stock! Proceeding to checkout.")
            
            # Click the checkout button
            atc = 'product-addtocart-button'
            scroll = driver.find_element(By.ID, atc)
            ActionChains(driver)\
                .scroll_to_element(scroll)\
                .perform()
            addtocart = driver.find_element(By.ID, atc)
            addtocart.click()
            break  # Exit loop once checkout is initiated
        except:
            print("Item is out of stock. Checking again in 5 minutes...")'''
        
        # Wait before checking again (adjust the delay as needed)

def proceed_to_checkout(driver):
    time.sleep(3)
    gotocart = 'button-modal-proceed'
    cart = driver.find_element(By.CLASS_NAME, gotocart)
    cart.click()
    time.sleep(random.uniform(1, 2))

    checkout_button = driver.find_element(By.CSS_SELECTOR, "button.action.primary.checkout")
    driver.execute_script("arguments[0].click();", checkout_button)

    time.sleep(random.uniform(4, 5))
    guest = 'button.action.primary.checkout'
    as_guest = driver.find_element(By.CSS_SELECTOR, guest)
    as_guest.click()
    

def shipping_details(driver):
    # Shipping address
    firstname = 'firstname'
    lastname = 'lastname'
    street = 'street[0]'
    city = 'city'
    state = 'region_id'
    zip = 'postcode'
    phone = 'telephone'
    email = 'customer-email'
    time.sleep(random.uniform(3, 5))

    fname = driver.find_element(By.NAME, firstname)
    fname.click()
    fname.send_keys('Harshaan')

    lname = driver.find_element(By.NAME, lastname)
    lname.click()
    lname.send_keys('Chakkal')

    address = driver.find_element(By.NAME, street)
    address.click()
    address.send_keys('14982 S Houston St', Keys.RETURN)

    shehar = driver.find_element(By.NAME, city)
    shehar.click()
    shehar.send_keys('Olathe')

    stateselect = driver.find_element(By.NAME, state)
    dropdown = Select(stateselect)
    dropdown.select_by_visible_text('Kansas')

    zipcode = driver.find_element(By.NAME, zip)
    zipcode.click()
    zipcode.send_keys('66061')

    number = driver.find_element(By.NAME, phone)
    number.click()
    number.send_keys('4628451915')
    time.sleep(1)

    emailid = driver.find_element(By.ID, email)
    emailid.click()
    emailid.send_keys('harshaansingh113@gmail.com')
    time.sleep(1)

def verify_address(driver):
    scroll2 = driver.find_element(By.CSS_SELECTOR, 'button.button.action.continue.primary')
    ActionChains(driver)\
        .scroll_to_element(scroll2)\
        .perform()
    time.sleep(2)
    continue_button = driver.find_element(By.CSS_SELECTOR, 'button.button.action.continue.primary')
    continue_button.click()

    time.sleep(3)
    verified = driver.find_element(By.CSS_SELECTOR, 'button.button.action.use')
    verified.click()
    time.sleep(3)

#Card details
def card_info(driver):
    scroll2 = driver.find_element(By.ID, 'continue-to-review')
    ActionChains(driver)\
        .scroll_to_element(scroll2)\
        .perform()
    time.sleep(1)
    name = driver.find_element(By.ID, 'name_on_card')
    name.click()
    name.send_keys('Harshaan Chakkal')
    time.sleep(1)

    iframe = driver.find_element(By.CSS_SELECTOR, "iframe[title='secure payment field']")
    driver.switch_to.frame(iframe)

    # Locate the credit card number input field within the iframe
    cardnumber = driver.find_element(By.NAME, "number")  # Adjust selector if necessary
    cardnumber.send_keys('5269414463695278')
    # Switch back to the main content
    driver.switch_to.default_content()
    time.sleep(1)

    expmonth = driver.find_element(By.ID, 'chcybersource_expiration')
    drop = Select(expmonth)
    drop.select_by_visible_text('03 - March')
    
    expyear = driver.find_element(By.ID, 'chcybersource_expiration_yr')
    dropdown = Select(expyear)
    dropdown.select_by_visible_text('2026')
    time.sleep(1)
    
    iframe2 = driver.find_element(By.CSS_SELECTOR, ".flex.input-text.cvv.flex-microform iframe")
    driver.switch_to.frame(iframe2)
    cvv = driver.find_element(By.NAME, 'securityCode')
    cvv.click()
    cvv.send_keys('811')
    driver.switch_to.default_content()

def final_step(driver):
    '''scroll3 = driver.find_element(By.CLASS_NAMEE, 'norton-verisign')
    ActionChains(driver)\
        .scroll_to_element(scroll3)\
        .perform()'''
    time.sleep(random.uniform(2, 3))
    review = driver.find_element(By.ID, 'continue-to-review')
    review.click()
    time.sleep(2)
    submit = driver.find_element(By.ID, 'place-order-trigger')
    driver.execute_script("arguments[0].click();", submit)

def main():
    try:
        driver = setup_driver()
    except Exception as e:
        print(f"Error: {e}")
        driver.quit()
        driver = setup_driver()
    url = "https://www.usa.canon.com/shop/p/eos-r10-rf-s18-150mm-f3-5-6-3-is-stm-lens-kit?color=Black&type=New"
    urlg7x = 'https://www.usa.canon.com/shop/p/powershot-g7-x-mark-iii?color=Black&type=New&srsltid=AfmBOoqNsvYKMQ0wAnJXLehRvdb8cdRG8J2NlL_ugcC4WIg63EngZ-Yv'
    try:
        while True:
            in_stock = check_stock_and_add_to_cart(driver, url)
            if in_stock:
                break
            driver.refresh()
            time.sleep(random.uniform(280, 300))  # Check every 5 minutes
    except Exception as e:
        print(f"Error: {e}")
    proceed_to_checkout(driver)
    shipping_details(driver)
    verify_address(driver)
    card_info(driver)
    final_step(driver)
    
main()