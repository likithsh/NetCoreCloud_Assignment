import unittest
from selenium.webdriver import Chrome
from Flipkart_pageobjects import *
from Variables import *
import csv

class TestSearch(unittest.TestCase):
    def setUp(self):
        self.driver=Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get('https://www.flipkart.com')
        self.search=Flipkart_homepage(self.driver)

    def tearDown(self):
        self.driver.close()

# trying search the iphone mobiles.
    def Search_iphone_mobiles(self):
        self.driver.find_element_by_xpath(login_pop_cancel).click() #to cancel the login pop up which appears every time
        self.search.wait_for_Flipkart_website_to_launch()
        self.search.search_textbox().sendkey("iphone")
        self.search.click_search_button()

# trying to identify all the matching iphone mobiles.
    def searching_iphone_mobiles_with_50k_price(self):
        self.driver.find_element_by_xpath(login_pop_cancel).click()  # to cancel the login pop up which appears every time
        self.search.wait_for_Flipkart_website_to_launch()
        self.search.search_textbox().sendkey("iphone")
        self.search.click_search_button()
        self.search.Filter_price_dropdown_50k()
        self.search.getting_iphone_mobiles_max_50k_price()

# trying to take the names of all the matching iphone mobiles.
    def taking_model_names_of_the_iphone_mobiles(self):
        self.driver.find_element_by_xpath(login_pop_cancel).click()  # to cancel the login pop up which appears every time
        self.search.wait_for_Flipkart_website_to_launch()
        self.search.search_textbox().sendkey("iphone")
        self.search.click_search_button()
        self.search.Filter_price_dropdown_50k()
        self.search.getting_iphone_mobiles_model_names()

# trying to take the ratings of all the matching iphone mobiles.
    def taking_rating_of_the_iphone_mobiles(self):
        self.driver.find_element_by_xpath(login_pop_cancel).click()  # to cancel the login pop up which appears every time
        self.search.wait_for_Flipkart_website_to_launch()
        self.search.search_textbox().sendkey("iphone")
        self.search.click_search_button()
        self.search.Filter_price_dropdown_50k()
        self.search.getting_rating_of_mobiles()

# trying to write the results in csv file.
    def writing_into_csv_file(self):
        print(price)
        print(rating)
        print(Device_details)
        file = open("results.csv", "w")
        deatils= ["Device_details","price","ratings"]

        writer = csv.writer(file)
        writer.writerow(deatils)
        for a in range(len(rating)):
            writer.writerow([Device_details[a], price[a], rating[a]])
        file.close()









