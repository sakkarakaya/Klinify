# tüm div class section-layout section-layout-root
# section-layout tüm comments
# bir yorum content section-review-review-content
# section-review-stars aria-label = 5 sterne
# section-review-publish-date
# section-review-review-content
# section-review-owner-response
# section-review-owner-response-subtitle ----date
# section-review-text
# more tuşu section-expand-review blue-link try --- except ---
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

sleep(5)
try:
    Kommentare = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/span[1]/span/span/span[2]/span[1]/button"))
    )
    Kommentare.click()
except:
    print('Quiting Point 3')
    driver.quit()

sleep(10)

for i in range(5):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    sleep(5)
    print(f"{i} nci scroll")

contents = driver.find_elements_by_class_name('section-review-review-content')
print(len(contents))
for content in contents:
    sleep(5)
    print(content)
    comment = content.find_element_by_class_name('section-review-text').text
    print(comment)
