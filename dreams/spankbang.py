
from bs4 import BeautifulSoup as bs
import requests as rq
import mechanicalsoup as mec
import re
import logging
import time

from dreams.settings import puts
from requests_html import HTMLSession
asession = HTMLSession()



from dreams.settings import argument_bool_throw_error_find_videos, search_porn_base
import kitano.logging as lg

site_name = 'spankbang'
lg.str_date(f'[%H:%M:%S %d/%m/%Y ({site_name})]: ')


headers = {'user-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36(KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-URL-Manager Mobile Safari/537.36',
            'connection': 'keep-alive', 'upgrade-insecure-requests': '1', 
#            'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-A225M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'pt-BR,pt-PT;q=0.9,pt;q=0.8,en-US;q=0.7,en;q=0.6'}




url_base='https://spankbang.com'
br = mec.StatefulBrowser()
br.session.headers = headers
br.session.headers.update(headers)








def get_videos_bg_link(url:str,page_number:int) -> list:

    assert (url_base in url), '[error spankbang]: it is not a url from spankbang!'
    url_html = br.get(url)
    url_html = url_html.text
    html_parser = bs(url_html,features="html.parser")
    #assert (not ('We could not find any videos for' in  html_parser.get_text())), '[error spankbang]: site dont have videos more here page!'

    try:
        video_div = html_parser.find_all('div',{'class':'video-item'})
    except:
        if argument_bool_throw_error_find_videos:
            pass
            return False
        else:
            raise Exception('[error spankbang]: dont find any videos here page!')

    list_video = []
    for video in video_div:
        url_video = f"{url_base}{video.find('a')['href']}"
        title_video = video.find('img')['alt']
        time_video = video.find('span',{'class':'l'}).text
        url_img_video = video.find('img')['data-src']
        stats = video.find('div',{'class':'stats'}).text
        #print(stats)
        try:
            gif_url = video.find('img')['data-preview']
        except:
            gif_url = None
            pass

        dur = int(time_video.split(' min')[0])*60
        vid = {'title':title_video,
                'time':time_video,
                'dur':dur,
                'stats':stats,
                'page_number':page_number,
                'url':url_video,
                'url_font':url,
                'thumbnail':url_img_video,

                'preview':gif_url,
        }
        list_video.append(vid)
        #count_video_ = count_video_ + 1
        #print(f'video: {title_video} - {time_video} [{url}]')
    return list_video








def url_base_search_page(query,p):
    return f'{url_base}/s/{query}/{p}/?o=trending'



def search_porn(query:str,page_limit:int=2,page_number=None):
    """ a simple function for return data video's porn from SpankBang search

    Example:
        >>> import dreams.spankbang as sb
        >>> sb.search_porn('natasha nice',page_limit=1)
        {'url_base': 'https://spankbang.com', 'query': 'natasha+nice', 'ping': 2.200756072998047, 'len_videos': 98, 'videos': [{'url': 'https://spankbang.com/7btrt/video/natasha+nice+stepmom+natasha+s+big+tit+cum+candy+treat', 'url_img': 'https://tb-lb.sb-cd.com/t/12309113/1/2/w:800/t6-enh/natasha-nice-stepmom-natasha.jpg', 'title': "Natasha Nice - Stepmom Natasha'S Big Tit Cum Candy Treat", 'time': '43 min', 'gif': 'https://tbv.sb-cd.com/t/12309113/1/2/td.mp4', 'stats': '150K 100% 2 months', 'dur': 2580}, ...


      Args:
        query (str): _the argument for to searching in the site porn
        page_number (int): getting video's from only it page number. Defaults to None.
        page_limit (int, optional): _page number limit for getting . Defaults to 2.

    Returns:
        dict: dict with list video's data, ping info, site name, lens video's data
    """
    return search_porn_base(query=query,
                            url_base=url_base,
                            page_limit=page_limit,
                            page_number=page_number,
                            call_get_videos_site=get_videos_bg_link,
                            url_base_page_number_search=url_base_search_page)







def get_video_embed(video):
    res = asession.get(video['url'])
    #print(res.text)
    html_parser = bs(res.text,features="html.parser")

    video = html_parser.find('video')
    link = video.find('source')['src']
    
    return link
