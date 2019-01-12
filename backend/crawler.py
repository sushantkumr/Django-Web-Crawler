from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from ordered_set import OrderedSet
from .helpers import is_url_valid, get_clean_url, is_link_internal


class Crawler():

    def __init__(self, url, depth=25):
        self.crawled_urls = OrderedSet([])
        if (is_url_valid(url)):
            url = get_clean_url(url, '')
            self.depth = depth
            self.index = 0
            self.crawled_urls.add(url)
            self.crawl(url)

    def crawl(self, url):
        '''
        Crawl over URLs
            - scrape for anchor tags with hrefs in a webpage
            - reject if unwanted or cleanup the obtained links
            - append to a set to remove duplicates
            - "crawled_urls" is the repository for crawled URLs
        @input:
            url: URL to be scraped
        '''
        found_urls = []
        try:
            page = urlopen(url)
            content = page.read()
            soup = BeautifulSoup(content, 'lxml', parse_only=SoupStrainer('a'))
            for anchor in soup.find_all('a'):
                link = anchor.get('href')
                if is_url_valid(link):
                    # Complete relative URLs
                    link = get_clean_url(url, link)
                    if is_link_internal(link, url):
                        found_urls.append(link)
                else:
                    pass

        except HTTPError as e:
            print('HTTPError:' + str(e.code) + ' in ', url)
        except URLError as e:
            print('URLError: ' + str(e.reason) + ' in ', url)
        except Exception:
            import traceback
            print('Generic exception: ' + traceback.format_exc() + ' in ', url)

        cleaned_found_urls = set(found_urls)  # To remove repitions
        self.crawled_urls |= cleaned_found_urls  # Union of sets
        if (len(self.crawled_urls) > self.depth):
            self.crawled_urls = self.crawled_urls[:self.depth]
            return
        else:
            self.index += 1
            if self.index < len(self.crawled_urls):
                self.crawl(self.crawled_urls[self.index])
            else:
                return
