from bs4 import BeautifulSoup as bs
import requests as rq
import mechanicalsoup as mec
import re
import time

from dreams.settings import puts
from requests_html import HTMLSession
asession = HTMLSession()

from dreams.settings import argument_bool_throw_error_find_videos, search_porn_base
import kitano.logging as lg

site_name = 'ukevids'
url_base= 'https://ukdevilz.com'

lg.str_date(f'[%H:%M:%S %d/%m/%Y ({site_name})]: ')


headers = {'user-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36(KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-URL-Manager Mobile Safari/537.36',
            'connection': 'keep-alive', 'upgrade-insecure-requests': '1',
#            'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-A225M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'pt-BR,pt-PT;q=0.9,pt;q=0.8,en-US;q=0.7,en;q=0.6'}


br = mec.StatefulBrowser()
br.session.headers = headers
br.session.headers.update(headers)







def get_videos_uk_link(url:str,page_number:int) -> list:
    assert (url_base in url), '[error ukevids]: it is not a url from ukevids!'
    url_html = br.get(url)
    url_html = url_html.text
    html_parser = bs(url_html,features="html.parser")
    #assert (not ('Nothing Found' in  html_parser.get_text())), '[error ukevids]: site dont have videos more here page!'

    try:
        video_div = html_parser.find_all('div',{'class':'item'})
    except:
        if argument_bool_throw_error_find_videos:
            pass
            return False
        else:
            raise Exception('[error ukevids]: dont find any videos here page!')

    list_video = []
    for video in video_div:
        url_video = f"{url_base}{video.find('a')['href']}"
        title_video = video.find('img')['alt']
        time_video = video.find('div',{'class':'m_time'}).text
        url_img_video = video.find('img')['data-src']
        views = video.find('div',{'class':'m_views'}).text
        min,seg = time_video.split(':')[0],time_video.split(':')[1]
        dur = (int(min)*60)+int(seg)

        vid = {'title':title_video,
                'time':time_video,
                'dur':dur,
                'views':views,
                'page_number':page_number,
                'url_font':url,
                'url':url_video,
                'thumbnail':url_img_video,
                # 'gif':gif_url,
        }
        list_video.append(vid)

    return list_video







def url_base_page_number_search(query:str,page:int):
    return f'{url_base}/video/{query}?p={page}'







def search_porn(query:str,page_limit:int=2,page_number=None):
    return search_porn_base(query=query,
                            url_base=url_base,
                            page_limit=page_limit,
                            page_number=page_number,
                            call_get_videos_site=get_videos_uk_link,
                            url_base_page_number_search=url_base_page_number_search)








# #in the last option
# def get_video_embed(video):
#     url_html = br.get(video['url'])
#     #print(url_html)
#     url_html = url_html.text
#     html_parser = bs(url_html,features="html.parser")
#     #print(html_parser)
#     if ('Sorry, this video has been deleted' in  html_parser.get_text()):
#         return f"the [{video['title']}-{video['time']}] has been deleted!"
#     else:
#         url_video = html_parser.find('iframe',{'id':'iplayer'})['src'].split('&amp')[0]
#         url_video = f'{url_base}{url_video}'
#         return url_video




def get_video_embed(video):
    res = asession.get(video['url'])
    print(res.text)
    html_parser = bs(res.text,features="html.parser")

    video = html_parser.find('iframe')
    link = f"{url_base}{video['src'].split('&a=1')[0]}"
    return link
