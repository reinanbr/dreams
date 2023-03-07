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
    sucess={self.sucess},
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
    page_number:int
    url:str
    url_font:str
    thumbnail:str
    site_name:str
    preview:str=None
    stats:str=None
    indice:int=None
    views:str=None
    views_int:int=None
    rating:str=None
    rating_int:int=None
    date_upload:str=None
    date_upload_seconds:int=None
    duration:int=None
    duration_seconds:int=None

    def __repr__(self) -> str:
        stats = f',\n            stats="{self.stats}"' if self.stats else ''
        preview = f',\n            preview="{self.preview}"' if self.preview else ''
        indice = f',\n            indice={self.indice}' if not self.indice==None else ''
        views = f',\n            views="{self.views}"' if self.views else ''
        views_int = f',\n            views_int={self.views_int}' if self.views_int else ''
        rating = f',\n            rating="{self.rating}"' if self.rating else ''
        rating_int = f',\n            rating_int={self.rating_int}' if self.rating_int else ''
        date_upload = f',\n            date_upload="{self.date_upload}"' if self.date_upload else ''
        date_upload_seconds = f',\n            date_upload_seconds={self.date_upload_seconds}' if self.date_upload_seconds else ''
        duration = f',\n            duration={self.duration}' if self.duration else ''
        duration_seconds = f',\n            duration_seconds={self.duration_seconds}' if self.duration_seconds else ''

        return f'''
        {self.site_name.lower()}_video(
            title="{self.title}", 
            time="{self.time}", 
            url="{self.url}", 
            url_font="{self.url_font}", 
            thumbnail="{self.thumbnail}",
            site_name="{self.site_name}",
            page_number={self.page_number}{stats}{views}{views_int}{rating}{rating_int}{date_upload}{date_upload_seconds}{duration}{duration_seconds}{preview}{indice})'''



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
    rating:str=None
    duration_seconds:int=None
    upload_date:str=None
    views_int:int=None
    likes:int=None
    person:str=None
    tags:str=None
    

    def __repr__(self) -> str:
        #stats = f',\n            stats="{self.stats}"' if self.stats else ''
        #preview = f',\n            preview="{self.preview}"' if self.preview else ''
        #indice = f',\n            indice={self.indice}' if not self.indice==None else ''
        #views = f',\n            views="{self.views}"' if self.views else ''
        views_int = f',\n        views_int={self.views_int}' if self.views_int else ''
        #rating = f',\n            rating="{self.rating}"' if self.rating else ''
        #rating_int = f',\n            rating_int={self.rating_int}' if self.rating_int else ''
        upload_date = f',\n        upload_date="{self.upload_date}"' if self.upload_date else ''
        #date_upload_seconds = f',\n            date_upload_seconds={self.date_upload_seconds}' if self.date_upload_seconds else ''
        #duration = f',\n            duration={self.duration}' if self.duration else ''
        duration_seconds = f',\n        duration_seconds={self.duration_seconds}' if self.duration_seconds else ''
        likes = f',\n        likes={self.likes}' if self.duration_seconds else ''
        person = f',\n        person="{self.person}"' if self.duration_seconds else ''
        tags = f',\n        tags="{self.tags}"' if self.tags else ''
        rating = f',\n        rating="{self.rating}"' if self.rating else ''

        return f'''
    EmbedVideo{self.site_name}(
        title="{self.title}", 
        time="{self.time}", 
        url="{self.url}", 
        thumbnail="{self.thumbnail}", 
        views="{self.views}", 
        time_published="{self.time_published}"{rating}{views_int}{duration_seconds}{likes}{upload_date}{person}{tags},
        len_videos_sugestions={self.len_videos_sugestions},
        videos_sugestions={self.videos_sugestions})'''


