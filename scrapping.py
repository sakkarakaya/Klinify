from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome("/Applications/chromedriver")
driver.get("https://www.google.de/maps/")
driver.maximize_window()
try:
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe")))
    agree = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="introAgreeButton"]/span/span')))
    agree.click()
except:
    print('Quiting Point 1')
    driver.quit()

Place = driver.find_element_by_class_name("tactile-searchbox-input")
Place.send_keys("Augenklinik Dr.Hoffmann")

sleep(3)
try:
    Submit = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button"))

    )
    Submit.click()
except:
    print('Quiting Point 1')
    driver.quit()

sleep(10)
try:
    KHaus_Submit = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/div[1]/div/a"))
    )
    KHaus_Submit.click()
except:
    print('Quiting Point 2')
    driver.quit()

sleep(3)
try:
    Adresse = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[8]/div[1]/button/div[1]/div[2]/div[1]"))

    )
    print(Adresse.text)
    Adresse = Adresse.text
except:
    print('Quiting Point 3')
    driver.quit()

sleep(3)
try:
    Kommentare = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[25]/div/div[2]/button"))
    )
    Kommentare.click()
except:
    print('Quiting Point 4')
    driver.quit()

sleep(3)
try:
    Sterne = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[3]/div[2]/div/div[2]/div[1]"))
    )
    print(Sterne.text)
    Sterne = Sterne.text
except:
    print('Quiting Point 5')
    driver.quit()

Komment = True
div_num = 1
Komment = []
while True:
    element = driver.find_element_by_xpath(
        "/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[3]")
    ActionChains(driver).move_to_element(element).click(element).perform()
    # element.send_keys(Keys.PAGE_DOWN)
    sleep(5)
    try:
        Click_More = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, f"/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[3]/div[9]/div[{div_num}]/div/div[3]/div[3]/jsl/button"))
        )
        Click_More.click()
    except:
        print(" --- ")
    try:
        Komment = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, f"/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[3]/div[9]/div[{div_num}]/div/div[3]/div[3]/div[2]/span[2]"))
        )
        Komment.append(Komment.text)

        print(Komment.text)
        Comment_Date = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, f"/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[3]/div[9]/div[{div_num}]/div/div[3]/div[3]/div[1]/span[3]"))
        )
        print(Comment_Date.text)
    except:
        print('Comment_Date could not be taken')
    div_num += 3
