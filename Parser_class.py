from bs4 import BeautifulSoup
import urllib.request

class Parser:
  raw_html = ''
  html = ''
  results = []

  def __init__(self, url, path):
    self.url = url
    self.path = path

  def get_html(self):
    req = urllib.request.urlopen(self.url)
    self.raw_html = req.read()
    self.html = BeautifulSoup(self.raw_html, 'html.parser')

  def run(self):
    self.get_html()

# soup = BeautifulSoup(html, 'html.parser')
# news = soup.find_all('li', class_='liga-news-item')

# for item in news:
#   title = item.find('span', class_='d-block').get_text(strip=True)
#   desc = item.find('span', class_='name-dop').get_text(strip=True)
#   href = item.a.get('href')
#   results.append({
#     'title': title,
#     'desc': desc,
#     'href': href
#   })

# f = open('news.txt', 'w', encoding='utf-8')
# i = 1
# for item in results:
#   f.write(f'Новость № {i}\n\nНазвание: {item["title"]}\nОписание: {item["desc"]}\nСсылка: {item["href"]}\n\n*******************************\n')
#   i += 1
# f.close()