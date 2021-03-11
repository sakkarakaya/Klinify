from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("/Users/MEHMET/Downloads/chromedriver")
url = "https://www.google.it/maps/place/Pantheon/@41.8986108,12.4746842,17z/data=!3m1!4b1!4m7!3m6!1s0x132f604f678640a9:0xcad165fa2036ce2c!8m2!3d41.8986108!4d12.4768729!9m1!1b1"
url2 = "https://www.google.com/maps/place/Augenklinik+Dr.+Hoffmann/@52.2555789,10.5275976,15z/data=!4m7!3m6!1s0x0:0xe66ee9e189648187!8m2!3d52.2555789!4d10.5275976!9m1!1b1"
driver.get(url2)