from bs4 import BeautifulSoup as bs
from dreams.utils.settings import puts
import kitano.logging as lg

from dreams.utils.settings import VideoData

site_name = 'XVideos'
url_base= 'https://www.xvideos.com'#/video/diva%20gali?p=1'
dir_pattern_cookies = f'.cookies_{site_name}.json'


lg.str_date(f'[%H:%M:%S %d/%m/%Y ({site_name})]: ')





def url_base_page_number_search(query:str,page:int):
    return f'{url_base}/?k={query}&p={page}'



def minerate_video(html_parser:bs,page_number:int,url_font:str):
    #print(html_parser)
    if "No video match with this search" in html_parser.get_text():
        puts('Ops! end page search!')
        return False
    list_div = html_parser.find_all('div')
    list_div_id = [div_id for div_id in list_div if div_id.get('id',None)]
    list_div_video = [div_video for div_video in list_div_id if 'video' in div_video['id']] 
    #print(len(list_div_video))
    videos_list = []
    for i,div in enumerate(list_div_video):
       #print(div)
       title = div.find_all('a')[1].text if len(div.find_all('a')) > 1 else div.find('a').text
       time = div.find('span',{'class':'duration'}).text
       thumbnail = div.find('img')['data-src']
       link = f"{url_base}{div.find('a')['href']}"
       preview = None #div.find('div',{'class':'videopv'}).find('video').get('src',None)
       views = None#div.find('span',{'class':'views'}).text
       rating = None #''.join(li.find('div',{'class':'rating-container'}).text.split()).replace('\n','').replace(' ','')
       upload_date = None #li.find('var',{'class':'added'}).text
        
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