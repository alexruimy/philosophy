from bs4 import BeautifulSoup
import requests
from sys import argv
import urllib

class PhilosophyFinder:

  base_url = "https://en.wikipedia.org/wiki/"
  random_page = "Special:Random"
  goal = "Philosophy"
  not_found = "Article not found"

  request_count = 0
  max_depth = 999
  depth = 1
  start = None

  quiet = False
  history = []
  complete = False
  cache_file = '.wordpairs'

  def __init__(self):
    self.wordpairs = self._read_wordpairs()


  def find(self, search=''):

    if search == '' or search == None:
      search = self.random_page

    if not self.quiet and search and search != self.random_page:
      self._log(search)

    if search == self.goal:
      self._save_wordpairs()
      self._log("%s -> %s in %d clicks (%d requests)" % (self.start, self.goal, self.depth, self.request_count), False)
      self.complete = True
      return self.depth

    if search in self.wordpairs.keys():

      if search != self.random_page:
        self.depth+= 1
        return self.find(self.wordpairs[search])

    if search == self.not_found or search == None:
      self.complete = True
      self._log("ERROR: Article not found (%s)" % search)

    if search:
      result = self.crawl(search)
      if not result:
        print('no')
        return self.find(search)

      if result in self.history:
        self.complete = True
        self._log("ERROR: Caught in loop (%s)" % result)

      if self.depth > self.max_depth:
        self.complete = True
        self._log("ERROR: Max depth exceeded")

      if result and search != self.random_page:
        self.wordpairs[search] = result
        self.request_count+= 1

      if search != self.random_page:
        self.depth+= 1

      return self.find(result)


  def crawl(self, search):

    self.history.append(search)

    url = self.base_url + search.replace(" ","_")
    r = requests.get(url)
    html = r.content

    if search == self.random_page:
      self.start = r.url.split('/')[-1]

    soup = BeautifulSoup(html, 'html.parser')

    for i in soup.find_all('span', class_ = 'IPA'):
      i.decompose()

    for i in soup.find_all('i'):
      i.decompose()

    body_text = soup.find(id='mw-content-text')
    paragraphs = body_text.find_all('p')
    lis = body_text.find_all('li')
    tables = body_text.find_all('table')

    for paragraph in paragraphs + lis + tables:

      links = paragraph.find_all('a', {'href': lambda l: l and l.startswith('/wiki/')})

      for link in links:
        if link['title']:
          if self.balanced_parens(str(link), str(body_text)):
            return link['title']

    return False


  def balanced_parens(self, link, body_text):

    text = body_text.split(link)[0]
    opened = text.count('(')
    closed = text.count(')')
    return opened == closed


  def _log(self, msg, indent=True):

    if not msg.startswith('ERROR'):
      if indent:
        msg = ''.join(['-' for i in range(self.depth)]) + msg
      msg = msg.replace('_', ' ')
      msg = urllib.parse.unquote(msg)
    print(msg)


  def _read_wordpairs(self):

    pairs = {}
    try:
      fh = open(self.cache_file, 'r+')
    except:
      fh = open(self.cache_file, 'a+')
    data = fh.read()

    for line in data.split('\n'):
      if '\t' in line:
        a, b = line.split('\t')
        pairs[a] = b

    fh.close()
    return pairs


  def _save_wordpairs(self):

    pairs = '\n'.join(['%s\t%s' % (a,b) for a,b in self.wordpairs.items()])

    fh = open('.wordpairs', 'w+')
    fh.write(pairs)
    fh.close()
