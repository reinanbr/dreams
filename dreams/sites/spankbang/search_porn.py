from dreams.sites.spankbang.schoolbag import url_base,argument_bool_throw_error_find_videos,site_name,br,puts,work_stats,bs,VideoData,HTMLSession,load_cookies,save_cookies
from dreams.utils.settings import headers
import http.cookiejar
import requests as rq
import os
asession = HTMLSession()
import cloudscraper
scrapper = cloudscraper.create_scraper()
#headers = {'User-Agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36(KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-URL-Manager Mobile Safari/537.36'}
# s = rq.Session()
# s.cookies = http.cookiejar.MozillaCookieJar(
    # 
path_cookies=".cookies_spankbang.json"
scrapper.headers = headers
def get_videos_bg_link(url:str,page_number:int,query:str) -> list[VideoData]:
    assert (url_base in url), '[error spankbang]: it is not a url from spankbang!'
    #url = 'https://getdatausers.000webhostapp.com/index.php?file=views_headers'
    if os.path.isfile(path_cookies):
        load_cookies(scrapper,path_cookies)
        #print(scrapper.cookies)
    url_html = scrapper.get(url) # br.open(url)

    save_cookies(url_html,path_cookies)
    #print(url_html.url)
    url_html = url_html.text
    #print(url_html)
    html_parser = bs(url_html,features="html.parser")
    print(html_parser)
    try:
        video_div = html_parser.find_all('div',{'class':'video-item'})
    except:
        if argument_bool_throw_error_find_videos:
            pass
            return False
        else:
            raise Exception('[error spankbang]: dont find any videos here page!')

    list_video = []
    #'''it work line, is for stopping the code in end page search'''
    if 'We could not find any videos for ' in html_parser.get_text():
        puts('Ops! end page search!')
        return False

    indice = 0
    for video in video_div:
        url_video = f"{url_base}{video.find('a')['href']}"
        title_video = video.find('img')['alt']
        time_video = video.find('span',{'class':'l'}).text
        url_img_video = video.find('img')['data-src']
        stats = video.find('div',{'class':'stats'}).text #find('span').text

        stats=stats.replace('aa',' ').replace('\n\n\n','')
        stats_w = work_stats(stats)

        views = stats_w['int']['views']
        date_upload = stats_w['int']['date_upload']
        rating = stats_w['int']['rating']
        
        views_str = stats_w['str']['views']
        date_upload_str = stats_w['str']['date_upload']
        rating_str = stats_w['str']['rating']
        
        try:
            gif_url = video.find('img')['data-preview']
        except:
            gif_url = None
            pass

        dur = int(time_video.split(' min')[0])*60

        Vid = VideoData(title=title_video,
                        time=time_video,
                        duration_seconds=dur,
                        stats=None,
                        views=views_str,
                        rating=rating_str,
                        date_upload=date_upload_str,
                        views_int=views,
                        date_upload_seconds=date_upload,
                        rating_int=rating,
                        page_number=page_number,
                        url=url_video,
                        url_font=url,
                        thumbnail=url_img_video,
                        preview=gif_url,
                        site_name=site_name,
                        indice=indice)
        list_video.append(Vid)
        indice = indice+1
        #count_video_ = count_video_ + 1
        #print(f'video: {title_video} - {time_video} [{url}]')
    return list_video

