from dreams import tnaflix as tn



def test_search_porn():
    vds = tn.search_porn('lorena aquino').videos


    for vd in vds:
        print(vd,'\n')