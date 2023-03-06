from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
from dreams.utils.objects import VideoData,DataVideos
from dreams.utils.settings import search_porn_base

asession = HTMLSession()
url_base = 'https://nudes7.com/' #?s=mia+monroe'
site_name = 'nudes7@only'

def get_videos_nudes7_link(url:str,page_number:int)->list:
    url_html = asession.get(url)
    url_ = url_html.url
    html_parser = bs(url_html.text,features='html.parser')
    articles = html_parser.find_all('article')
    #print(len(articles))
    list_videos = []
    for i,article in enumerate(articles):
        title = article.find('a')['title']
        url_video = article.find('a')['href']
        img = article.find('img')['src']
        
        list_videos.append(VideoData(title=title,
                                     url=url_video,
                                     thumbnail=img,
                                     time=None,
                                     site_name=site_name,
                                     url_font=url,
                                     indice=i,
                                     page_number=page_number))
    return list_videos




def url_base_search_page_nudes7(query,p):
    url_search = f'https://nudes7.com/?s={query}'
    return url_search


def search_porn(query:str)->DataVideos:
    return search_porn_base(query=query,
                            url_base=url_base,
                            site_name=site_name,
                            page_limit=None,
                            page_number=1,
                            call_get_videos_site=get_videos_nudes7_link,
                            url_base_page_number_search=url_base_search_page_nudes7)
