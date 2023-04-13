
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.kuranmeali.com/AyetKarsilastirma.php?sure=2&ayet=3")

#time.sleep(5)
#print(driver.title)
Ahmet_Varol = driver.find_element(By.ID,'ahmetvarol')
print(Ahmet_Varol)
driver.close


""""
PATH = '/Users/mustafamelihcan/Applications/chromedriver'

driver = webdriver.Chrome(PATH)
driver = webdriver.Chrome(ChromeDriverManager(PATH).install())

driver.get('https://www.kuranmeali.com/AyetKarsilastirma.php?sure=2&ayet=3') 

"""