
from bs4 import BeautifulSoup as bs
import requests as rq
import mechanicalsoup as mec
import re
import logging
import time

url_base='https://spankbang.com'
headers = {'User-Agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36(KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-URL-Manager Mobile Safari/537.36'}


br = mec.StatefulBrowser()
br.session.headers = headers
br.session.headers.update(headers)

count_video_ = 0
def get_videos_bg_link(url:str) -> list:

    assert (url_base in url), '[error spankbang]: it is not a url from spankbang!'
    url_html = br.get(url)
    url_html = url_html.text
    html_parser = bs(url_html,features="html.parser")
    assert (not ('We could not find any videos for' in  html_parser.get_text())), '[error spankbang]: site dont have videos more here page!'

    try:
        video_div = html_parser.find_all('div',{'class':'video-item'})
    except:
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
        vid = {'url':url_video,
                'url_img':url_img_video,
                'title':title_video,
                'time':time_video,
                'gif':gif_url,
                'stats':stats,
                'dur':dur
        }
        list_video.append(vid)
        #count_video_ = count_video_ + 1
        #print(f'video: {title_video} - {time_video} [{url}]')
    return list_video




def search_porn(query:str,page_number:int=None,page_limit:int=2) -> dict:
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
    #print('[spankbang]')
    query = '+'.join(query.split(' '))
    list_div_content = []
    list_div_info = []
    list_videos = []

    time_ping_init = time.time()
    if not page_number:
        p = 1
        N = page_limit
        for i in range(N):
            #print(p)
            url = f'{url_base}/s/{query}/{p}/?o=all'
            vds = get_videos_bg_link(url)
            list_videos = list_videos+vds
            print('\r',end='')
            print(f'finding {len(list_videos)} videos from {p} pages...',end='',flush=True)

            p = p + 1

    else:
        p = page_number
        url = f'{url_base}/s/{query}/{p}/?o=all'
        list_videos = get_videos_bg_link(url)
        print('\r',end='')
        print(f'{len(list_videos)} videos finds from page search number {p}!',end='',flush=True)

    print('\n')
    time_ping_end = time.time() - time_ping_init
    
    data = {'url_base':url_base,'query':query,'page_search': f'{url_base}/s/{query}/?o=all','ping':time_ping_end,'len_videos':len(list_videos),'videos':list_videos}
    return data
	
	
# query = 'alessandra marques'
# res = (search_porn(query))

# i=0
# for v in res:
#     print(f'[{i}]',v,'\n')
#     i=i+1

count_video_ = 0
