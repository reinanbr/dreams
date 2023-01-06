from bs4 import BeautifulSoup as bs
import requests as rq
import http.cookiejar
from dreams.settings import puts
from requests_html import HTMLSession
asession = HTMLSession()


#import mechanicalsoup as mec
import re





from dreams.settings import argument_bool_throw_error_find_videos, search_porn_base
import kitano.logging as lg

site_name = 'pornone'
lg.str_date(f'[%H:%M:%S %d/%m/%Y ({site_name})]: ')


headers = {'user-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36(KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-URL-Manager Mobile Safari/537.36',
            'connection': 'keep-alive', 'upgrade-insecure-requests': '1',
#            'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-A225M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'pt-BR,pt-PT;q=0.9,pt;q=0.8,en-US;q=0.7,en;q=0.6'}




url_base='https://pornone.com'
s = rq.Session()
#s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
s.headers = headers
s.cookies = http.cookiejar.MozillaCookieJar("all_cookies.txt")

# br = mec.StatefulBrowser()
# br.session.headers = headers
# br.session.headers.update(headers)








def get_videos_bg_link(url:str,page_number:int) -> list:
    #print(url)
    assert (url_base in url), f'[error {site_name}]: it is not a url from {site_name}!'
    # loc = url
    # seen = []
    # while True:
    #  r = rq.get(loc, allow_redirects=False)
    #  #print(r.headers)
    #  loc = r.headers['location']
    #  if loc in seen:
    #      break
    #  seen.append(loc)
    #  print(loc)

    #print(url)
    url_html = asession.get(url)
    #print(url_html.headers) #rq.get(url,headers=headers,allow_redirects=True)
    #print(dir(url_html))
    #print(url_html.url)
    #print(url_html.text)
    url = url_html.url
    url_html = url_html.text
    #print(url_html)
    html_parser = bs(url_html,features="html.parser")
    list_video = []
    if 'Pornstar rank' in url_html:
        pornstar = html_parser.find('h1',{'class':'text-3xl'}).text #url_html.find('')
        url = f'{url}{page_number}/'
        puts(f'is page pornstar from {pornstar} - {url}')
        
        
        try:
            heaven = html_parser.find('div',{'class':'portrait:gap-x-0.1'})
            #puts('heaven is find!') 
            # error: 'No videos for this user.'
            #print(heaven)#video_div = html_parser.find_all('div',{'class':'video-item'})
        except:
            if argument_bool_throw_error_find_videos:
                pass
                return False
            else:
                raise Exception(f'[error {site_name}]: dont find any videos here page!')

        
        videos = heaven.find_all('a',{'class':'relative'})
        for vd in videos:
            title_video = vd.find('div',{'class':'leading-[22px]'}).text
            time_video = vd.find('span',{'class':'text-f13'}).text
            stats = vd.find('div',{'class':'vidInfo'}).text
            url_img = vd.find('img',{'class':'imgvideo'})['src']
            url_video = vd['href']


            min,seg = time_video.split(':')[0],time_video.split(':')[1]
            dur = (int(min)*60)+int(seg)

            vid = {'title':title_video,
                    'time':time_video,
                    'dur':dur,
                    'stats':stats,
                    'page_number':page_number,
                    'url':url_video,
                    'url_font':url,
                    'thumbnail':url_img,

                    #'gif':gif_url,
            }
            list_video.append(vid)
        return list_video


    else:
       #puts(f'is not page pornstar - {url}')

    #assert (not ('We could not find any videos for' in  html_parser.get_text())), '[error spankbang]: site dont have videos more here page!'

       try:
         heaven = html_parser.find('div',{'class':'mt-1'})
         #print(heaven)#video_div = html_parser.find_all('div',{'class':'video-item'})
       except:
        if argument_bool_throw_error_find_videos:
            pass
            return False
        else:
            raise Exception(f'[error {site_name}]: dont find any videos here page!')


       videos = heaven.find_all('a',{'class':'relative'})
       #print(len(videos))
       for vd in videos:
        title_video = vd.find('div',{'class':'leading-[22px]'}).text
        time_video = vd.find('span',{'class':'text-f13'}).text
        stats = vd.find('div',{'class':'vidInfo'}).text
        url_img = vd.find('img',{'class':'imgvideo'})['src']
        url_video = vd['href']


        min,seg = time_video.split(':')[0],time_video.split(':')[1]
        dur = (int(min)*60)+int(seg)

        vid = {'title':title_video,
                'time':time_video,
                'dur':dur,
                'stats':stats,
                'page_number':page_number,
                'url':url_video,
                'url_font':url,
                'thumbnail':url_img,

                #'gif':gif_url,
        }
        list_video.append(vid)
       return list_video







def url_base_search_page(query,p):
    url_search= f'{url_base}/search/?q={query}&sort=relevance&filter=&page={p}' #f'{url_base}/search/?q={query}'
    #print(url_search)
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
                            page_limit=page_limit,
                            page_number=page_number,
                            call_get_videos_site=get_videos_bg_link,
                            url_base_page_number_search=url_base_search_page)




def get_video_embed(video):
    res = asession.get(video['url'])
    #print(res.text)
    html_parser = bs(res.text,features="html.parser")

    video = html_parser.find('video')
    link = video.find('source')['src']
    
    return link
