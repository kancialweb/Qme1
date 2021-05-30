from line_notify import LineNotify
from flask import Flask, send_file
import time
from selenium import webdriver
import chromedriver_binary
app = Flask(__name__)
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("window-size=1920,780")
options.add_argument("--no-sandbox")
browser = webdriver.Chrome(chrome_options=options)
@app.route("/")
def hello_world(checktime_status,times,date):
    if checktime_status == 1:
        Access_Token_Pop = '8hCRHw1nO8yRlChEn5XlGNSE9RUEXSfVj7P6QIX7gVD'
        Access_Token_Peace = 'QLACyyfPjHuFIZl6scvwgAjAn0mjLLzv2dgNaePp7m2'
        notify_Pop = LineNotify(Access_Token_Pop)
        notify_Peace = LineNotify(Access_Token_Peace)
        browser.get("https://datastudio.google.com/embed/reporting/697e8976-a291-4e90-968b-b50fa3f80270/page/0YrJC")
        time.sleep(40)
        try:
            picture_path = "Report_CR.png"
            browser.save_screenshot(picture_path)
            notify_Pop.send("ทดสอบส่งรายงานการติดตั้งโครงการ Solar AIS BTS 2020 ภาคกลาง")
            notify_Pop.send("วันที่ %s เวลา %s"%(date,times),image_path=picture_path)
            notify_Peace.send("ทดสอบส่งรายงานการติดตั้งโครงการ Solar AIS BTS 2020 ภาคกลาง")
            notify_Peace.send("วันที่ %s เวลา %s" % (date, times), image_path=picture_path)
            print("ส่งข้อมูลเข้า Line สำเร็จ")
        except:
            print("ส่งข้อมูลเข้า Line ไม่สำเร็จ")
@app.route("/")
def checktime():
    schedule_Hour = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    schedule_Minute = [0,15,30,45,60]
    H = int(time.strftime("%H"))
    M = int(time.strftime("%M"))
    times = time.strftime("%H:%M:%S")
    date = time.strftime("%d/%m/%y")
    check_M = 0
    if H in schedule_Hour and M in schedule_Minute:
        print("กำลังส่งข้อมูลไปใน Line")
        checktime_status = 1
    else:
        for i in range(0,len(schedule_Minute)):
            if M <= schedule_Minute[i]:
                check_M = schedule_Minute[i] - M
                break
        print("เหลือเวลาอีก : %d นาที" % check_M)
        checktime_status = 0
    return (checktime_status,times,date)
while True:
    checktime_status,times,date = checktime()
    hello_world(checktime_status,times,date)
    time.sleep(30)
