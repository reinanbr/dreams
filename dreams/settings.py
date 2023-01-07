from collections import namedtuple
from kitano import puts
import time
import kitano.logging as lg





argument_bool_throw_error_find_videos = True
# throw error
def throw_error(arg:bool)->None:
    global argument_bool_throw_error_find_videos
    argument_bool_throw_error_find_videos = arg





def search_porn_base(query:str,
                     url_base:str,
                     call_get_videos_site,
                     url_base_page_number_search,
                     site_name:str,
                     page_limit=2,
                     page_number:int=None):
    
    lg.str_date(f'[%H:%M:%S %d/%m/%Y ({site_name})]: ')
    query = '+'.join(query.split(' '))
    list_videos = []

    time_ping_init = time.time()
    if not page_number:
        p = 1
        N = page_limit
        for i in range(N):
            #print(p)
            url = url_base_page_number_search(query,p)
            vds = call_get_videos_site(url,page_number=p)
            if vds:
                list_videos = list_videos+vds
                #print('\r',end='')
                puts(f'finding {len(list_videos)} videos from {p} pages...') #,end='',flush=True)

                p = p + 1
            else:
                puts(f'\nops! finished in {p} pages search!')
                break

    else:
        p = page_number
        url = url_base_page_number_search(query,p) #f'{url_base}/s/{query}/{p}/?o=all'
        list_videos = call_get_videos_site(url,page_number=p)
        #print('\r',end='')
        puts(f'{len(list_videos)} videos finds from page search number {p}!')#,end='',flush=True)

    print('\n')
    time_ping_end = time.time() - time_ping_init
    len_videos = len(list_videos)

    if page_number:
        len_pg = None
        len_videos_pages = len_videos
    else:
        len_pg = p-1
        len_videos_pages = int(len_videos/len_pg)

    data = {'site_name':site_name,
            'url_base':url_base,
            'query':query,
            'url_search':f'{url_base}/video/{query}',
            'ping':time_ping_end,
            'videos_per_pages':len_videos_pages,
            'len_pages':len_pg,
            'len_videos':len_videos,
            'videos':list_videos}
    Data = namedtuple(site_name,data)
    D = Data(**data)
    return D
    

