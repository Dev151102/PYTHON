from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Create the WebDriver instance (e.g., Chrome, Firefox, Safari)
    driver = webdriver.Safari()
    
    # Optional: Add any additional setup code for the driver
    
    # Return the driver instance to be used in the test functions
    yield driver
    
    # Optional: Add any teardown code for the driver
    driver.quit()


def test_search_functionality(driver):
    # Open the website
    driver.get("https://www.youtube.com")

    # Wait for the search input element to be visible
    search_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input#search"))
    )

    # Perform search actions
    search_input.send_keys("test")
    search_input.submit()

    # ... continue with your assertions and test logic

def test_navigation_links(driver):
    # Open the website
    driver.get("https://www.google.com")
    
    # Perform click action on navigation link
    link_about = driver.find_element(By.LINK_TEXT, "About")
    link_about.click()
    
    # Perform assertion on page URL after navigation
    assert driver.current_url == "https://about.google/?utm_source=google-IN&utm_medium=referral&utm_campaign=hp-footer&fg=1"
