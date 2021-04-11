# API_Crawler
특허청_상표 정보 검색 서비스(https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15043964)  
특허청_디자인 정보 검색 서비스(https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15043970)  

Open API Clawler  

위 서비스를 사용하기 위해서 활용 신청 후 개인의 인증키를 사용하시길 바랍니다.

## Package
```
pip install Beutifulsoup4
pip install requests
pip install lxml
```

## How to...
```
Choose Type: 1. Mark 2. Design... :
```
상표 이미지는 1, 디자인 이미지는 2 입력

```
keyword... :
```
찾고자 하는 관련 단어 입력

```
for page_num in range(__,int(total_page))
```
Line 41, 75의 페이지 넘버를 사용하여 크롤링 시작 페이지 지정 가능

1페이지의 100개의 item 출력하므로 참고하여 __ 부분에 시작페이지 입력
