#Author: Tirtha Subedi
#Purpose: Automate thru allegiantair website

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import re

#opening site on chrome
driver = webdriver.Chrome("/home/rajsubedi/Desktop/Projects/Python/AutomateTest/driver/chromedriver")      #this path has to be changed
driver.get("https://www.allegiantair.com")
time.sleep(3)


# close popup
closeBtn = driver.find_element_by_class_name("ui-dialog")
closeBtn = closeBtn.find_element_by_class_name("ui-dialog-titlebar-close").click()

# entering cities
elem = driver.find_element_by_name("search_form[departure_city]")
elem1 = driver.find_element_by_name("search_form[destination_city]")

#clearing the input field
elem.clear()
elem.send_keys("", Keys.RETURN)
elem1.clear()
elem1.send_keys("", Keys.RETURN)

# departure time
time.sleep(2)
dDate1 = driver.find_element_by_class_name("datepicker-toggle").click()
time.sleep(1)
elemPicker1 = driver.find_element_by_id("ui-datepicker-0-0-23").click()
dDate2 = driver.find_element_by_name("search_form[departure_date]")

# return date
time.sleep(2)
rDate = driver.find_element_by_css_selector(".return")
rDate.find_element_by_xpath(".//button[@class='datepicker-toggle']").click()
time.sleep(2)
elemPicker2 = rDate.find_element_by_id("ui-datepicker-0-0-30").click()
rDate2 = driver.find_element_by_name("search_form[return_date]")

# click on submit search button
time.sleep(1)
driver.find_element_by_id("submit-search").click()

# wait 10 seconds to make sure everything in the page is loaded
time.sleep(10)

page_url = driver.page_source

# finding first flight cost using Regex. Regex is used here because of the way it is coded in the website
firstFlightCost = re.findall(
    r"<span\s(?:class=\"element-invisible\">Priced\s*<\/span>\s*<span class=\"strikethrough\">\$(?:[\d]*)<sup class=\"medium-up-flights\">(?:.*)<\/sup>)<\/span>\s*\$([\d]*)<sup\s*class=\"medium-up-flights\">([\.\d]*)</sup>\s*</span>\s*</span>\s*</span>\s*<span class=\"flight-choose\">(?:[.]*)",
    page_url,
)

returnFlightCost = re.findall(
    r"<span class=\"mobile-only price\">\s*<span class=\"element-invisible\">Priced </span>\s*<span\s*class=\"strikethrough\">(?:.*)<sup>(?:.*)</sup></span>\s*\$([\d]*)<sup>([\.\d]*)</sup>\s*</span>",
    page_url,
)

firstFlightCostTotal = float(firstFlightCost[0][0]) + float(firstFlightCost[0][1])
returnFlightCostTotal = float(returnFlightCost[0][0]) + float(returnFlightCost[0][1])
totalFromForm = float(firstFlightCostTotal + returnFlightCostTotal)

driver.find_element_by_class_name("continue").click()

# Bundle page
time.sleep(5)
driver.find_element_by_class_name("no-item-selected").click()

# Hotel page
time.sleep(5)
driver.find_element_by_class_name("no-item-selected").click()

# Getting Aroung page
time.sleep(5)
driver.find_element_by_class_name("no-item-selected").click()

# Travelers page
time.sleep(5)
totalPriceFromWeb = driver.find_element_by_class_name("allegiant_models_price_total")
totalPriceFromWeb = totalPriceFromWeb.find_element_by_class_name("value").text
totalPriceFromWeb = float(re.findall(r"(?:\$)([\.\d]*)", totalPriceFromWeb)[0])

# printing price by calculating from flights page
print(
    "Departure price: ",
    firstFlightCostTotal,
    " | Return price: ",
    returnFlightCostTotal,
    " | Total Price: ",
    totalFromForm,
)
# printing price from travelers page total
print("Total Price Showing at Travelers Page: ", totalPriceFromWeb)

if totalFromForm == totalPriceFromWeb:
    print("Two Prices Matched!")
else:
    print("Two Prices Doesn't Matched!")

driver.close()
