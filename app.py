from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests

ID = '8rZov7pqM1E'
path="chromedriver.exe"
options = Options()
options.headless = True
driver=webdriver.Chrome(executable_path=path,options=options)
driver.get('file:///C:/My%20Web%20Sites/splitter%20api/thepirat000.github.io/spleeter-api/index.html')
driver.find_element_by_id("url").send_keys(f'https://www.youtube.com/watch?v={ID}')
driver.find_element_by_id("btn-split").click()

if driver.execute_script("document.getElementById('wait-dialog').style.display")==None:
    data = requests.get(f'https://spleeter.westus.cloudapp.azure.com/yt/d/4stems/{ID}?sub=other&ext=.mp3&hf=true')
    print(len(data.content))
