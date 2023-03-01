# from dreams.sites.only.nudes7 import get_videos_nudes7_link as test

# print(test('https://nudes7.com/?s=mia+monroe',page_number=1,query='3'))

from dreams.sites.only import nudes7


def test_search():
    res = nudes7.search_porn('mia monroe')
    print(res)

test_search()