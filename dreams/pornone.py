from bs4 import BeautifulSoup as bs
import requests as rq

import mechanicalsoup as mec
import re

br = mec.StatefulBrowser()


headers = {'User-Agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36(KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-URL-Manager Mobile Safari/537.36'}



br.session.headers = headers
br.session.headers.update(headers)

def search_porn(query,num=20,lang='pt-BR',long=False):
	#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko), Chrome/61.0.3163.100 Safari/537.36'}
	query = '+'.join(query.split(' '))
	#br.addheaders = headers

	#query = '%20'.join(query.split(' '))
	list_div_content = []
	list_div_info = []
#url_test='https://pornoklad.me/videos/pyshnaya-mamka-s-seksualnymi-formami/'

#	print(f'page n:{i}')
	url_base='https://pornone.com'
	
	
	url = f'{url_base}/search/?q={query}'
	
	url_html = br.get(url)
	url_html = url_html.text
	
	html_parser = bs(url_html,features="html.parser")
	
	#list_a = html_parser.find_all('a')
	list_a = html_parser.find_all('a',{'class':'relative overflow-hidden flex-grow sm:flex-initial bg-white-two dark:bg-black-dark md:h-[235px] border dark:border-black-33 portrait:rounded-none rounded-xl shadow-sm shadow-gray-two dark:shadow-black-three shadow-opacity-5 tracking-normal links'})
	list_img = html_parser.find_all('img',{'width':'270'})
	list_span_dur = html_parser.find_all('span',{'class':'rounded text-f11 font-semibold leading-4 text-white ml-2 bg-black-two px-[5px] py-[2px] bg-opacity-50'})
	list_url = []
	list_title = []
	list_imgs = []
	list_dur = []
	
	list_video = []
	
	for span_dur in list_span_dur:
	  list_dur.append(span_dur.text)
	
	
	for img in list_img:
	  if 'imgvideo' in img['class']:
	    list_imgs.append(img['src'])
	    list_title.append(img['alt'])
	
	#list_url = list_a
	for ls in list_a:
	  list_url.append(ls['href'])
	  #print(ls['href'])
# 	  if 'p-2' in ls['class']:
# 	    #print(ls)
# 	    list_url.append(f'{url_base}/{ls["href"]}')
	    
	for i in range(len(list_url)):
	  video = {'url':list_url[i],'imgUrl':list_imgs[i],
	           'duration':list_dur[i],'title':list_title[i]}
	  list_video.append(video)
	return list_video
	
	
#query = 'tony tigrao emrrabando joyce oliveira'
#print((search_porn(query)))
	
	

	
