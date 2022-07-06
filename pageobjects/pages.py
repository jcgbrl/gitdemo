from selenium.webdriver.common.by import By

class c_homepage:

    def __init__(self, driver):
        self.driver = driver

    booktitle1 = (By.XPATH, "//h2[text()='Test & Train Self-Study B2 First']")

    def m_booktitle1(self):
        return self.driver.find_element(*c_homepage.booktitle1).text

    bookprice1 = (By.XPATH, "//p[text()=' £ 20.00 ']")

    def m_bookprice1(self):
        return self.driver.find_element(*c_homepage.bookprice1).text

    addtocart1 = (By.XPATH, "(//button[text()=' Add to cart '])[1]")

    def m_addtocart(self):
        return self.driver.find_element(*c_homepage.addtocart1).click()

    cartitem = (By.XPATH, "//*[@id='app']/div[1]/header/div/div[1]/button")

    def m_cartitem(self):
        return self.driver.find_element(*c_homepage.cartitem).click()

class c_cartpage:

    def __init__(self, driver):
        self.driver = driver

    nbooktitle1 = (By.XPATH, "//*[@id='collapseProductList']/div/div[1]/div[2]/div[1]/div/a")

    def n_booktitle1(self):
        return self.driver.find_element(*c_cartpage.nbooktitle1).text
