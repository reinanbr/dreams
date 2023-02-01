from dreams import tnaflix as tn, __version__
print(__version__)



def test_search_porn():
    print('search] \n')
    vds = tn.search_porn('lorena aquino')
    print(vds,'\n')
    vds = vds.videos



def test_end_search():
    print('end_search] \n')
    vds = tn.search_porn('asdcwseffefsrrg')
    print(vds.len_videos)
    print(vds)
    assert not vds.len_videos, 'dont return end page search'
    vds = tn.search_porn('lorena aquino',page_limit=90)
    print(vds)
    print('pages: ',vds.len_pages)
    assert vds.len_pages < 90, 'ops. page_limit < page_get'
    print('pages: ',vds.len_pages)
    
    
    
test_search_porn()
test_end_search()