from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials



with open('gspreadinfo.json','r') as file:
    info = json.load(file)

#step5.언어팩 구글 스프레드 시트 연동
    # google platform 인증 keyfile
json_file_name = info['keyFile']
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name)
gc = gspread.authorize(credentials)

#리스트 불러올 URL 
spreadsheet_url = info['spreadsheetURL']
doc = gc.open_by_url(spreadsheet_url)
#구글 sheet 이름
worksheet = doc.worksheet(info['sheetName'])


#step3.크롬드라이버로 원하는 url로 접속
options = webdriver.ChromeOptions()
#클립 a2a 창을 열기 위해 유저에이전트가 모바일이여야 함 
options.add_argument("user-agent=Mozilla/5.0 (Linux; Android 9; SM-A530N Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.116 Mobile Safari/537.36;KAKAOTALK 1909000")
driver = webdriver.Chrome("./chromedriver", options = options)



def lauguagePack_verification(key) :
    lauguagePack_list = []
    if key == '1d1d_auctionGuide' : 
        driver.get('https://qa.klipdrops.com/1d1d/detail/2110652')
        time.sleep(3)
    elif key == '1d1d_editionGuide':
        driver.get('https://qa.klipdrops.com/1d1d/detail/999990014')
        time.sleep(3)
    elif key == 'dfactory_editionGuide':
        driver.get('https://qa.klipdrops.com/dfactory/detail/1112220259')
        time.sleep(3)
    elif key == 'market_auction':
        driver.get('https://qa.klipdrops.com/market/0xd801d5C72c996FF11812F50F85E18C7E34f51CFd/2110352')
        time.sleep(3)
    elif key == 'market_dfactory':
        driver.get('https://qa.klipdrops.com/dfactory/detail/1112220259')
        time.sleep(3)

    # auction 구글 시트 불러올 범위 설정
    print(info[key])
    for i in range(len(info[key])) :
        tempList = worksheet.range(info[key][i])
        for j in range(len(tempList)):
            if tempList[j].value != '' :
                lauguagePack_list.append(tempList[j].value)

    #옥션 구매 가이드 텍스트 추출 
    auction_guide = driver.find_elements(By.CLASS_NAME,"dot-text")
    # #옥션 구매 가이드 서브 
    # auction_guide_sub= driver.find_elements(By.CLASS_NAME,"dot-text")
    #옥션 
    # auction_guide_common = driver.find_element(By.CLASS_NAME, "dot-text impotant-message")

    auction_guide_list= []
    for i in auction_guide : 
        auction_guide_list.append(i.text)

    auctionG_PF = []
    for i in range(len(lauguagePack_list)) :
        if auction_guide_list[i] == lauguagePack_list[i] :
            auctionG_PF.append("p")
        else : 
            print("Fail")
            print("qa 환경:"+ auction_guide_list[i])
            print("실제 언어팩 :" + lauguagePack_list[i])
            auctionG_PF.append("F")
    if  "F" in auctionG_PF :
        print( key +': Fail')
    else: 
        print( key + ': Pass') 

#lauguagePack_verification('1d1d_auctionGuide')
lauguagePack_verification('1d1d_editionGuide')
lauguagePack_verification('dfactory_editionGuide')
lauguagePack_verification('market_1d1d')
lauguagePack_verification('market_auction')  
lauguagePack_verification('market_dfactory')  