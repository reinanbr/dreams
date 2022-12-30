import dreams.ukevids as uk

vds = uk.search_porn('natasha_nice',page_limit=6)

def video_html(vd:dict) -> str:
	return f'''<div align="center"><a href="{vd['url']}"><img height='90px' width='160px' src="{vd['url_img']}"></a>
 					<p>{vd['title']} - {vd['time']}<br><span>[{vd['stats']}]</span></p><br/>'''

list_html = []

for vd in vds:
    list_html = list_html[::-1]
    list_html.append(video_html(vd))

with open('uk.html','w') as sb_page:
    sb_page.writelines(list_html)