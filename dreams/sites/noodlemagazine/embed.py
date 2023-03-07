from bs4 import BeautifulSoup as bs
import mechanicalsoup as mec
from dreams.utils.settings import puts
from requests_html import HTMLSession
import os
from dreams.utils.settings import headers, EmbedVideo,load_cookies,save_cookies
import kitano.logging as lg
from .utils import minerate_video,site_name,dir_pattern_cookies




lg.str_date(f'[%H:%M:%S %d/%m/%Y ({site_name})]: ')


br = mec.StatefulBrowser()
br.session.headers = headers
br.session.headers.update(headers)

asession = HTMLSession()

if os.path.isfile(dir_pattern_cookies):
    load_cookies(br.session,dir_pattern_cookies)


def get_video_embed(url:str):
    res = asession.get(url)
    save_cookies(res,dir_pattern_cookies)
    
    html_parser = bs(res.text,features="html.parser")
    
    link_video_embed = html_parser.find('meta',{'property':'og:video'})['content'] #f"{url_base}{video['src'].split('&a=1')[0]}"
    title_video_embed = html_parser.find('meta',{'property':'og:title'})['content']
    duration_seconds_video_embed = int(html_parser.find('meta',{'property':'video:duration'})['content'])
    upload_date_video_embed = html_parser.find('meta',{'property':'ya:ovs:upload_date'})['content']
    views_video_embed =  html_parser.find('meta',{'property':'ya:ovs:views_total'})['content']
    likes_video_embed =  html_parser.find('meta',{'property':'ya:ovs:likes'})['content']
    thumbnail_video_embed =  html_parser.find('meta',{'property':'og:image'})['content']
    person_video_embed =  html_parser.find('meta',{'property':'ya:ovs:person'})['content']
    tags_video_embed =  html_parser.find('meta',{'property':'video:tag'})['content']
    
    #sugestions videos
    list_video_sugestions = minerate_video(html_parser,url=url,page_number=0)
    
    return EmbedVideo(title=title_video_embed,
                      url=link_video_embed,
                      duration_seconds=duration_seconds_video_embed,
                      upload_date=upload_date_video_embed,
                      views_int=views_video_embed,
                      likes=likes_video_embed,
                      thumbnail=thumbnail_video_embed,
                      person=person_video_embed,
                      tags=tags_video_embed,
                      site_name=site_name,
                      time=None,
                      views=None,
                      time_published=None,
                      len_videos_sugestions=len(list_video_sugestions),
                      videos_sugestions=list_video_sugestions)
    
