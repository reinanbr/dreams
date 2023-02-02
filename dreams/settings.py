from kitano import puts
import time
import kitano.logging as lg
from dataclasses import dataclass
from urllib.parse import quote,unquote
from dreams.classes import EmbedVideo,VideoData,DataVideos



# for return in bool and not error raises
argument_bool_throw_error_find_videos = True
headers = {'user-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36(KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-URL-Manager Mobile Safari/537.36',
            'connection': 'keep-alive', 'upgrade-insecure-requests': '1',
#            'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-A225M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'pt-BR,pt-PT;q=0.9,pt;q=0.8,en-US;q=0.7,en;q=0.6'}


# throw error
def throw_error(arg:bool)->None:
    global argument_bool_throw_error_find_videos
    argument_bool_throw_error_find_videos = arg




#function base that get return data video from functions scrap site porn
def search_porn_base(query:str, url_base:str, call_get_videos_site, url_base_page_number_search, site_name:str, page_limit=2, page_number:int=None):
    
    lg.str_date(f'[%H:%M:%S %d/%m/%Y ({site_name})]: ')
    query_=query
    query = quote(query)
    
    list_videos = [] 

    time_ping_init = time.time() 
    if not page_number: 
        p = 1 
        N = page_limit 
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




