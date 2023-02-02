from dataclasses import dataclass





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
    sucess:bool

    def __repr__(self) -> str:
        return f'''
{self.site_name}(
    sucess="{self.sucess}",
    query="{self.query}",
    len_videos={self.len_videos}, 
    len_pages={self.len_pages}, 
    videos_per_pages={self.videos_per_pages}, 
    ping={self.ping}, 
    url_base="{self.url_base}", 
    url_search="{self.url_search}", 
    videos={self.videos})'''




# organization data video,
# based on SpankBank response video,
# because is the more complete
@dataclass
class VideoData:
    title:str
    time:str
    duration:int
    page_number:int
    url:str
    url_font:str
    thumbnail:str
    site_name:str
    preview:str=None
    stats:str=None
    indice:int=None
    views:str=None
    rating:str=None
    date_upload:str=None
    duration_seconds:int=None

    def __repr__(self) -> str:
        stats = f',\n            stats="{self.stats}"' if self.stats else ''
        preview = f',\n            preview="{self.preview}"' if self.preview else ''
        indice = f',\n            indice={self.indice}' if not self.indice==None else ''
        views = f',\n            views="{self.views}"' if self.views else ''
        rating = f',\n            rating="{self.rating}"' if self.rating else ''
        date_upload = f',\n            date_upload="{self.date_upload}"' if self.date_upload else ''
        duration = f',\n            duration={self.duration}' if self.duration else ''

        return f'''
        {self.site_name.lower()}_video(
            site_name="{self.site_name}", 
            title="{self.title}", 
            time="{self.time}", 
            page_number={self.page_number}, 
            url="{self.url}", 
            url_font="{self.url_font}", 
            thumbnail="{self.thumbnail}"{stats}{views}{rating}{date_upload}{duration}{preview}{indice})'''



@dataclass
class EmbedVideo:
    url:str
    title:str
    time:str
    thumbnail:str
    views:str
    time_published:str
    site_name:str
    len_videos_sugestions:int
    videos_sugestions:list

    def __repr__(self) -> str:
        return f'''
    EmbedVideo{self.site_name}(
        title={self.title}, 
        time={self.time}, 
        url={self.url}, 
        thumbnail={self.thumbnail}, 
        views={self.views}, 
        time_published={self.time_published}, 
        len_videos_sugestions={self.len_videos_sugestions}, 
        videos_sugestions={self.videos_sugestions})'''


