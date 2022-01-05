import unittest
from selenium import webdriver


class WebUnitTesting(unittest.TestCase):



    def setUp(self):

        self.driver = webdriver.Firefox (executable_path="D:\\Facultate\\VVS\\geckodriver.exe")
        self.base_url = "http://127.0.0.1:8080/"
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.driver = self.driver
        self.driver.get(self.base_url)




    def testIndexURL(self):
        self.get_url = self.driver.current_url
        self.assertIn(self.base_url, self.get_url)

    def testMainPageText(self):

        self.mainPage = self.driver.find_element_by_class_name("header")
        self.assertIn("May I take your order?", self.mainPage.text)

    def testPizzaExistence(self):

        self.link_pizza = self.driver.find_element_by_link_text("Pizza")
        self.assertIn("Pizza", self.link_pizza.text)

    def testPizzaClick(self):

        self.link_pizza = self.driver.find_element_by_link_text("Pizza")
        self.link_pizza.click()
        self.get_url = self.driver.current_url
        self.assertIn("http://127.0.0.1:8080/pizza", self.get_url)

    def testPizzaText(self):
        self.link_pizza = self.driver.find_element_by_link_text("Pizza")
        self.link_pizza.click()
        self.get_url = self.driver.current_url
        self.assertIn("http://127.0.0.1:8080/pizza", self.get_url)
        self.link_pizza = self.driver.find_element_by_class_name("header")
        self.assertIn("Enjoy your pizza", self.link_pizza.text)

    def testPizzaImage(self):
        self.link_pizza = self.driver.find_element_by_link_text("Pizza")
        self.link_pizza.click()
        self.get_url = self.driver.current_url
        self.assertIn("http://127.0.0.1:8080/pizza", self.get_url)
        self.link_pizza = self.driver.find_element_by_tag_name("link")
        self.assertIn("/static/pizza.css", self.link_pizza.get_attribute("href"))


    def testBreadExistence(self):
        self.link_bread = self.driver.find_element_by_link_text("Bread")
        self.assertIn("Bread", self.link_bread.text)

    def testBreadClick(self):
        self.link_bread = self.driver.find_element_by_link_text("Bread")
        self.link_bread.click()
        self.get_url = self.driver.current_url
        self.assertIn("http://127.0.0.1:8080/bread", self.get_url)

    def testBreadText(self):
        self.link_bread = self.driver.find_element_by_link_text("Bread")
        self.link_bread.click()
        self.get_url = self.driver.current_url
        self.assertIn("http://127.0.0.1:8080/bread", self.get_url)
        self.link_bread = self.driver.find_element_by_class_name("header")
        self.assertIn("Enjoy your bread", self.link_bread.text)
    def testBreadImage(self):
        self.link_bread = self.driver.find_element_by_link_text("Bread")
        self.link_bread.click()
        self.get_url = self.driver.current_url
        self.assertIn("http://127.0.0.1:8080/bread", self.get_url)
        self.link_bread = self.driver.find_element_by_tag_name("link")
        self.assertIn("/static/bread.css", self.link_bread.get_attribute("href"))





    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()