import requests
from bs4 import BeautifulSoup as bs
import urllib.request
import os

class Crawler:
  def __init__(self):
    self.option = int(input('Choose Type: 1. Mark 2. Design... : '))  # Choose search type
    self.keyword = str(input('keyword... : '))  # image keyword for search
    self.dirPath = ""  # image stored directory

  def create_new_directory(self):

    self.cwd = os.getcwd()
    self.dirPath = os.path.join(self.cwd, self.keyword)

    if not os.path.exists(self.dirPath):
      os.mkdir(self.dirPath)

  def Markinfo(self):
    key = '' # Your own service key...
    necessary = '?serviceKey=' + key + '&freeSearch=' + self.keyword
    option = '&numOfRows=100&application=true&registration=true&refused=true' \
             '&expiration=true&refused=true&expiration=true&withdrawal=true' \
             '&publication=true&cancel=true&abandonment=true&trademark=true' \
             '&serviceMark=true&trademarkServiceMark=true&businessEmblem=true' \
             '&collectiveMark=true&internationalMark=true&character=true&figure=true' \
             '&compositionCharacter=true&figureComposition=true'

    url = 'http://kipo-api.kipi.or.kr/openapi/service/trademarkInfoSearchService/getAdvancedSearch'

    req = requests.get(url + necessary + option).content
    soup = bs(req, 'lxml-xml')

    data_count = soup.find_all('count')

    for count in data_count:
      total_data = count.totalCount.text
      total_page = int(total_data)/100 + 1

    for page_num in range(1,int(total_page)): # You can choose start page
      new_req = requests.get((url + necessary + '&pageNo=' + str(page_num) + option))
      new_soup = bs(new_req.content, 'lxml-xml')

      data = new_soup.find_all('item')

      for item in data:
        appnum = item.applicationNumber.text
        link = item.bigDrawing.text
        if link == '':
          continue

        save_path = self.dirPath + '/' + appnum + '.jpg'
        urllib.request.urlretrieve(link, save_path)


  def Designinfo(self):
    key = '' # Your own service key...

    necessary = '?serviceKey=' + key + '&articleName=' + self.keyword
    option = '&numOfRows=100'

    url = 'http://kipo-api.kipi.or.kr/openapi/service/designInfoSearchService/getWordSearch'

    req = requests.get(url + necessary + option).content
    soup = bs(req, 'lxml-xml')

    data_count = soup.find_all('count')

    for count in data_count:
      total_data = count.totalCount.text
      total_page = int(total_data) / 100 + 1

    for page_num in range(1, int(total_page)): # You can choose start page
      new_req = requests.get((url + necessary + '&pageNo=' + str(page_num) + option))
      new_soup = bs(new_req.content, 'lxml-xml')

      data = new_soup.find_all('item')

      for item in data:
        appnum = item.applicationNumber.text
        try:
          link = item.imagePathLarge.text
        except AttributeError or ValueError:
          continue

        save_path = self.dirPath + '/' + appnum + '.jpg'
        urllib.request.urlretrieve(link, save_path)


  def run(self):

    self.create_new_directory()
    if self.option == 1:
      self.Markinfo()

    elif self.option == 2:
      self.Designinfo()

    else:
      print("wrong type")

if __name__ == '__main__':
  newCrawler = Crawler()
  newCrawler.run()



