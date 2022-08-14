from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass
from app.obfuscation.obf_web import web_scrape
import time


@dataclass
class web_scraper(web_scrape):

    def return_web(self, search_word, debug):

        web_time = time.time()
        base_url = 'https://en.wiktionary.org/wiki/'
        word_language = search_word + '#English'
        url = '{}{}'.format(base_url, word_language)
        print(url) if debug else ()
        response = requests.get(url)
        if response.status_code == 200:
            return web_scraper.word_try(self, url)
        else:
            base_url = 'https://en.wiktionary.org/wiki/'
            word_language = search_word.capitalize() + '#English'
            url = '{}{}'.format(base_url, word_language)
            print(url) if debug else ()
            url = requests.get(url)
            if response.status_code == 200:
                return web_scraper.word_try(self, url)
            else:
                base_url = 'https://en.wiktionary.org/wiki/'
                word_language = search_word.upper() + '#English'
                url = '{}{}'.format(base_url, word_language)
                print(url) if debug else ()
                url = requests.get(url)
                print("Scraping time:", time.time() - web_time) if debug else ()
                if response.status_code == 200:
                    return web_scraper.word_try(self, url)
                else:
                    return "word not in dictionary"

    def word_try(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        list(soup.children)
        return soup.find_all('p')[0].get_text()
