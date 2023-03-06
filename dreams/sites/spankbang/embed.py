from dreams.sites.spankbang.schoolbag import url_base,br,bs,site_name,VideoData,EmbedVideo,load_cookies,save_cookies
import cloudscraper
from dreams.utils.settings import headers
import os
scrapper = cloudscraper.create_scraper()#cloudscraper.CloudScraper()
scrapper.headers = headers
path_cookies = '.cookies_spankbang.json'


def get_video_embed(url)->EmbedVideo:
    if os.path.isfile(path_cookies):
        load_cookies(scrapper,path_cookies)
    res = scrapper.get(url)
    save_cookies(res,path_cookies)
    html_parser = bs(res.text,features="html.parser")
    title =  html_parser.find('h1').text
    time = html_parser.find('span',{'class':'i-length'}).text
    players = html_parser.find('span',{'class':'i-plays'}).text
    time_published = html_parser.find('span',{'class':'i-date'}).text #.find('section',{'class':'details'}).find('p').text
    image_thumbnail = html_parser.find('img',{'class':'player_thumb'})['src']

    video = html_parser.find('video')
    link = video.find('source')['src']#.split('?')[0]
    indice_sugestions = 0
    list_video_sugestions = []
    for video_sugestion in html_parser.find_all('div',{'class':'video-item'}):
        url_video = f"{url_base}{video_sugestion.find('a')['href']}"
        title_video = video_sugestion.find('img')['alt']
        time_video = video_sugestion.find('span',{'class':'l'}).text
        url_img_video = video_sugestion.find('img')['data-src']
        try:
            stats = video_sugestion.find('div',{'class':'stats'}).text#[span.text for span in video_sugestion.find_all('span')]
            stats=stats.replace('\n',' ').replace('\n\n','').replace('(','').replace(')','').replace("'",'').replace('\xa0','').replace(',','')
        except:
            stats = None
        gif_url = video_sugestion.find('img').get('data-preview', None)
        dur = int(time_video.split('m')[0])*60

        Vid = VideoData(title=title_video,
                        time=time_video,
                        duration=dur,
                        stats=stats,
                        page_number=None,
                        url=url_video,
                        url_font=url,
                        thumbnail=url_img_video,
                        preview=gif_url,
                        site_name=site_name,
                        indice=indice_sugestions)
        list_video_sugestions.append(Vid)
        indice_sugestions = indice_sugestions+1
    
    return EmbedVideo(site_name=site_name,
                      url=link,
                      title=title,
                      time=time,
                      thumbnail=image_thumbnail,
                      time_published=time_published,
                      views=players,
                      len_videos_sugestions=indice_sugestions-1,
                      videos_sugestions=list_video_sugestions)



