from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd


df = pd.read_excel('Klinikliste.xlsx')


driver = webdriver.Chrome("/Applications/chromedriver")

namen = []
adressen = []
sternen = []
alle_daten = []

def scrapping(klinik_url):

    driver.get(klinik_url)
    driver.maximize_window()

    ''' Exit from Google's Agree verification '''
    try:
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe")))
        agree = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="introAgreeButton"]/span/span')))
        agree.click()
    except:
        print('-----')

    sleep(5)

    try:
        Name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/h1/span[1]'))

        )
        print(Name.text)
        Name = Name.text

        sleep(3)

        Adresse = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div.ugiz4pqJLAG__primary-text.gm2-body-2")))
        print(Adresse.text)
        Adresse = Adresse.text
    except:
        print('Quiting Point 2')
        driver.quit()

    sleep(3)
    try:
        Stern = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "span.section-star-display"))

        )
        print(Stern.text)
        Stern = Stern.text
    except:
        print('Quiting Point 4')
        driver.quit()
    try:
        Kommentare = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "button.widget-pane-link"))

        )
        Kommentare.click()
    except:
        print('Quiting Point 3')
        driver.quit()

    sleep(5)

    Komment = True
    div_num = 1
    komment = []
    comment_date = []
    likes = []
    finish = 0

    while True:

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
            komment.append(Komment.text)
            print(Komment.text)
            sleep(3)
            Comment_Date = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[3]/div[9]/div[{div_num}]/div/div[3]/div[3]/div[1]/span[3]"))
            )
            comment_date.append(Comment_Date)
            print(Comment_Date.text)
            try:
                like = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, f"/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[3]/div[9]/div[{div_num}]/div/div[3]/div[3]/div[7]/button[2]/span/span[2]"))
                )

                likes.append(like.text)
                print(like.text)
            except:
                likes.append(0)
                print("Gibt keine likes")
        except:
            print('Comment_Date could not be taken')
            finish += 1
            if finish == 5:
                break
            else:
                continue
        sleep(3)
        div_num += 3

    einzelne = {
        'Namen': Name,
        'Adresse': Adresse,
        'Sterne': Stern,
        'Kommentare': komment,
        'Datum': comment_date,
        'Likes': likes
    }
    return einzelne


def get_data(links):
    for link in links:
        daten_einzelne = scrapping(link)
        alle_daten.append(daten_einzelne)

    return alle_daten


def make_csv():
    daten = get_data(df['Link Google Maps'])
    data_frame = pd.DataFrame(daten)
    daten.to_csv('bewertungen_google_maps.csv')


make_csv()
