import dreams.ukevids as uk

vds = uk.search_porn('natasha nice',page_limit=20)

i = 1
size = len(vds['videos'])
for vd in vds['videos']:
	url_video = uk.get_video_url(vd)
	print(vd)
	print(f'video url[{i}/{size}]: {url_video}','\n')
	i = i+1
