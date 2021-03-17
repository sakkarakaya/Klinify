from selenium import webdriver
#import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/Users/MEHMET/Downloads/chromedriver")

names=[] #List to store name of the product
adresses=[] #List to store price of the product
ratings=[] #List to store rating of the product

url = "https://www.klinikbewertungen.de/klinik-forum/krankenhaus-suche?selText=&selRadius=Hannover&selFB=_void_"
driver.get(url)


content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
for a in soup.findAll('article', attrs={'class':'js-klinik-row standard'}):
    name = a.find('a',href=True)
    names.append(name.text)
    adres = a.find('section', attrs={'class': 'content'})
    adresses.append(adres.text)
    rating = EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[3]/div[1]/div[3]/div[2]/article[7]/section[2]/dl/dd[1]/img"))
    ratings.append(rating)






# content = driver.page_source
# soup = BeautifulSoup(content)
# for a in soup.findAll('article', attrs={'class':'js-klinik-row standard'}):
#name = a.find('article', attrs={'class':'js-klinik-row standard'})
# price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
# rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    
# prices.append(price.text)
# ratings.append(rating.text) 
print(names)