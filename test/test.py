import dreams.playvids as pv
import dreams.noodlemagazine as nm
import dreams.ukevids as uk
import dreams.spankbang as sb


query = 'natasha nice'
page_limit = 100


# spankbang
sb_videos = sb.search_porn(query,page_limit)
print(f'spankbang search: {len(sb_videos)} videos')
print(sb_videos[0],'\n')

#nodlemagazine
nm_videos = nm.search_porn(query,page_limit)
print(f'nodlemagazine search: {len(nm_videos)} videos')
print(nm_videos[0],'\n')

#ukevids
uk_videos = uk.search_porn(query,page_limit)
print(f'ukevids search: {len(uk_videos)} videos')
print(uk_videos[0],'\n')

#playvids
pv_videos = pv.search_porn(query,page_limit)
print(f'playvids search: {len(pv_videos)} videos')
print(pv_videos[0])