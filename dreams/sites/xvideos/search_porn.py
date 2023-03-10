from bs4 import BeautifulSoup as bs
import mechanicalsoup as mec
import os
from dreams.utils.settings import  headers, search_porn_base,load_cookies,save_cookies
import kitano.logging as lg
from .utils import minerate_video,url_base_page_number_search,site_name,url_base,dir_pattern_cookies

lg.str_date(f'[%H:%M:%S %d/%m/%Y ({site_name})]: ')

br = mec.StatefulBrowser()
br.session.headers = headers
br.session.headers.update(headers)

if os.path.isfile(dir_pattern_cookies):
    load_cookies(br.session,dir_pattern_cookies)


#get url search
def get_videos_uk_link_search(url:str,page_number:int,query:str) -> list:
    assert (url_base in url), f'[error {site_name}]: it is not a url from {site_name}!'
    loc = url
    url_html_ = br.get(url)
    save_cookies(br.session,dir_pattern_cookies)
    url_html = url_html_.text
    html_parser = bs(url_html,features="html.parser")
    
    return minerate_video(html_parser,page_number=page_number,url_font=url_html_.url)


#/?k=gali+diva&p=1
# https://pt.pornhub.com/video/search?search=milf+big+ass&page=2






def search_porn(query:str,page_limit:int=2,page_number=None):
    return search_porn_base(query=query,
                            url_base=url_base,
                            site_name=site_name,
                            page_limit=page_limit,
                            page_number=page_number,
                            call_get_videos_site=get_videos_uk_link_search,
                            url_base_page_number_search=url_base_page_number_search)








# #in the last option
# def get_video_embed(video):
#     url_html = br.get(video['url'])
#     #print(url_html)
#     url_html = url_html.text
#     html_parser = bs(url_html,features="html.parser")
#     #print(html_parser)
#     if ('Sorry, this video has been deleted' in  html_parser.get_text()):
#         return f"the [{video['title']}-{video['time']}] has been deleted!"
#     else:
#         url_video = html_parser.find('iframe',{'id':'iplayer'})['src'].split('&amp')[0]
#         url_video = f'{url_base}{url_video}'
#         return url_video

