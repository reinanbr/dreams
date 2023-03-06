from bs4 import BeautifulSoup as bs
from dreams.utils.settings import puts
from requests_html import HTMLSession
from dreams.utils.settings import argument_bool_throw_error_find_videos, search_porn_base,VideoData
import kitano.logging as lg




site_name = 'pornone'
lg.str_date(f'[%H:%M:%S %d/%m/%Y ({site_name})]: ')
url_base='https://pornone.com'

asession = HTMLSession()




def get_videos_bg_link(url:str,page_number:int,query:str) -> list:
    assert (url_base in url), f'[error {site_name}]: it is not a url from {site_name}!'
    url_html = asession.get(url)

    url = url_html.url
    url_html = url_html.text
    html_parser = bs(url_html,features="html.parser") # first look
    
    htm_parser = bs(asession.get(url).text,features='html.parser') # validation if it is it, or it is ok
    list_video = []
    
    #''' testing if it url is a page porn '''
    if 'Pornstar rank' in url_html:
        if 'No videos for this user.' in html_parser.get_text():
            puts('Ops! end page search!')
            return False

        pornstar = html_parser.find('h1',{'class':'text-3xl'}).text #url_html.find('')
        url = f'{url}{page_number}/'
        puts(f'is page pornstar from {pornstar} - {url}')

        try:
            heaven = html_parser.find('div',{'class':'portrait:gap-x-0.1'})
        except:
            if argument_bool_throw_error_find_videos:
                pass
                return False
            else:
                raise Exception(f'[error {site_name}]: dont find any videos here page!')

        #'''it work line, is for stopping the code in end page search'''
        if 'No videos for this user.' in html_parser.get_text():
            puts('Ops! end page search!')
            return False


        videos = heaven.find_all('a',{'class':'relative'})
        i = 0
        # getting info video from divVideos of htmlSite
        for vd in videos:
            title_video = vd.find('div',{'class':'leading-[22px]'}).text
            time_video = vd.find('span',{'class':'text-f13'}).text
            stats = vd.find('div',{'class':'vidInfo'}).text
            url_img = vd.find('img',{'class':'imgvideo'})['src']
            url_video = vd['href']
            min,seg = time_video.split(':')[0],time_video.split(':')[1]
            dur = (int(min)*60)+int(seg)

            Vid = VideoData(title=title_video,
                            time=time_video.replace('\n',''),
                            duration=dur,
                            page_number=page_number,
                            url=url_video,
                            url_font=url,
                            stats=stats.replace('\n',' ').replace('\n\n',' ').replace('\n\n\n',' '),
                            thumbnail=url_img,
                            site_name=site_name,
                            indice=i,
                            preview=None)
            i = i+1

            list_video.append(Vid)
        return list_video

    #'''if it is not a page porn'''
    else:

       #'''it work line, is for stopping the code in end page search'''
       if 'No results found for this criteria.' in html_parser.get_text():
            puts('Ops! end page search!')
            return False

       if query.count(' '):
        if '' in query.split(' '):
            query = query.split(' ')
            del query[query.index('')]
            query = ' '.join(query)
        if htm_parser.get_text().lower().count(query.split(' ')[0]) <= 2:
            puts('Ops! end page search! Query init dont found!')
            return False
       else:
           if htm_parser.get_text().lower().count(query) <= 2:
            puts('Ops! end page search! Query init dont found!')
            return False
        
       try:
         heaven = html_parser.find('div',{'class':'mt-1'})

       except:
        if argument_bool_throw_error_find_videos:
            pass
            return False
        else:
            raise Exception(f'[error {site_name}]: dont find any videos here page!')


       videos = heaven.find_all('a',{'class':'relative'})

       i= 0
       for vd in videos:
        title_video = vd.find('div',{'class':'leading-[22px]'}).text
        time_video = vd.find('span',{'class':'text-f13'}).text
        stats = vd.find('div',{'class':'vidInfo'}).text
        url_img = vd.find('img',{'class':'imgvideo'})['src']
        url_video = vd['href']


        min,seg = time_video.split(':')[0],time_video.split(':')[1]
        dur = (int(min)*60)+int(seg)

        Vid = VideoData(title=title_video,
                            time=time_video.replace('\n',''),
                            duration=dur,
                            page_number=page_number,
                            url=url_video,
                            stats=stats.replace('\n',' ').replace('\n\n',' ').replace('\n\n\n',' '),
                            url_font=url,
                            thumbnail=url_img,
                            site_name=site_name,
                            indice=i,
                            preview=None)
        i = i+1
        list_video.append(Vid)
       return list_video







def url_base_search_page(query,p):
    url_search= f'{url_base}/search/?q={query}&sort=relevance&filter=&page={p}' 
    return url_search



def search_porn(query:str,page_limit:int=2,page_number=None):
    """ a simple function for return data video's porn from Pornone site search

    Example:
        >>> import dreams.pornone as pn
        >>> pn.search_porn('natasha nice',page_limit=2)
        {'url_base': 'https://spankbang.com', 'query': 'natasha+nice', 'ping': 2.200756072998047, 'len_videos': 98, 'videos': [{'url': 'https://spankbang.com/7btrt/video/natasha+nice+stepmom+natasha+s+big+tit+cum+candy+treat', 'url_img': 'https://tb-lb.sb-cd.com/t/12309113/1/2/w:800/t6-enh/natasha-nice-stepmom-natasha.jpg', 'title': "Natasha Nice - Stepmom Natasha'S Big Tit Cum Candy Treat", 'time': '43 min', 'gif': 'https://tbv.sb-cd.com/t/12309113/1/2/td.mp4', 'stats': '150K 100% 2 months', 'dur': 2580}, ...


      Args:
        query (str): _the argument for to searching in the site porn
        page_number (int): getting video's from only it page number. Defaults to None.
        page_limit (int, optional): _page number limit for getting . Defaults to 2.

    Returns:
        dict: dict with list video's data, ping info, site name, lens video's data
    """
    return search_porn_base(query=query,
                            url_base=url_base,
                            site_name=site_name,
                            page_limit=None,
                            page_number=None,
                            call_get_videos_site=get_videos_bg_link,
                            url_base_page_number_search=url_base_search_page)




def get_video_embed(video):
    res = asession.get(video['url'])
    #print(res.text)
    html_parser = bs(res.text,features="html.parser")

    video = html_parser.find('video')
    link = video.find('source')['src']
    
    return link
