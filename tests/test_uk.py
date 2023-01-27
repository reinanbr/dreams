from dreams import ukdelviz as uk


def test_search_porn():
    vds = uk.search_porn('lorena aquino').videos

    for vd in vds:
        print(vd,'\n')