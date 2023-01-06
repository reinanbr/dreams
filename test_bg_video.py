import dreams.spankbang as sb

query = 'natasha nice'
page_limit = 2



sb_videos = sb.search_porn(query,page_limit)

print(f'data: {sb_videos}','\n')

print(f'{len(sb_videos["videos"])} videos','\n')


print('first video from list:\n',sb_videos["videos"][0],'\n')
