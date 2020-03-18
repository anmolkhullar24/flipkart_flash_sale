from selenium import webdriver
from requests import get
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("F:/WORK/chromedriver_win32/chromedriver_win32/chromedriver")
url = "https://www.flipkart.com/poco-f1-steel-blue-256-gb/p/itmf8qpcumze7msy?pid=MOBF85V7SSRXGFRZ&lid=LSTMOBF85V7SSRXGFRZYF68TE&marketplace=FLIPKART&srno=s_1_10&otracker=AS_QueryStore_OrganicAutoSuggest_0_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_0_6_na_na_na&fm=organic&iid=9166a6de-1d95-4de9-823a-2065b0dd214b.MOBF85V7SSRXGFRZ.SEARCH&ssid=rc5q8mhg9c0000001584519031461&qH=9b046b567ecc0251"
driver.get(url)
driver.implicitly_wait(10)
username = "7837223239"
password = "khullar123"
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