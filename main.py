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
    key = 'l8gBL3d0H0uEerbEKxYRva%2FQUSZQ3YXR9A9qGkFO7btByiwP09y2PfQc2Utg2cM%2FhChr3n44WtFPEJizwFrlwA%3D%3D'
    necessary = '?serviceKey=' + key + '&freeSearch=' + self.keyword
    option = '&application=true&registration=true&refused=true' \
             '&expiration=true&refused=true&expiration=true&withdrawal=true' \
             '&publication=true&cancel=true&abandonment=true&trademark=true' \
             '&serviceMark=true&trademarkServiceMark=true&businessEmblem=true' \
             '&collectiveMark=true&internationalMark=true&character=true&figure=true' \
             '&compositionCharacter=true&figureComposition=true'

    url = 'http://kipo-api.kipi.or.kr/openapi/service/trademarkInfoSearchService/getAdvancedSearch'

    req = requests.get(url + necessary + option).content
    soup = bs(req, 'lxml-xml')

    data = soup.find_all('item')

    for item in data:
      appnum = item.applicationNumber.text
      link = item.bigDrawing.text

      save_path = self.dirPath + '/' + str(appnum) + '.jpg'
      urllib.request.urlretrieve(link,save_path)

  def Designinfo(self):
    key = 'l8gBL3d0H0uEerbEKxYRva%2FQUSZQ3YXR9A9qGkFO7btByiwP09y2PfQc2Utg2cM%2FhChr3n44WtFPEJizwFrlwA%3D%3D'
    necessary = '?serviceKey=' + key + '&freeSearch=' + self.keyword
    option = '&open=true&rejection=true&destroy=true' \
             '&cancle=true&notice=true&registration=true&invalid=true' \
             '&abandonment=true&simi=true' \
             '&part=true&etc=true&destroy=소멸'

    url = 'http://kipo-api.kipi.or.kr/openapi/service/designInfoSearchService/getAdvancedSearch'

    req = requests.get(url + necessary + option).content
    soup = bs(req, 'lxml-xml')

    data = soup.find_all('item')

    for item in data:
      appnum = item.applicationNumber.text
      link = item.imagePathLarge.text

      save_path = self.dirPath + '/' + str(appnum) + '.jpg'
      urllib.request.urlretrieve(link,save_path)

  def run(self):
    """
        main routines
        :return:
        """
    self.create_new_directory()
    if self.option == 1:
      self.Markinfo()

    elif self.option == 2:
      self.Designinfo()

    else:
      print("wrong type")

if __name__ == '__main__':
  newCrawler = Crawler()  # create new crawler
  newCrawler.run()



