from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from Variables import *
import time

price = []
Device_details = []
rating = []
class Flipkart_homepage():

    def __init__(self,driver):
        self.driver=driver

    def wait_for_Flipkart_website_to_launch(self):
        wait=WebDriverWait(driver=self.driver,timeout=30)
        wait.until(expected_conditions.title_contains(self.driver.find_element_by_xpath(Filpkart_website)))

# this method will identify the serach textbox
    def search_textbox(self):
        try:
            return self.driver.find_element_by_name("q")

        except:
            return None

#this method will click on the serach button
    def click_search_button(self):
        try:
            return self.driver.find_element_by_xpath(search_button).click()
        except:
            return None

#this methid will help us to select the drop down item.
    def Filter_price_dropdown_50k(self):
        try:
            filter_drop_down=self.driver.find_element_by_xpath(filter_drop)
            filter=Select(filter_drop_down)
            filter.select_by_value("50000")
        except:
            print("not able to select the value")

#this methid will help us to get all the iphone mobiles below 50k
    def getting_iphone_mobiles_max_50k_price(self):
        try:
            n = self.driver.find_elements_by_xpath(mobiles_with_price_50k)

            for i in range(0, len(n)):
                e1 = n[i].text
                price.append(e1)
            print(price)

        except:
            print("No matching mobiles are searched")


#this methid will help us to get all the iphone mobile model names below 50k
    def getting_iphone_mobiles_model_names(self):
        try:
            r = self.driver.find_elements_by_xpath(mobiles_model_names)

            for i in range(0, len(r)):
                e2 = r[i].text
                Device_details.append(e2)
            print(Device_details)

        except:
            print("no matching names of mabiles are searched")

#this methid will help us to get all the iphone mobiles ratings below 50k
    def getting_rating_of_mobiles(self):
        try:
            s = self.driver.find_elements_by_xpath(rating_of_mobiles)
            for i in range(0, len(s)):
                e2 = s[i].text
                rating.append(e2)
            print(rating)

        except:
            print("no matching rating got serached")





