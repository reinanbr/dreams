from dreams import ukdevilz as uk, __version__
print(__version__)


def test_search_porn():
    print('[search] \n')
    vds = uk.search_porn('lorena aquino')
    print(vds,'\n')
    vds = vds.videos


def test_end_search():
    print('end_search] \n')
    vds = uk.search_porn('asdcwseffefsrrg')
    print(vds)
    print(vds.len_videos)
    assert not vds.len_videos, 'dont return end page search'
   
    vds = uk.search_porn('lorena aquino',page_limit=60)
    print(vds)
    assert vds.len_pages < 60, 'ops. page_limit < page_get'
    



test_search_porn()
test_end_search()