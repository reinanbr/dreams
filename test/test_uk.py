import dreams.ukevids as uk

vds = uk.search_porn('natasha nice',page_limit=10)

i = 0
for key in vds.keys():
    if key=='videos':
        break
    print(f'{key}: {vds[key]}')
    
for vd in vds['videos']:
    i = i+1
    print(f'[video N° {i}]:',vd,'\n')
