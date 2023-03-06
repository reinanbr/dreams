from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
from dreams.utils.objects import VideoData,DataVideos
from dreams.utils.settings import search_porn_base


asession = HTMLSession()
url_base = 'https://nudes7.com/' #?s=mia+monroe'
site_name = 'viralpornhub@only'


url_base = 'https://viralpornhub.com' #/search/Mia-Monroe-/'

def get_videos_link_viralpornhub(url:str,page_number:int,query:str)-> list[VideoData]:
    
    #urls = [url,url+'-/#search'] # page 1 and 2
    #for p,_url in enumerate(urls):
    i=0
    url_html = asession.get(url)
    url_ = url_html.url
    html_parser = bs(url_html.text,features='html.parser')
    items = html_parser.find_all('div',{'class':'item'})
    list_videos:list[VideoData] = []

    for item in items:
        title = item.find('a')['title']
        url_video = item.find('a')['href']
        thumbnail = 'https://'+item.find('img')['data-webp'].split('/ss.')[1]
        preview = item.find('img')['data-preview']
        time = item.find('div',{'class':'duration'}).text
        rating_str = ''.join(item.find('div',{'class':'rating'}).text.split()).replace('\n','').replace(' ','')
        date_upload_str = item.find('div',{'class':'added'}).text
        views_str = item.find('div',{'class':'views'}).text

        list_videos.append(VideoData(title=title,
                                    url=url_video,
                                    thumbnail=thumbnail,
                                    preview=preview,
                                    rating=rating_str,
                                    time=time,
                                    date_upload=date_upload_str,
                                    views=views_str,
                                    page_number=1,
                                    indice=i,
                                    url_font=url_,
                                    site_name=site_name))
        i=i+1

    return list_videos


def url_base_search_page_viralpornhub(query,p):
    return f'https://viralpornhub.com/search/{query}'


def search_porn(query:str)->DataVideos:
    return search_porn_base(query=query,
                            url_base=url_base,
                            site_name=site_name,
                            call_get_videos_site=get_videos_link_viralpornhub,
                            url_base_page_number_search=url_base_search_page_viralpornhub,
                            page_number=None,
                            page_limit=1)