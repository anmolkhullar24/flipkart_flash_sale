from selenium import webdriver
from requests import get
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("chrome driver location")
url = "enter url"
driver.get(url)
driver.implicitly_wait(10)
username = "email id / phone number"
password = "enter password"
def buy_now():
    while True:
        # response = get(url)
        if "BUY NOW" in driver.page_source:
            driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[2]/form[1]/button[1]").click()
            break
        else:
            driver.refresh()
            print("refresh")
def login():
    if "Enter Email/Mobile number" in driver.page_source:
        driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]").send_keys(username)
        driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/button[1]").click()
    else :
        driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]").send_keys(username)
        driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/button[1]").click()
        driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/input[1]").send_keys(password)
        driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[3]/button[1]").click()
        
def delivery():
    driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/label[1]/div[2]/div[1]/div[1]/button[1]").click()

def order_confim():
    driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/span[2]/button[1]").click()


buy_now()
login()
delivery()
order_confim()