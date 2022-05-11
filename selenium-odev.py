from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class LCWaikiki:

    # Locator
    HOMEPAGE_LOCATOR = (By.CLASS_NAME, "main-header-logo")
    CATEGORY_LOCATOR_STEP1 = (By.CLASS_NAME, "menu-header-item")
    CATEGORY_LOCATOR_STEP2 = (By.CLASS_NAME, "zone-item__anchor")
    PRODUCT_PAGE_LOCATOR = (By.CLASS_NAME, "product-price")
    PRODUCT_SIZE= (By.CSS_SELECTOR, "#option-size a")
    ADD_TO_CART= (By.ID, "pd_add_to_cart")
    CART_LOCATOR = (By.CLASS_NAME, "badge-circle")

    # Assert
    CATEGORY_ASSERT = (By.CLASS_NAME, "quick-filters__heading-text")
    CART_ASSERT = (By.CLASS_NAME, "coupon-code-link")
    HOMEPAGE_ASSERT = (By.CLASS_NAME, "order-track")

    website = "https://www.lcwaikiki.com/tr-TR/TR"

    def _init_(self):
        self.driver = webdriver.Chrome
        self.driver.maximize_window()
        self.driver.get(self.website)
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)

    def test_navigate(self):
        assert self.wait.until(
            ec.presence_of_element_located(self.HOMEPAGE_ASSERT)).is_displayed(), "not on home page"

        self.actions.move_to_element(self.wait.until(ec.presence_of_element_located(self.CATEGORY_LOCATOR_STEP1))).click(
            self.wait.until(ec.presence_of_element_located(self.CATEGORY_LOCATOR_STEP2))).perform()
        assert self.wait.until(
            ec.presence_of_element_located(self.CATEGORY_ASSERT)).is_displayed, "not on category page"

        self.wait.until(ec.presence_of_all_elements_located(self.PRODUCT_PAGE_LOCATOR))[7].click()
        assert self.wait.until(
            ec.presence_of_element_located(self.PRODUCT_SIZE)).is_displayed(), "not on product page"

        self.wait.until(ec.presence_of_all_elements_located(self.PRODUCT_SIZE))[1].click()
           
        self.wait.until(ec.presence_of_element_located(self.ADD_TO_CART)).click()
        assert int(
            self.wait.until(ec.presence_of_element_located(
                self.CART_LOCATOR)).text) > 0, "couldn't add product"

        self.wait.until(ec.presence_of_all_elements_located(self.CART_LOCATOR))[1].click()
        assert self.wait.until(
            ec.presence_of_element_located(self.CART_ASSERT)).is_displayed(), "not on the cart page"

        self.wait.until(ec.presence_of_element_located(self.HOMEPAGE_LOCATOR)).click()
        assert self.wait.until(
            ec.presence_of_element_located(self.HOMEPAGE_ASSERT)).is_displayed(), "not on the home page"
        
        self.driver.quit()


waikiki_test = LCWaikiki()
waikiki_test.test_navigate()
