from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome("/Applications/chromedriver")
driver.get("https://www.google.com/maps/place/Augenklinik+Dr.+Hoffmann/@52.2555789,10.5275976,15z/data=!4m2!3m1!1s0x0:0xe66ee9e189648187?sa=X&ved=2ahUKEwiUrOzD5_DuAhVLDOwKHUVOACkQ_BIwDHoECBgQBQ")
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

sleep(5)
try:
    Adresse = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[8]/div[1]/button/div[1]/div[2]/div[1]"))

    )
    print(Adresse.text)
    Adresse = Adresse.text
except:
    print('Quiting Point 2')
    driver.quit()

sleep(3)
try:
    Kommentare = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[25]/div/div[2]/button"))
    )
    Kommentare.click()
except:
    print('Quiting Point 3')
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
    print('Quiting Point 4')
    driver.quit()

Komment = True
div_num = 1
Komment = []
'''for i in range(5):
    element = driver.find_element_by_xpath(
        "/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[3]")
    ActionChains(driver).move_to_element(element).click(element).perform()
    # element.send_keys(Keys.PAGE_DOWN)
    sleep(5)
    print(f"{i} nci scroll")'''
while True:
    '''scroll_active_friends_list = WebDriverWait(driver, 40).until(EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="pane"]/div')))

                scroll_active_friends_list.location_once_scrolled_into_view'''
    scrollable_div = driver.find_element_by_css_selector(
        'div.section-layout.section-scrollbox.scrollable-y.scrollable-show'
    )
    driver.execute_script(
        'arguments[0].scrollTop = arguments[0].scrollHeight',
        scrollable_div
    )
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
        # Komment.append(Komment.text)
        print(Komment.text)
        sleep(3)
        Comment_Date = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, f"/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[3]/div[9]/div[{div_num}]/div/div[3]/div[3]/div[1]/span[3]"))
        )
        print(Comment_Date.text)
    except:
        print('Comment_Date could not be taken')
    sleep(3)
    '''element = driver.find_element_by_xpath(
                    "/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[3]")
                ActionChains(driver).move_to_element(element).click(element).perform()'''
    div_num += 3
