from selenium import webdriver
from selenium. webdriver. chrome. options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

product_URL = "Paste an Amazon product here"
# product_URL = "https://www.amazon.com/REDMAGIC-Android-Smartphone-Snapdragon-Unlocked/dp/B09XGXMY66/ref=sr_1_3?keywords=RedMagic%2B5G&sr=8-3&th=1"


chrome_driver_path = "Paste here your web driver path"
# brave_browser_path = '/usr/bin/brave-browser'

chrome_options = Options()
# chrome_options.binary_location = brave_browser_path
chrome_options. add_experimental_option("detach", True)

service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url=product_URL)

item = driver.find_element(
    By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[1]/span[1]')


print(item)
print(item.get_attribute('innerHTML'))


driver.close()
