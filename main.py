from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import os, time, requests
my_secret = os.environ['googlepassword']
ready = False
conjnumber = 0

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)


driver.get("https://conjuguemos.com/auth/login")
#usernam = driver.find_element(By.NAME, 'identity')
#usernam.send_keys("ok")

#main_page = driver.current_window_handle

#click the cookie accept button
bruhcookie = driver.find_element(By.XPATH, "/html/body/div/div/div/button")
bruhcookie.click()

#click the sign in with google button
#aight = driver.find_element(By.CLASS_NAME, "abcRioButtonContentWrapper")
#aight.click()
#sleep(2)

#for handle in driver.window_handles:
    #if handle != main_page:
        #login_page = handle

#switches from the conjuguemos window to the google login window
#driver.switch_to.window(login_page)
#select the google window and input username & pass
#amongus = driver.find_element(By.TAG_NAME, "input")
#amongus.send_keys("25ct4645@medinabees.org" + Keys.ENTER)
#sleep(5)
#amongus.send_keys(my_secret)

#input username and password on the native login
username = driver.find_element(By.ID, "identity").send_keys("25ct4645@medinabees.org")

password = driver.find_element(By.ID, "password").send_keys(my_secret)

submit = driver.find_element(By.ID, "login_btn").click()

oof = input("Are you logged in?[type 'yes' when done]: \n")
if oof == "yes":
  #driver.switch_to.window(main_page)
  oof2 = input("What number conjuguemos would you like to do?: \n")
  conjnumber = int(oof2)
  driver.execute_script("window.scrollTo(0,300);")

if conjnumber > 0:
  ready = True


if ready == True:
  #bruh = driver.find_element(By.TAG_NAME, "body")
  #bruh.send_keys(Keys.CONTROL, "f")
  #webdriver.ActionChains(driver).send_keys(Keys.CONTROL, "f").perform()

  matched_elements = driver.find_elements(By.CLASS_NAME, "row-number")
#gets all the availible conjuguemoses on the main page
  texts = []
for matched_element in matched_elements:
    text = matched_element.text
    texts.append(text)

#find the number conjuguemos from the number inputted
amog = texts[conjnumber - 1]
#remove the excess letters and whitespace
amogstripped = amog.strip("VC").strip()
print(amogstripped)

#find the conjuguemos wanted and click it
que = driver.find_element(By.LINK_TEXT, amogstripped).click()
sleep(1)


#click on the dropdown box and copy the vocab list link
voclist = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[3]/div[1]/div/div[1]").click()
vooclist2 = driver.find_element(By.LINK_TEXT, "Vocabulary List").get_attribute("href")
print(vooclist2)
bruhworkalready = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[3]/div[1]/div/div[1]").click()

#press the buttons needed to start 
gradedpracticebutton = driver.find_element(By.XPATH, "//*[@id='practice']").click()
timerbutton = driver.find_element(By.ID, "timer-checkbox").click()
startpracticebutton = driver.find_element(By.XPATH, "//*[@id='timerModal']/div/div[2]/button").click()

oof2 = input("Ready?[type 'yes'] when ready to start: \n")



if oof2 == "yes":
  questiontext = driver.find_element(By.ID, "question-input").text
  print(questiontext)
  
pdtest = pd.read_html(vooclist2)
print(pdtest)






