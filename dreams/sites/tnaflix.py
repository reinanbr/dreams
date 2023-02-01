from bs4 import BeautifulSoup as bs
#import requests as rq
import mechanicalsoup as mec
from collections import namedtuple
#import re
import time

from requests_html import HTMLSession
asession = HTMLSession()

from dreams.settings import argument_bool_throw_error_find_videos, EmbedVideo,DataVideos, search_porn_base,VideoData
from kitano import puts
import kitano.logging as lg

site_name = 'tnaflix'
url_base= 'https://tnaflix.com'

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




#get url search
def get_videos_tn_link_search(url:str,page_number:int,query:str) ->list:
    assert (url_base in url), f'[error {site_name}]: it is not a url from {site_name}'
    loc = url
    url_htm = asession.get(url)
    url_html = url_htm.text
    html_parser = bs(url_html,features="html.parser")

    if query.count(' '):
        if html_parser.get_text().count(query.split(' ')[0])< 3:
            puts('Ops! end page search! Query init dont found!')
            return False
    else:
        if html_parser.get_text().count(query) < 3:
            puts('Ops! end page search! Query init dont found!')
            return False

    try:
        video_ul = html_parser.find('ul',{'class':'thumbsList'})
    except:
        if argument_bool_throw_error_find_videos:
            pass
            return False
        else:
            raise Exception(f'[error {site_name}]: dont find any videos here page!')

    #'''it work line, is for stopping the code in end page search'''
    if page_number > int(url_htm.url.split('&page=')[1]):
        puts('Ops! end page search! it is returned to init page search!')
        return False
    
    
    list_video_li = video_ul.find_all('li')
    #print(len(list_video_li))
    videos_list = []
    i = 0
    for video in list_video_li:
        #print(video)
        vd_data = video.find('a')
        
        video_url = f"{url_base}{vd_data['href']}"
        video_title = video['data-name'] #vd_data.text
        video_time = vd_data.find('div',{'class':'videoDuration'}).text
        thumbnail = vd_data.find('img')['data-original']
        rating = vd_data.find('div',{'class':'ratingSp'}).text if vd_data.find('div',{'class':'ratingSp'}) else None
        preview = video['data-trailer']
        dur = int(video['data-time'])
        views = video['data-vn']
        
        year_upload = ((time.time() - int(video['data-date']))/60/60/24/365)
        date_upload = f"{year_upload:.1f} year's ago"
        date_upload = f"{(12*year_upload):.1f} month's ago" if year_upload<1 else date_upload
        
        videos_list.append(VideoData(
            url=video_url,
            title=video_title,
            time=video_time,
            thumbnail=thumbnail,
            rating=rating,
            preview=preview,
            duration_seconds=dur,
            duration=dur,
            url_font=url_htm.url,
            views=views,
            stats=None,
            date_upload=date_upload,
            page_number=page_number,
            site_name=site_name,
            indice=i
        ))
        i = i+1
    return videos_list


#https://www.tnaflix.com/search.php?tab=videos&what=lorena+aquino&category=&sb=relevance&su=anytime&sd=all&dir=desc&page=2
def url_base_search_page(query,p):
    query = query.replace(' ','+')
    url_search= f'{url_base}/search.php?tab=videos&what={query}&category=&sb=relevance&su=anytime&sd=all&dir=desc&page={p}' #f'{url_base}/search/?q={query}'
    #print(url_search)
    return url_search



def search_porn(query:str,page_limit:int=2,page_number:int=None)->DataVideos:
    
    return search_porn_base(query=query,
                            url_base=url_base,
                            site_name=site_name,
                            page_limit=page_limit,
                            page_number=page_number,
                            call_get_videos_site=get_videos_tn_link_search,
                            url_base_page_number_search=url_base_search_page)






def get_video_embed(url:str)->EmbedVideo:
    res = asession.get(url)
    res_br = br.get(url)
    html_parser = bs(res.text,features="html.parser")
    html_parser_br = bs(res_br.text,features='html.parser')
    #print(html_parser)
    title = html_parser.find('h1').text
    thumbnail = html_parser.find('img',{'class':'pVideoPreview'})['src']
    link = html_parser_br.find('video')['src']
    views = html_parser.find('div',{'class':'nWatchCount'}).text
    likes = html_parser_br.find('span',{'class':'text_like'}).text
    tags = html_parser.find('div',{'class':'_video_info'}).text
    
    videos_sugestions = html_parser.find('ul',{'class':'thumbsList'}).find_all('li')
    videos_sugestions_list = []
    i = 0
    for video in videos_sugestions:
        vd_data = video.find('a')
        
        video_url = f"{url_base}{vd_data['href']}"
        video_title = video['data-name'] #vd_data.text
        video_time = vd_data.find('div',{'class':'videoDuration'}).text
        thumbnail = vd_data.find('img')['data-original']
        rating = vd_data.find('div',{'class':'ratingSp'}).text if vd_data.find('div',{'class':'ratingSp'}) else None
        preview = video['data-trailer']
        dur = int(video['data-time'])
        views = video['data-vn']
        date_upload = int(video['data-date'])
        
        year_upload = ((time.time() - date_upload)/60/60/24/365)
        date_upload = f"{year_upload:.1f} year's ago"
        date_upload = f"{(12*year_upload):.1f} month's ago" if year_upload<1 else date_upload
        
        videos_sugestions_list.append(VideoData(
            url=video_url,
            title=video_title,
            time=video_time,
            thumbnail=thumbnail,
            rating=rating,
            preview=preview,
            duration_seconds=dur,
            duration=dur,
            url_font=res.url,
            views=views,
            stats=None,
            date_upload=date_upload,
            page_number=0,
            site_name=site_name,
            indice=i
        ))
        i = i+1
    
    return EmbedVideo(site_name=site_name,
                      url=link,
                      title=title,
                      time=None,
                      thumbnail=thumbnail,
                      time_published=None,
                      views=views,
                      len_videos_sugestions=i-1,
                      videos_sugestions=videos_sugestions_list)
