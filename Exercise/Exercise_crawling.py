import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://www.gopax.co.kr/exchange/btc-krw'


def crawl(self):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get(url)

    bitcoin_price = driver.find_element_by_class_name("TradingPair__currentPriceValue")
    print(bitcoin_price.text)