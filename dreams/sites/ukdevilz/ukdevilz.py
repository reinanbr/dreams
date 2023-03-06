from bs4 import BeautifulSoup as bs
#import requests as rq
import mechanicalsoup as mec
from collections import namedtuple
#import re
#import time

from dreams.utils.settings import puts
from requests_html import HTMLSession
asession = HTMLSession()

from dreams.utils.settings import argument_bool_throw_error_find_videos, headers, search_porn_base,VideoData
import kitano.logging as lg

site_name = 'ukdevilz'
url_base= 'https://ukdevilz.com'

lg.str_date(f'[%H:%M:%S %d/%m/%Y ({site_name})]: ')



br = mec.StatefulBrowser()
br.session.headers = headers
br.session.headers.update(headers)






#get url search
def get_videos_uk_link_search(url:str,page_number:int,query:str) -> list:
    assert (url_base in url), '[error ukdevilz]: it is not a url from ukdevilz!'
    loc = url
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
            raise Exception('[error ukdevilz]: dont find any videos here page!')
    
    #'''it work line, is for stopping the code in end page search'''
    if 'Nothing Found' in html_parser.get_text():
        puts('Ops! end page search!')
        return False

    list_video = []
    i = 0
    for video in video_div:
        url_video = f"{url_base}{video.find('a')['href']}"
        title_video = video.find('img')['alt']
        time_video = video.find('div',{'class':'m_time'}).text
        url_img_video = video.find('img')['data-src']
        views = video.find('div',{'class':'m_views'}).text
        min,seg = time_video.split(':')[0],time_video.split(':')[1]
        try:
            dur = (int(min)*60)+int(seg)
        except Exception as e:
            dur = None
            puts(f'error Exception: {e}')
            pass

        Vid = VideoData(title=title_video,
                            time=time_video,
                            duration=dur,
                            page_number=page_number,
                            url=url_video,
                            url_font=url,
                            stats=views,
                            thumbnail=url_img_video,
                            site_name=site_name,
                            indice=i,
                            preview=None)
        i = i+1

        list_video.append(Vid)

    return list_video


def url_base_page_number_search(query:str,page:int):
    return f'{url_base}/video/{query}?p={page}'







def search_porn(query:str,page_limit:int=2,page_number=None):
    return search_porn_base(query=query,
                            url_base=url_base,
                            site_name=site_name,
                            page_limit=page_limit,
                            page_number=page_number,
                            call_get_videos_site=get_videos_uk_link_search,
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
