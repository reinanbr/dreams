from bs4 import BeautifulSoup as bs
import mechanicalsoup as mec
import time
from requests_html import HTMLSession
from kitano import puts
import kitano.logging as lg
from dreams.utils.settings import headers, EmbedVideo,DataVideos,VideoData,load_cookies,save_cookies
import os

asession = HTMLSession()

br = mec.StatefulBrowser()
br.session.headers = headers
br.session.headers.update(headers)





site_name = 'tnaflix'
url_base= 'https://tnaflix.com'
dir_pattern_cookies = '.cookies_tnaflix.json'

lg.str_date(f'[%H:%M:%S %d/%m/%Y ({site_name})]: ')




asession.headers = headers

if os.path.isfile(dir_pattern_cookies):
    load_cookies(asession,dir_pattern_cookies)
    load_cookies(br.session,dir_pattern_cookies)




def get_video_embed(url:str)->EmbedVideo:
    url = url+'&autoPlay=1'
    res = asession.get(url)
    save_cookies(res,dir_pattern_cookies)
    res_br = br.get(url)
    html_parser = bs(res.text,features="html.parser")
    html_parser_br = bs(res_br.text,features='html.parser')
    #print(html_parser_br)
    
    title = html_parser.find('h1').text
    thumbnail = html_parser_br.find('img',{'class':'pVideoPreview'})['src']
    link = html_parser_br.find('meta',{'itemprop':'embedUrl'})['content']
    views = html_parser.find('div',{'class':'nWatchCount'}).text
    #likes = html_parser_br.find('span',{'class':'text_like'}).text
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
