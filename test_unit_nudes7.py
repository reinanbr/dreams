# from dreams.sites.only.nudes7 import get_videos_nudes7_link as test

# print(test('https://nudes7.com/?s=mia+monroe',page_number=1,query='3'))

from dreams.sites.only import nudes7

res = nudes7.search_porn('mia monroe')

for i, vid in enumerate(res.videos):
    print(i,vid)