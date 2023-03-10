from bs4 import BeautifulSoup as bs
import mechanicalsoup as mec
from dreams.utils.settings import puts
from requests_html import HTMLSession
import os
from dreams.utils.settings import headers, EmbedVideo,load_cookies,save_cookies
import kitano.logging as lg
from .utils import minerate_video,url_base,site_name,dir_pattern_cookies


lg.str_date(f'[%H:%M:%S %d/%m/%Y ({site_name})]: ')


br = mec.StatefulBrowser()
br.session.headers = headers
br.session.headers.update(headers)

asession = HTMLSession()

if os.path.isfile(dir_pattern_cookies):
    load_cookies(br.session,dir_pattern_cookies)


url_base_embed = 'https://www.pornhub.com/embed/'


def get_video_embed(url:str):
    res = asession.get(url)
    save_cookies(res,dir_pattern_cookies)
    
    html_parser = bs(res.text,features='html.parser')
    #print(html_parser)
    
    key_video = url.split('video')[2].split('/')[0]
    link_video_embed = f'{url_base}/embedframe/{key_video}'#html_parser.find('meta',{'name':'twitter:player'})['content']#url_base_embed+url.split('viewkey=')[1]
    title_video_embed = html_parser.find('meta',{'property':'og:title'})['content']
    duration_seconds_video_embed = html_parser.find('meta',{'property':'og:duration'})['content']
    thumbnail_video_embed = html_parser.find('meta',{'property':'og:image'})['content']
    likes_video_embed = None #html_parser.find('div',{'class':'rating-good-nbr'}).text
    views_video_embed = html_parser.find('strong',{'class':'mobile-hide'}).get('text',None)
    upload_date_video_embed =None # html_parser.find('div',{'class':'videoInfo'}).text
    rating_video_embed = html_parser.find('div',{'class':'rating-good-perc hide-if-zero-2045'}).text if html_parser.find('div',{'class':'rating-good-perc hide-if-zero-2045'}) else None
    tags_video_embed = None #html_parser.find('div',{'class':'tagsWrapper'}).text
    person_video_embed = None #html_parser.find('div',{'class':'pornstarsWrapper'}).text
    
    
    #list_video_sugestions = minerate_video(html_parser,page_number=0,url_font=res.url)
    
    return EmbedVideo(title=title_video_embed,
                      url=link_video_embed,
                      duration_seconds=duration_seconds_video_embed,
                      thumbnail=thumbnail_video_embed,
                      likes=None,#likes_video_embed,
                      upload_date=upload_date_video_embed,
                      views=views_video_embed,
                      rating=rating_video_embed,
                      tags = None,#tags_video_embed,
                      person=None,#person_video_embed,
                      len_videos_sugestions=0,#len(list_video_sugestions),
                      videos_sugestions=None,#list_video_sugestions,
                      time=None,
                      site_name=site_name,
                      time_published=None)