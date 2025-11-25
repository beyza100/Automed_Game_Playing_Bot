from selenium import webdriver
from selenium.common import NoSuchDriverException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

time.sleep(3)

try:
    language_button= driver.find_element(By.ID, value="langSelect-EN")
    language_button.click()
    print("it is found button")
    time.sleep(3)
except NoSuchDriverException:
    print("not found button")

time.sleep(2)

cookie=driver.find_element(By.ID,value="bigCookie")

wait_time=5
timeout=time.time()+wait_time
five_min=time.time()+60*5

while True:
    grade=cookie.click()
    if time.time()>timeout:
        try:
            time.sleep(1)
            cookies_element=driver.find_element(By.ID,value="cookies")
            cookie_text=cookies_element.text
            cookie_count=int(cookie_text.split()[0].replace(",",""))


            products=driver.find_elements(By.ID,value="products")

            best_item=None

            for i in reversed(products):
                if "enabled" in i.get_attribute("class"):
                    best_item=i
                    break


            if best_item:
                best_item.click()
                print("it is bought")

        except(NoSuchElementException,ValueError):
            print("not found")

    timeout = time.time() + wait_time



    if time.time() > five_min:
        try:
            cookie_element=driver.find_element(By.ID,value="cookies")
            print(f"final result: { cookie_element.text}")
        except NoSuchElementException:
            print("couldnt get cookies")
        break



























