from pageobjects.pages import c_homepage, c_cartpage
from utilities.baseclass import baseclass
import time
booktitle1 = None

class TestScenarioOne(baseclass):  # every class name should have a test on it

    def test_shopfront_homepage(self):

        global booktitle1

        homepage = c_homepage(self.driver)

        # STORE BOOK 1 TITLE
        booktitle1 = homepage.m_booktitle1()
        print(booktitle1)

        # STORE BOOK 1 PRICE
        bookprice1 = homepage.m_bookprice1()
        print(bookprice1)

        # CLICK ADD TO CART
        homepage.m_addtocart()
        time.sleep(5)

        # CLICK CART ITEM
        homepage.m_cartitem()
        time.sleep(5)

    def test_shopfront_cartpage(self):

        cartpage = c_cartpage(self.driver)

        # STORE BOOK 1 TITLE
        cartpage_booktitle1 = cartpage.n_booktitle1()
        print(cartpage_booktitle1)

        #  VERIFY THE BOOK 1 TITLE IN CART PAGE
        assert cartpage_booktitle1 == booktitle1
