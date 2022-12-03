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
	list_a = html_parser.find_all('a',{'role':'menuitem'})
	list_url = []
	
	for ls in list_a:
	  #print(ls['class'])
	  if 'p-2' in ls['class']:
	    #print(ls)
	    list_url.append(f'{url_base}/{ls["href"]}')
	return list_url
	
	

	
