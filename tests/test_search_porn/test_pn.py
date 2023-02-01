from dreams import pornone as pn, __version__
print(__version__)



def test_search_porn():
    print('search] \n')
    vds = pn.search_porn('lorena aquino')
    print(vds,'\n')
    vds = vds.videos





def test_end_search():
    print('end_search] \n')
    vds = pn.search_porn('asdcwseffefsrrg')
    print(vds.len_videos)
    print(vds)
    assert not vds.len_videos, 'dont return end page search'
    
    print(vds)
    vds = pn.search_porn('lorena aquino',page_limit=60)
    assert vds.len_pages < 60, 'ops. page_limit < page_get'
    
    
test_search_porn()
test_end_search()