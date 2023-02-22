from dreams.sites.spankbang.schoolbag import url_base,search_porn_base,site_name
from dreams.sites.spankbang.search_porn import get_videos_bg_link








def url_base_search_page(query,p):
    return f'{url_base}/s/{query}/{p}/?o=trending'




# ''' function search '''
def search_porn(query:str,page_limit:int=2,page_number=None)->search_porn_base:
    """ a simple function for return data video's porn from SpankBang search
     Args:
        query (str): _the argument for to searching in the site porn
        page_number (int): getting video's from only it page number. Defaults to None.
        page_limit (int, optional): _page number limit for getting . Defaults to 2.

    Returns:
        dict: dict with list video's data, ping info, site name, lens video's data

    Example:
        >>> import dreams.spankbang as sb
        >>> sb.search_porn('natasha nice',page_limit=1)
        {'url_base': 'https://spankbang.com', 'query': 'natasha+nice', 'ping': 2.200756072998047, 'len_videos': 98, 'videos': [{'url': 'https://spankbang.com/7btrt/video/natasha+nice+stepmom+natasha+s+big+tit+cum+candy+treat', 'url_img': 'https://tb-lb.sb-cd.com/t/12309113/1/2/w:800/t6-enh/natasha-nice-stepmom-natasha.jpg', 'title': "Natasha Nice - Stepmom Natasha'S Big Tit Cum Candy Treat", 'time': '43 min', 'gif': 'https://tbv.sb-cd.com/t/12309113/1/2/td.mp4', 'stats': '150K 100% 2 months', 'dur': 2580}, ...

    """
    return search_porn_base(query=query,
                            url_base=url_base,
                            page_limit=page_limit,
                            site_name=site_name,
                            page_number=page_number,
                            call_get_videos_site=get_videos_bg_link,
                            url_base_page_number_search=url_base_search_page)


