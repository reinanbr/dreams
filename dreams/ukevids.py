from bs4 import BeautifulSoup as bs
import requests as rq
import mechanicalsoup as mec
import re
import time

br = mec.StatefulBrowser()


headers = {'User-Agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36(KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-URL-Manager Mobile Safari/537.36'}
url_base='https://ukdevilz.com'


br.session.headers = headers
br.session.headers.update(headers)




def get_videos_bg_link(url:str) -> list:

    assert (url_base in url), '[error spankbang]: it is not a url from spankbang!'
    url_html = br.get(url)
    url_html = url_html.text
    html_parser = bs(url_html,features="html.parser")
    assert (not ('Nothing Found' in  html_parser.get_text())), '[error ukevids]: site dont have videos more here page!'

    try:
        video_div = html_parser.find_all('div',{'class':'item'})
        #video_div = html_parser.find_all('div',{'class':'video-item'})
    except:
        raise Exception('[error ukevids]: dont find any videos here page!')

    list_video = []
    for video in video_div:
        url_video = f"{url_base}{video.find('a')['href']}"
        title_video = video.find('img')['alt']
        time_video = video.find('div',{'class':'m_time'}).text
        url_img_video = video.find('img')['data-src']
        views = video.find('div',{'class':'m_views'}).text

        # vid = {'url':url_video,
        #        'url_img':url_img_video,
        #        'title':title_video,
        #        'time':time_video
        #      }
        # list_video.append(vid)

        min,seg = time_video.split(':')[0],time_video.split(':')[1]
        dur = (int(min)*60)+int(seg)
        vid = {'title':title_video,
                'time':time_video,
        #       'gif':gif_url,
                'stats':views,
                'dur':dur,
                'url':url_video,
                'url_img':url_img_video,
                
                
        }
        list_video.append(vid)
        #count_video_ = count_video_ + 1
        #print(f'video: {title_video} - {time_video} [{url}]')
    return list_video




def search_porn(query,page_limit=2,page_number:int=None):
    #print('[ukevids]')
    #headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko), Chrome/61.0.3163.100 Safari/537.36'}
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
            url = f'{url_base}/video/{query}?p={p}'
            vds = get_videos_bg_link(url)
            list_videos = list_videos+vds
            print('\r',end='')
            print(f'finding {len(list_videos)} videos from {p} pages...',end='',flush=True)

            p = p + 1

    else:
        p = page_number
        url = f'{url_base}/video/{query}?p={p}' #f'{url_base}/s/{query}/{p}/?o=all'
        list_videos = get_videos_bg_link(url)
        print('\r',end='')
        print(f'{len(list_videos)} videos finds from page search number {p}!',end='',flush=True)

    print('\n')
    time_ping_end = time.time() - time_ping_init
    
    data = {'url_base':url_base,'query':query,'url_search':f'{url_base}/video/{query}','ping':time_ping_end,'len_videos':len(list_videos),'videos':list_videos}
    return data
# query = 'natasha nice'
# res = (search_porn(query))
# i=0
# for v in res:
#     print(f'[{i}]',v,'\n')
#     i=i+1

	
