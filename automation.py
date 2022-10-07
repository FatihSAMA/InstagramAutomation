from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from datetime import datetime
import os




def OpenBrowser():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()    


def Login(username, password):

    url = "https://www.instagram.com"
    driver.get(url)

    time.sleep(3)

    username_box = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')

    password_box = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')

    username_box.send_keys(username)
    password_box.send_keys(password)


    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()


    time.sleep(5)


def GetData():
    global  USD, EUR, gramAltin, BTC, ETH, sterlin

    driver.get("https://tr.tradingview.com/symbols/USDTRY/?exchange=FX")
    time.sleep(delayTime)
    USD = driver.find_element_by_css_selector('.tv-symbol-price-quote__value.js-symbol-last').text
    USD = round(float(USD),2)

    driver.get("https://tr.tradingview.com/symbols/EURTRY/?exchange=FX")
    time.sleep(delayTime)
    EUR = driver.find_element_by_css_selector('.tv-symbol-price-quote__value.js-symbol-last').text
    EUR = round(float(EUR),2)

    driver.get("https://tr.tradingview.com/symbols/FX_IDC-XAUTRYG/")
    time.sleep(delayTime)
    gramAltin = driver.find_element_by_css_selector('.tv-symbol-price-quote__value.js-symbol-last').text
    gramAltin = round(float(gramAltin),2)

    driver.get("https://tr.tradingview.com/symbols/BTCUSD/?exchange=BINANCE")
    time.sleep(delayTime)
    BTC = driver.find_element_by_css_selector('.tv-symbol-price-quote__value.js-symbol-last').text
    BTC = round(float(BTC),2)

    driver.get("https://tr.tradingview.com/symbols/ETHUSD/?exchange=BINANCE")
    time.sleep(delayTime)
    ETH = driver.find_element_by_css_selector('.tv-symbol-price-quote__value.js-symbol-last').text
    ETH = round(float(ETH),2)

    driver.get("https://tr.tradingview.com/symbols/GBPTRY/")
    time.sleep(delayTime)
    sterlin = driver.find_element_by_css_selector('.tv-symbol-price-quote__value.js-symbol-last').text
    sterlin = round(float(sterlin),2)


def ImageTemp():
    
    # img = Image.open(r"C:\Users\fatih\Desktop\Masaüstü\Programming\InstagramAutomation\template.png")
    # draw = ImageDraw.Draw(img)

    # font = ImageFont.truetype(r"C:\Windows\Fonts\Cambria\cambriab.ttf", 50)
    
    # draw.text((340, 380), f"{USD} TL", textColor, anchor="lm", font=font)
    # draw.text((340, 670), f"{EUR} TL", textColor, anchor="lm", font=font)
    # draw.text((340, 965), f"{BTC} $", textColor, anchor="lm", font=font)

    # draw.text((890, 380), f"{sterlin} TL", textColor, anchor="lm", font=font)
    # draw.text((890, 670), f"{gramAltin} TL", textColor, anchor="lm", font=font)
    # draw.text((890, 965), f"{ETH} $", textColor, anchor="lm", font=font)


    # now = datetime.now()
    # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # draw.text((430,105), f"{dt_string}", textColor, anchor="lm", font=font)

    img = Image.open(r"C:\Users\fatih\Desktop\Masaüstü\Programming\InstagramAutomation\template1.png")
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype(r"C:\Windows\Fonts\Cambria\cambriab.ttf", 25)
    draw.text((285, 400), f"{USD} TL", textColor, anchor="lm", font=font)
    draw.text((285, 600), f"{sterlin} TL", textColor, anchor="lm", font=font)
    draw.text((285, 800), f"{BTC} $", textColor, anchor="lm", font=font)

    draw.text((685, 400), f"{EUR} TL", textColor, anchor="lm", font=font)
    draw.text((685, 600), f"{gramAltin} TL", textColor, anchor="lm", font=font)
    draw.text((685, 800), f"{ETH} $", textColor, anchor="lm", font=font)


    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    hour = now.strftime("%H:%M:%S")
    font2 = ImageFont.truetype(r"C:\Windows\Fonts\Cambria\cambriab.ttf", 40)
    draw.text((380,215), f"{date}", textColor, anchor="lm", font=font2)
    draw.text((410,255), f"{hour}", textColor, anchor="lm", font=font2)


    img.save('output.png')


def InstaUpload(path):
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button').click()

    time.sleep(1)

    #driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button').click()

    time.sleep(1)

    driver.find_elements_by_tag_name('input')[-1].send_keys(path)

    time.sleep(2)

    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button').click()

    time.sleep(1)

    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button').click()

    time.sleep(1)

    descBox = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea')
    descBox.send_keys(description)

    time.sleep(1)

    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button').click()

    time.sleep(60)
     
    driver.close()

    
    
    
    
#app
textColor = (255,255,255)


delayTime = 3

description = """
#altın #dolar #euro #döviz #kur #money #para #türklirası 
#türk #gram #yatırım #alsat #finans #bütçe #banka #akbank 
#enpara #enparacom #işbankası #garantibankası #dollar #avro 
#exchange #holiday #turkey #btc #follow #eth #bitcoin
"""



username = input("Kullanıcı Adı: ")
password = input("Şifre: ")

path = os.getcwd()


waitTime = 60*60*3
while True:
    OpenBrowser()

    GetData()

    Login(username, password)

    ImageTemp()
    
    InstaUpload(path + "\\output.png")

    time.sleep(waitTime)




 


















