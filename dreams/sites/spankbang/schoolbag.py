from bs4 import BeautifulSoup as bs
from collections import namedtuple
import mechanicalsoup as mec
from dreams.utils.settings import VideoData,EmbedVideo,load_cookies,save_cookies
from dreams.utils.settings import argument_bool_throw_error_find_videos,headers, search_porn_base
from kitano import puts
import kitano.logging as lg
from requests_html import HTMLSession
from requests.utils import cookiejar_from_dict
import time
import json





site_name = 'SpankBang'
lg.str_date(f'[%H:%M:%S %d/%m/%Y ({site_name})]: ')
asession = HTMLSession()

url_base='https://spankbang.com'
br = mec.StatefulBrowser()
br.session.headers = headers
br.session.headers.update(headers)








def work_stats(stats):
    stats=stats.replace('\n\n\n','')
    stats_list = stats.split('\n')

    views_str = stats_list[1]
    if 'M' in views_str:
        views =int(float(views_str.split('M')[0])*10**6)
    elif 'K' in views_str:
        views =int(float(views_str.split('K')[0])*10**3)
    else:
        views =int(float(views_str))

    rating_str = stats_list[2]
    rating = int(rating_str.split('%')[0])

    date_upload_str = stats_list[3]
    seconds_hour = 3600
    if 'minute' in date_upload_str:
        minutes = int(date_upload_str.split(' minute')[0])
        date_upload = time.time() - minutes*60
    elif 'hour' in date_upload_str:
        hours = int(date_upload_str.split(' hour')[0])
        date_upload = time.time() - hours*seconds_hour
    elif 'day' in date_upload_str:
        days = int(date_upload_str.split(' day')[0])
        date_upload = time.time() - days*24*seconds_hour
    elif 'week' in date_upload_str:
        weeks = int(date_upload_str.split(' week')[0])
        date_upload = time.time() - weeks*7*24*seconds_hour
    elif 'month' in date_upload_str:
        months = int(date_upload_str.split(' month')[0])
        date_upload = time.time() - months*30*24*seconds_hour
    elif 'year' in date_upload_str:
        years = int(date_upload_str.split(' year')[0])
        date_upload = time.time() - years*365*24*seconds_hour
    
    return {'int':{'views':views,'rating':rating,'date_upload':date_upload},
            'str':{'views':views_str,'rating':rating_str,'date_upload':date_upload_str}}


