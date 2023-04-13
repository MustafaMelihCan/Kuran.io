
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#ayet = input('Please enter the name of the sure: ').lower()

def pagesetter():
    sureler = {'fatiha':'1'}
    sure_isim = input('Please enter the name of sure: ').lower()
    sure = sureler[sure_isim]
    ayet = input('Please enter the ayet number: ')
    driver.get(f"https://www.kuranmeali.com/AyetKarsilastirma.php?sure={sure}&ayet={ayet}")

pagesetter()
#time.sleep(5)
#print(driver.title)
Ahmet_Varol = driver.find_element(By.ID,'ahmetvarol')
print(Ahmet_Varol.text)
driver.close


""""
PATH = '/Users/mustafamelihcan/Applications/chromedriver'

driver = webdriver.Chrome(PATH)
driver = webdriver.Chrome(ChromeDriverManager(PATH).install())

driver.get('https://www.kuranmeali.com/AyetKarsilastirma.php?sure=2&ayet=3') 

"""