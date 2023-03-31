from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
import time
 
# instantiate options 
options = webdriver.ChromeOptions() 
 
# run browser in headless mode 
options.headless = True 
 
# instantiate driver 
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install()), options=options) 
 
# load website 
url = 'https://twitter.com/' 
 
# get the entire website content 
driver.get(url) 
 
# instantiate items 
items = [] 
 
# instantiate height of webpage 
last_height = driver.execute_script('return document.body.scrollHeight') 
 
# set target count 
itemTargetCount = 20 
 
# scroll to bottom of webpage 
while itemTargetCount > len(items): 
	driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') 
 
	# wait for content to load 
	time.sleep(1) 
 
	new_height = driver.execute_script('return document.body.scrollHeight') 
 
	if new_height == last_height: 
		break 
 
	last_height == new_height 
 
	# select elements by XPath 
	elements = driver.find_elements(By.XPATH, "//*[@id="id__45gjyugqia6"]/div[1]/div/a/div/div[1]") 
	h4_texts = [element.text for element in elements] 
 
	items.extend(h4_texts) 
 
	# print title 
	print(h4_texts)