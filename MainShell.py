
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def SureToNumber():
    driver.get("https://www.kuranmeali.com/AyetKarsilastirma.php?sure=1&ayet=1")
    selection = driver.find_element(By.ID,'Meal/AyetSec')
    print(selection.text)


def pagesetter():
    sureler = {'fatiha':'1',
               'bakara':'2',
               'al-i imran':'3',
               'nisa':'4',
               'maide':'5',
               "en'am":'6',
               "a'raf":'7',
               }
    sure_isim = input('Please enter the name of sure: ').lower()
    sure = sureler[sure_isim]
    ayet = input('Please enter the ayet number: ')
    driver.get(f"https://www.kuranmeali.com/AyetKarsilastirma.php?sure={sure}&ayet={ayet}")

L1 = ['Ahmet_Varol']
class CEVIRI:
    list = L1
    def __init__(self, name, translation):
        self.name = name
        self.translation = translation
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