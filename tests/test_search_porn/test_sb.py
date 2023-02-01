from dreams import spankbang as sb, __version__
print(__version__)



def test_search_porn():
    print('search] \n')
    vds = sb.search_porn('lorena aquino')
    print(vds,'\n')
    assert vds
    vds = vds.videos
    assert vds




def test_end_search():
    print('end_search] \n')
    vds = sb.search_porn('asdcwseffefsrrg')
    print(vds.len_videos)
    print(vds)
    assert not vds.len_videos, 'dont return end page search'

    print(vds)
    vds = sb.search_porn('lorena aquino',page_limit=90)
    assert vds.len_pages < 90, 'ops. page_limit < page_get'
    
    
    
    
test_search_porn()
test_end_search()