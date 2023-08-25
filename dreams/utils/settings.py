from kitano import puts
import time
import kitano.logging as lg
from dataclasses import dataclass
from urllib.parse import quote,unquote
from dreams.utils.objects import EmbedVideo,VideoData,DataVideos
import json
from requests.utils import cookiejar_from_dict
from requests import Session

# tools browser
dir_pattern_cookies = '.cookies.json'
dir_cookies = ''
def set_dir_cookies(dir:str):
    global dir_cookies
    dir_cookies = dir
    
def save_cookies(browser:Session,path_cookies:str):
    cookies = browser.cookies.get_dict()
    cookies_json = json.dumps(cookies,indent=4)
    print('dir cookie',dir_cookies)
    with open(dir_cookies+path_cookies,'w') as file_cookies:
        file_cookies.write(cookies_json)

def load_cookies(browser:Session,path_cookies:str):
    with open(dir_cookies+path_cookies,'r') as file_cookies:
        cookies_json = file_cookies.read()
        cookies_dict = json.loads(cookies_json)
    browser.cookies = cookiejar_from_dict(cookie_dict=cookies_dict)
    


# for return in bool and not error raises
argument_bool_throw_error_find_videos = True
headers = {"connection": "keep-alive",
"cache-control": "max-age=0",
"sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "\"Linux\"",
"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"sec-fetch-site": "none",
"sec-fetch-mode": "navigate",
"sec-fetch-user": "?1",
"sec-fetch-dest": "document",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7"
}

headers_ = {"connection":"keep-alive",
           "cache-control":"max-age=0",
           "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
           "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
           "accept-encoding":"gzip, deflate",
           "accept-language":"en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7"}

def throw_error(arg:bool)->None:
    global argument_bool_throw_error_find_videos
    argument_bool_throw_error_find_videos = arg



headers_ = {'user-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36(KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-URL-Manager Mobile Safari/537.36',
            'connection': 'keep-alive', 'upgrade-insecure-requests': '1',
#            'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-A225M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'pt-BR,pt-PT;q=0.9,pt;q=0.8,en-US;q=0.7,en;q=0.6'}



#function base that get return data video from functions scrap site porn
def search_porn_base(query:str, url_base:str, call_get_videos_site, url_base_page_number_search, site_name:str, page_limit=2, page_number:int=None):
    
    lg.str_date(f'[%H:%M:%S %d/%m/%Y ({site_name})]: ')
    query_=query
    query = quote(query)
    
    list_videos = [] 

    time_ping_init = time.time() 
    if not page_number: 
        p = 1 
        N = page_limit if page_limit else 2
        for i in range(N):

            url = url_base_page_number_search(query,p)
            vds = call_get_videos_site(url,page_number=p,query=query_)
            if vds:
                list_videos = list_videos+vds

                puts(f'finding {len(list_videos)} videos from {p} pages of {N} limit pages...') 

                p = p + 1 # iteration of number pages
            else:
                puts(f'\nops! finished in {p} pages search!')
                break

    else: 
        p = page_number
        url = url_base_page_number_search(query,p)
        list_videos = call_get_videos_site(url,page_number=p)
        puts(f'{len(list_videos)} videos finds from page search number {p}!')
    


    print('\n')
    time_ping_end = time.time() - time_ping_init 
    len_videos = len(list_videos) 

    if page_number: 
        len_pg = None
        len_videos_pages = len_videos
    else: 
        len_pg = p-1
        len_videos_pages = int(len_videos/len_pg) if len_pg else len_videos


    data_videos = DataVideos(site_name=site_name, 
                             sucess=bool(len_videos),        
                             query=query,         
                             url_base=url_base,         
                             url_search=url_base_page_number_search(query,1),         
                             videos=list_videos,         
                             ping=time_ping_end,         
                             videos_per_pages=len_videos_pages,         
                             len_pages=len_pg,         
                             len_videos=len_videos)
    return data_videos




