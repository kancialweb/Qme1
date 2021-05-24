import time
from line_notify import LineNotify
#from flask import Flask, send_file
from selenium import webdriver

import chromedriver_binary  # Adds chromedriver binary to path
#app = Flask(__name__)

# The following options are required to make headless Chrome
# work in a Docker container
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("window-size=1920,768")
#chrome_options.add_argument("window-size=1920,1600")
chrome_options.add_argument("--no-sandbox")

# Initialize a new browser
browser = webdriver.Chrome(chrome_options=chrome_options)
#browser = webdriver.Chrome()


#@app.route("/")
def hello_world():
    i = 1
    while i in range(1,6):
        ACCESS_TOKEN_Pop = 'vqpQawiQ79yzM51NfPrbMqbWgzPPy6xHz2yNdsYtxxJ'
        ACCESS_TOKEN_Peace = 'QLACyyfPjHuFIZl6scvwgAjAn0mjLLzv2dgNaePp7m2'
        Notify_Pop = LineNotify(ACCESS_TOKEN_Pop)
        Notify_Peace = LineNotify(ACCESS_TOKEN_Peace)
        browser.get("https://datastudio.google.com/embed/reporting/697e8976-a291-4e90-968b-b50fa3f80270/page/0YrJC")
        #browser.get("https://www.youtube.com")
        time.sleep(30)
        browser.save_screenshot("spooky.png")
        time.sleep(5)
        date_current = time.strftime("%d/%m/%y")
        Notify_Pop.send("ทดสอบส่งรายงานการติดตั้ง โครงการ Solar AIS BTS 2020 รอบที่ %d"%i)
        Notify_Pop.send("วันที่ %s" %date_current, image_path="spooky.png")
        time.sleep(2)
        #Notify_Peace.send("ต้องส่งงานแบบนี้นะ ทดสอบรอบที่ %d"%i, image_path="spooky.png")
        time.sleep(5)
        i = i+1
    #return send_file("spooky.png")
hello_world()