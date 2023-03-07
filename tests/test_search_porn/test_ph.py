from dreams import pornhub as ph, __version__
print(__version__)



def test_search_porn():
    print('search] \n')
    vds = ph.search_porn('lorena aquino')
    print(vds,'\n')
    #vds = vds.videos
    assert vds.len_videos>5, f'error, the code {ph.site_name} dont getting videos'







def test_end_search():
    print('end_search] \n')
    vds = ph.search_porn('asdcwseffefsrrg')
    print(vds.len_videos)
    print(vds)
    assert not vds.len_videos, 'dont return end page search'
    
    print(vds)
    vds = ph.search_porn('lorena aquino',page_limit=60)
    assert vds.len_pages < 60, 'ops. page_limit < page_get'
    
    
test_search_porn()
test_end_search()