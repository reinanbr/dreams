from dreams.sites.spankbang.schoolbag import url_base,argument_bool_throw_error_find_videos,site_name,br,puts,work_stats,bs,VideoData




def get_videos_bg_link(url:str,page_number:int,query:str) -> list[VideoData]:

    assert (url_base in url), '[error spankbang]: it is not a url from spankbang!'

    url_html = br.get(url)
    url_html = url_html.text
    html_parser = bs(url_html,features="html.parser")

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
        stats = video.find('div',{'class':'stats'}).text

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

