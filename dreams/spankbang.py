from bs4 import BeautifulSoup as bs
import requests as rq

import mechanicalsoup as mec
import re

br = mec.StatefulBrowser()


headers = {'User-Agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36(KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-URL-Manager Mobile Safari/537.36'}



br.session.headers = headers
br.session.headers.update(headers)




def search_porn(query,page_limit=2,lang='pt-BR',long=False):
    print('[spankbang]')
    #headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko), Chrome/61.0.3163.100 Safari/537.36'}
    query = '+'.join(query.split(' '))
    #br.addheaders = headers

    #query = '%20'.join(query.split(' '))
    list_div_content = []
    list_div_info = []
    url_base='https://spankbang.com'
	
    p = 1
    N = page_limit
    list_video = []
    for i in range(N):
        url = f'{url_base}/s/{query}/{p}/?o=all'
        
        url_html = br.get(url)
        url_html = url_html.text
        
        html_parser = bs(url_html,features="html.parser")
        
        if 'We could not find any videos for' in  html_parser.get_text():
            #print('ops! find the end...')
            break
        
        video_div = html_parser.find_all('div',{'class':'video-item'})
        #print(len(list_video_div))
        for video in video_div:
             url_video = f"{url_base}{video.find('a')['href']}"
             title_video = video.find('img')['alt']
             time_video = video.find('span',{'class':'l'}).text
             url_img_video = video.find('img')['data-src']

             vid = {'url':url_video,
                    'url_img':url_img_video,
                     'title':title_video,
                     'time':time_video
             }
             list_video.append(vid)
        
        print('\r',end='')
        print(f'finding {len(list_video)} videos from {p} pages...',end='',flush=True)
        
        
        p = p + 1

            #print(video)
            #print()

            # 	for span_dur in list_span_dur:
            # 	  list_dur.append(span_dur.text)


            # 	for img in list_img:
            # 	  if 'imgvideo' in img['class']:
            # 	    list_imgs.append(img['src'])
            # 	    list_title.append(img['alt'])

            # 	#list_url = list_a
            # 	for ls in list_a:
            # 	  list_url.append(ls['href'])
            # 	  #print(ls['href'])
            # # 	  if 'p-2' in ls['class']:
            # # 	    #print(ls)
            # # 	    list_url.append(f'{url_base}/{ls["href"]}')

            # 	for i in range(len(list_url)):
            # 	  video = {'url':list_url[i],'imgUrl':list_imgs[i],
            # 	           'duration':list_dur[i],'title':list_title[i]}
            # 	  list_video.append(video)
    print('\n')
    return list_video
	
	
# query = 'alessandra marques'
# res = (search_porn(query))

# i=0
# for v in res:
#     print(f'[{i}]',v,'\n')
#     i=i+1

	
