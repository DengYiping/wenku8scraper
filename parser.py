import requests
from bs4 import BeautifulSoup

class Parser:
    def __init__(self, url):
        '''
        a parser for general purpose get request parsing
        '''
        self.url = url
        req = requests.get(url)

        if req.status_code != 200:
            raise IOError('page cannot be open')
        content = req.content
        self.soup = BeautifulSoup(content, 'html.parser')

