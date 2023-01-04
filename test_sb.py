import dreams.spankbang as sb

vds = sb.search_porn('natasha nice',page_limit=3)

i = 0
for vd in vds['videos']:
    i = i+1
    print(f'[video N° {i}]:',vd,'\n')
