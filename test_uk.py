import dreams.ukevids as uk

vds = uk.search_porn('natasha nice',page_limit=40)

i = 0
for vd in vds['videos']:
    i = i+1
    print(f'[video N° {i}]:',vd,'\n')
