from dreams import tnaflix as tn, __version__
print(__version__)



def test_search_porn():
    vds = tn.search_porn('lorena aquino')
    print(vds,'\n')
    vds = vds.videos



test_search_porn()