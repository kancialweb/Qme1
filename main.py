from line_notify import LineNotify
from flask import Flask, send_file
import time
from selenium import webdriver
import chromedriver_binary
app = Flask(__name__)
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("window-size=1920,768")
options.add_argument("--no-sandbox")
browser = webdriver.Chrome(chrome_options=options)
#notify.send('ทดสอบ Loop For',sticker_id=1991,package_id=446)
@app.route("/")
def hello_world():
    i = 1
    while i in range(1,2):
        Access_Token_Pop = '8hCRHw1nO8yRlChEn5XlGNSE9RUEXSfVj7P6QIX7gVD'
        Access_Token_Peace = 'QLACyyfPjHuFIZl6scvwgAjAn0mjLLzv2dgNaePp7m2'
        notify_Pop = LineNotify(Access_Token_Pop)
        notify_Peace = LineNotify(Access_Token_Peace)
        browser.get("https://datastudio.google.com/embed/reporting/697e8976-a291-4e90-968b-b50fa3f80270/page/0YrJC")
        time.sleep(20)
        picture_path = "Report_CR.png"
        browser.save_screenshot(picture_path)
        time.sleep(1)
        times = time.strftime("%H:%M:%S")
        date = time.strftime("%d/%m/%y")
        notify_Pop.send("ครั้งที่ %d"%(i))
        notify_Pop.send("ทดสอบส่งรายงานการติดตั้งโครงการ Solar AIS BTS 2020 ภาคกลาง")
        notify_Pop.send("วันที่ %s เวลา %s"%(date,times),image_path=picture_path)
        #notify_Peace.send("ครั้งที่ %d" % (i))
        #notify_Peace.send("ทดสอบส่งรายงานการติดตั้งโครงการ Solar AIS BTS 2020 ภาคกลาง")
        #notify_Peace.send("วันที่ %s เวลา %s" % (date, times), image_path=picture_path)
        i = i+1
        time.sleep(1)
    #return send_file("spooky.png")
hello_world()
