# API_Crawler

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
