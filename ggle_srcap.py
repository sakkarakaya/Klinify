from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome("/Applications/chromedriver")
driver.get("https://www.google.de/maps/@52.0845064,9.8930038,14z")
sleep(2)


Place = driver.find_element_by_class_name("tactile-searchbox-input")
Place.send_keys("Augenklinik Dr.Hoffmann")
Submit = driver.find_element_by_xpath(
    "/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
sleep(3)  # für die Seite vollig geladen sein
Submit.click()

sleep(10)
#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/div[1]/div/a"))).click();
KHaus_Submit = driver.find_element_by_xpath(
    "/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/div[1]/div/a")
sleep(10)

KHaus_Submit.click()

sleep(10)

Adresse = driver.find_element_by_xpath(
    "/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[8]/div[1]/button/div[1]/div[2]/div[1]")
print("Adresse:", Adresse.text)
