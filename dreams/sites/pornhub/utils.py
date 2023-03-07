from bs4 import BeautifulSoup as bs
from dreams.utils.settings import puts
import kitano.logging as lg

from dreams.utils.settings import argument_bool_throw_error_find_videos,VideoData

site_name = 'PornHub'
url_base= 'https://pornhub.com'#/video/diva%20gali?p=1'
dir_pattern_cookies = f'.cookies_{site_name}.json'


lg.str_date(f'[%H:%M:%S %d/%m/%Y ({site_name})]: ')


def minerate_video(html_parser:bs,page_number:int,url_font:str):
    #print(html_parser)
    if "We're sorry, but the requested search cannot be found. Broaden your search." in html_parser.get_text():
        puts('Ops! end page search!')
        return False
    li_list = html_parser.find_all('li',{'class':'pcVideoListItem'})
    #print(len(li_list))
    #print(li_list)
    videos_list = []
    for i,li in enumerate(li_list):
        title = li.find('img')['alt']
        time = li.find('var').text
        thumbnail = li.find('img')['src']
        link = f"{url_base}{li.find('a')['href']}"
        preview = li.find('img').get('data-mediabook',None)
        views = li.find('span',{'class':'views'}).text
        rating = ''.join(li.find('div',{'class':'rating-container'}).text.split()).replace('\n','').replace(' ','')
        upload_date = li.find('var',{'class':'added'}).text
        
        videos_list.append(VideoData(
            url=link,
            title=title,
            time=time,
            thumbnail=thumbnail,
            preview=preview,
            views=views,
            rating=rating,
            date_upload=upload_date,
            page_number=page_number,
            site_name=site_name,
            url_font=url_font,
            indice=i
        ))
    #print(videos_list[0])
    return videos_list