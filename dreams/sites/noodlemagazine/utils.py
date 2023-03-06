from bs4 import BeautifulSoup as bs
from dreams.utils.settings import puts
import kitano.logging as lg

from dreams.utils.settings import argument_bool_throw_error_find_videos,VideoData

site_name = 'NoodleMagazine'
url_base= 'https://noodlemagazine.com'#/video/diva%20gali?p=1'
dir_pattern_cookies = '.cookies_noodlemagazine.json'


lg.str_date(f'[%H:%M:%S %d/%m/%Y ({site_name})]: ')


def minerate_video(html_parser:bs,url:str,page_number:int=0):
    try:
        video_div = html_parser.find_all('div',{'class':'item'})
    except:
        if argument_bool_throw_error_find_videos:
            pass
            return False
        else:
            raise Exception('[error nodlemagazine]: dont find any videos here page!')
    
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
        preview = video.find('video',{'class':'trailer'})
        if preview:
            preview = preview['data-src']
        else:
            preview = None

        time_spec = time_video.split(':')
        if len(time_spec)>2:
            hour,min,sec=tuple(time_spec)
            try:
                min = min+60*int(hour)
                dur = (int(min)*60)+int(sec)
            except Exception as e:
                dur = None
                puts(f'error Exception: {e}')
                pass
        else:
            min,sec=tuple(time_spec)
            try:
                dur = (int(min)*60)+int(sec)
            except Exception as e:
                dur = None
                puts(f'error Exception: {e}')
                pass

        Vid = VideoData(title=title_video,
                            time=time_video,
                            duration_seconds=dur,
                            page_number=page_number,
                            url=url_video,
                            url_font=url,
                            views=views,
                            stats=None,
                            thumbnail=url_img_video,
                            site_name=site_name,
                            preview=preview,
                            indice=i,
                            date_upload=None)
        i = i+1

        list_video.append(Vid)
    return list_video
