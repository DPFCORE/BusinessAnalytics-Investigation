import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
np.set_printoptions(threshold=np.inf)



chrome_binary_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
CsvPath = r"D:\PYTHON_FILE\test.csv"
ExeclPath = r"D:\PYTHON_FILE\test3.xls"
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_binary_path
driver = webdriver.Chrome(options=chrome_options)

# f = open(CsvPath,'w',encoding="utf-16")
# Writer = csv.writer(f)

BinaryList = []

KeyWord = ["安全","大修","废物"]


for key in KeyWord:
    # Writer.writerow(key)
    BinaryList.append(["",f"{key}",""])
    driver.get("http://www.heneng.net.cn/")
    SearchBoard = driver.find_element(By.NAME,"search_key")
    SearchBoard.send_keys(key)
    time.sleep(1)
    driver.find_element(By.CLASS_NAME,"search_btn").click()

    for i in range(2,5):
        NewsList = driver.find_elements(By.CSS_SELECTOR,".last_box li")
        for li in NewsList:
            print(li.find_element(By.CLASS_NAME,"time").text)
            print(li.find_element(By.CLASS_NAME,"txt").text)
            print(li.find_element(By.CSS_SELECTOR,"a").get_attribute("href"))

            print("-------------------------------------------")

            list = [li.find_element(By.CLASS_NAME,"time").text,li.find_element(By.CLASS_NAME,"txt").text,li.find_element(By.CSS_SELECTOR,"a").get_attribute("href")]
            # Writer.writerow(list)
            BinaryList.append(list)
        driver.find_element(By.LINK_TEXT,f"{i}").click()

Df = pd.DataFrame(BinaryList)
Df.columns = ["日期","新闻","链接"]
Df.to_csv(ExeclPath,encoding='utf-16')
print(Df)