
import dreams.pornone as pn

vds = pn.search_porn('pamela rios mother',page_limit=20)

for vd in vds['videos']:
	print(vd,'\n')

print(pn.get_video_embed(vds['videos'][0]))