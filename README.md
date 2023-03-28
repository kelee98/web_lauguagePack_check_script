# CHECK_LAUAGE PACK

## 개요
- python3, selenium, gspread 를 이용하여 웹 페이지의 언어팩이 구글 시트의 언어팩 과 같은지 확인 하는 스크립트 
- check_purchaseGuid.py : 언어팩을 체크 하 웹페이지를 열어 주고 , 구글 스프레드 시트와 같으 확인 하는 스크립트 
- gspreadinfo.json : 구글 스프레드 시트 범위 를 저장 한 json 파일 
- healthy-dolphin-: 구글 스프레드 시트 연동 을 위한 json 파일 
## 사전 설치 필요 
- Python 3.8 이상
- 아래 명령어 실행해서 필수 python 모듈 설치 (IDE 사용 시 IDE 내에서 설치 가능함)
- $pip3 install selenium
- $pip3 install gspread
- $pip3 install --upgrade oauth2client (구글 인증에 필요한 설치)
- $pip3 install json

