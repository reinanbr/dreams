from kitano import puts
import time
import kitano.logging as lg
from dataclasses import dataclass




# for return in bool and not error raises
argument_bool_throw_error_find_videos = True
# throw error
def throw_error(arg:bool)->None:
    global argument_bool_throw_error_find_videos
    argument_bool_throw_error_find_videos = arg



# it is for organization from return videos data
@dataclass
class DataVideos:
    site_name:str
    url_base:str
    query:str
    ping:float
    videos:list
    videos_per_pages:int
    len_pages:str
    len_videos:str
    url_search:str

    def __repr__(self) -> str:
        return f'{self.site_name}(query={self.query}, len_videos={self.len_videos}, len_pages={self.len_pages}, videos_per_pages={self.videos_per_pages}, ping={self.ping}, url_base={self.url_base}, url_search={self.url_search}), videos={self.videos}'

# organization data video, based on SpankBank response video, because is the more complete
@dataclass
class VideoData:
    title:str
    time:str
    duration:int
    stats:str
    page_number:int
    url:str
    url_font:str
    thumbnail:str
    preview:str
    site_name:str

    def __repr__(self) -> str:
        return f'{self.site_name.lower()}_video(title={self.title},time={self.time},duration={self.duration},stats={self.stats},page_number={self.page_number},url={self.url},url_font={self.url_font},thumbnail={self.thumbnail},preview={self.preview})'




#function base that get return data video from functions scrap site porn
def search_porn_base(query:str,
                     url_base:str,
                     call_get_videos_site,
                     url_base_page_number_search,
                     site_name:str,
                     page_limit=2,
                     page_number:int=None):
    
    lg.str_date(f'[%H:%M:%S %d/%m/%Y ({site_name})]: ') # configuration for puts print
    query = '+'.join(query.split(' ')) # splitting query for searching
    list_videos = [] # list that are receive video's

    time_ping_init = time.time() # for getting ping
    if not page_number: # if is not a only page number so is a page limit, and stop getting on page limit
        p = 1 # page init iteration
        N = page_limit # page end iteration
        for i in range(N):

            url = url_base_page_number_search(query,p) # url searchQuery from package site porn
            vds = call_get_videos_site(url,page_number=p)  # getting data videos from page search number p
            if vds: # if is a data video, and not a return bool False as argument_bool_throw_error_find_videos, it work
                list_videos = list_videos+vds # add list videos return in list main

                puts(f'finding {len(list_videos)} videos from {p} pages of {N} limit pages...') # printing it work and progress on pages

                p = p + 1 # iteration of number pages
            else:
                puts(f'\nops! finished in {p} pages search!') # if return is a bool false as argument_bool_throw_error_find_videos, it is stooped on it
                break

    else: # if is for get a only page number search
        p = page_number
        url = url_base_page_number_search(query,p)
        list_videos = call_get_videos_site(url,page_number=p)
        #print('\r',end='')
        puts(f'{len(list_videos)} videos finds from page search number {p}!')#,end='',flush=True)

    print('\n')
    time_ping_end = time.time() - time_ping_init # getting ping
    len_videos = len(list_videos) # count number videos

    # saving data info just
    if page_number: # if type search is a only page number, it dont count videos per page as natural
        len_pg = None
        len_videos_pages = len_videos
    else: # if is a search normal (with page limit), it count number per videos 
        len_pg = p-1 # because the final p is the numberVideo + 1, because is in the last work
        len_videos_pages = int(len_videos/len_pg)


    data_videos = DataVideos(site_name=site_name,
                             query=query,
                             url_base=url_base,
                             url_search=list_videos[0].url_font,
                             videos=list_videos,
                             ping=time_ping_end,
                             videos_per_pages=len_videos_pages,
                             len_pages=len_pg,
                             len_videos=len_videos)
    return data_videos
    


