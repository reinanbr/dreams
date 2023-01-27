from dreams import pornone as pn



def test_search_porn():
    vds = pn.search_porn('lorena aquino').videos


    for vd in vds:
        print(vd,'\n')